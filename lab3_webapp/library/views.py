from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from library.repositories.author_repository import AuthorRepository
from library.repositories.book_repository import BookRepository
from library.repositories.loan_repository import LoanRepository
from library.repositories.pub_house_repository import PublishingHouseRepository
from library.repositories.reader_repository import ReaderRepository
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from bokeh.embed import components
from bokeh.layouts import column
from bokeh.models import ColumnDataSource, Tabs, TabPanel
from bokeh.plotting import figure
from bokeh.transform import cumsum
from django.shortcuts import render

from .forms import *
from .models import *

MODEL_MAP = {
    "book": Book,
    "author": Author,
    "reader": Reader,
    "genre": Genre,
    "publishing_house": PublishingHouse,
    "country": Country,
    "loan" : Loan
}

FORM_MAP = {
    "country": CountryForm,
    "publishing_house": PublishingHouseForm,
    "genre": GenreForm,
    "author": AuthorForm,
    "book": BookForm,
    "reader": ReaderForm,
    "loan": LoanForm,
}

def home(request):
    return render(request, 'home.html')

class DynamicListView(ListView):
    template_name = "list.html"

    def get_queryset(self):
        model_name = self.kwargs.get("model_name")
        model = MODEL_MAP.get(model_name.lower())
        if not model:
            raise ValueError(f"Model '{model_name}' not found.")
        return model.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        model_name = self.kwargs.get("model_name")
        model = MODEL_MAP[model_name.lower()]
        context["model_name"] = model_name.capitalize()
        context["field_names"] = [field.name for field in model._meta.fields]
        context["items"] = self.object_list
        return context


class DynamicDetailView(DetailView):
    template_name = "detail.html"

    def get_object(self):
        model_name = self.kwargs.get("model_name")
        model = MODEL_MAP.get(model_name.lower())
        if not model:
            raise ValueError(f"Model '{model_name}' not found.")
        return get_object_or_404(model, pk=self.kwargs.get("pk"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        model_name = self.kwargs.get("model_name")
        model = MODEL_MAP[model_name.lower()]
        context["model_name"] = model_name.capitalize()
        context["field_names"] = [field.name for field in model._meta.fields]
        context["item"] = self.object
        return context


class DynamicCreateView(CreateView):
    template_name = "form.html"

    def get_form_class(self):
        model_name = self.kwargs.get("model_name")
        form_class = FORM_MAP.get(model_name.lower())
        if not form_class:
            raise ValueError(f"Form for model '{model_name}' not found.")
        return form_class

    def form_valid(self, form):
        # Save the object and get the instance
        self.object = form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        model_name = self.kwargs.get("model_name")
        context["model_name"] = model_name.capitalize()
        context["form_title"] = f"Add New {model_name.capitalize()}"
        return context

    def get_success_url(self):
        model_name = self.kwargs.get("model_name")
        # Redirect to the detail page of the newly created object
        return reverse_lazy("detail", kwargs={"model_name": model_name.lower(), "pk": self.object.pk})



class DynamicUpdateView(UpdateView):
    template_name = "form.html"

    def get_form_class(self):
        model_name = self.kwargs.get("model_name")
        form_class = FORM_MAP.get(model_name.lower())
        if not form_class:
            raise ValueError(f"Form for model '{model_name}' not found.")
        return form_class

    def get_object(self):
        model_name = self.kwargs.get("model_name")
        model = MODEL_MAP.get(model_name.lower())
        if not model:
            raise ValueError(f"Model '{model_name}' not found.")
        return get_object_or_404(model, pk=self.kwargs.get("pk"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        model_name = self.kwargs.get("model_name")
        context["model_name"] = model_name.capitalize()
        context["form_title"] = f"Edit {model_name.capitalize()}"
        return context

    def get_success_url(self):
        model_name = self.kwargs.get("model_name")
        return reverse_lazy("list", kwargs={"model_name": model_name.lower()})


class DynamicDeleteView(DeleteView):
    template_name = "delete.html"

    def get_object(self):
        model_name = self.kwargs.get("model_name")
        model = MODEL_MAP.get(model_name.lower())
        if not model:
            raise ValueError(f"Model '{model_name}' not found.")
        return get_object_or_404(model, pk=self.kwargs.get("pk"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        model_name = self.kwargs.get("model_name")
        context["model_name"] = model_name.capitalize()
        return context

    def get_success_url(self):
        model_name = self.kwargs.get("model_name")
        return reverse_lazy("list", kwargs={"model_name": model_name.lower()})


def plotly_dashboard(request):
    books_per_year = BookRepository.total_books_per_year()
    loans_per_book = BookRepository.total_loans_per_book()
    loans_per_age_category = BookRepository.total_loans_per_age_category()
    loans_per_reader = ReaderRepository.total_loans_per_reader()
    books_by_author = AuthorRepository.count_books_by_author()
    books_per_publishing_house = PublishingHouseRepository.total_books_per_publishing_house()

    df_books_per_year = pd.DataFrame(books_per_year)
    df_loans_per_book = pd.DataFrame(loans_per_book)
    df_loans_per_age_category = pd.DataFrame(loans_per_age_category)
    df_loans_per_reader = pd.DataFrame(loans_per_reader)
    df_books_by_author = pd.DataFrame(books_by_author)
    df_books_per_publishing_house = pd.DataFrame(books_per_publishing_house)

    fig_books_per_year = px.area(df_books_per_year, x='publishing_year', y='book_count', title='Total Books Per Year')
    fig_loans_per_book = px.bar(df_loans_per_book, x='title', y='loan_count', title='Total Loans Per Book')
    fig_loans_per_age_category = px.pie(df_loans_per_age_category, names='age_category', values='loan_count', title='Total Loans Per Age Category')
    fig_loans_per_reader = px.funnel(df_loans_per_reader, x='first_name', y='loan_count', title='Total Loans Per Reader')
    fig_books_by_author = px.bar(df_books_by_author, x='last_name', y='book_count', title='Count of Books by Author')
    fig_books_per_publishing_house = px.pie(df_books_per_publishing_house, names='name', values='book_count', title='Total Books Per Publishing House')

    plots = {
        'fig_books_per_year': fig_books_per_year.to_html(full_html=False),
        'fig_loans_per_book': fig_loans_per_book.to_html(full_html=False),
        'fig_loans_per_age_category': fig_loans_per_age_category.to_html(full_html=False),
        'fig_loans_per_reader': fig_loans_per_reader.to_html(full_html=False),
        'fig_books_by_author': fig_books_by_author.to_html(full_html=False),
        'fig_books_per_publishing_house': fig_books_per_publishing_house.to_html(full_html=False),
    }

    return render(request, 'dashboard.html', {'plots': plots})


def plotly_interactive_dashboard(request):
    overdue_loans = pd.DataFrame(LoanRepository.overdue_loans())
    active_loans = pd.DataFrame(LoanRepository.active_loans())
    returned_loans = pd.DataFrame(LoanRepository.returned_loans())

    overdue_loans = overdue_loans.fillna({'book_title': 'No Data'}) if not overdue_loans.empty else pd.DataFrame(columns=['book_title', 'due_date'])
    active_loans = active_loans.fillna({'book_title': 'No Data'}) if not active_loans.empty else pd.DataFrame(columns=['book_title'])
    returned_loans = returned_loans.fillna({'book_title': 'No Data'}) if not returned_loans.empty else pd.DataFrame(columns=['book_title'])

    fig_loans = go.Figure()
    fig_loans.add_trace(go.Bar(x=overdue_loans['book_title'], y=overdue_loans['due_date'], name='Overdue Loans'))
    fig_loans.add_trace(go.Bar(x=active_loans['book_title'], y=active_loans['loan_date'], name='Active Loans'))
    fig_loans.add_trace(go.Bar(x=returned_loans['book_title'], y=returned_loans['return_date'], name='Returned Loans'))

    fig_loans.update_layout(
        updatemenus=[
            dict(
                buttons=list([
                    dict(label="Overdue Loans",
                         method="update",
                         args=[{"visible": [True, False, False]},
                               {"title": "Overdue Loans"}]),
                    dict(label="Active Loans",
                         method="update",
                         args=[{"visible": [False, True, False]},
                               {"title": "Active Loans"}]),
                    dict(label="Returned Loans",
                         method="update",
                         args=[{"visible": [False, False, True]},
                               {"title": "Returned Loans"}]),
                    dict(label="All",
                         method="update",
                         args=[{"visible": [True, True, True]},
                               {"title": "All Loans"}]),
                ]),
                direction="down",
                showactive=True,
            )
        ]
    )

    plot_html = fig_loans.to_html(full_html=False)

    return render(request, 'interactive_dashboard.html', {'plot_html': plot_html})


def bokeh_dashboard(request):
    books_per_year = BookRepository.total_books_per_year()
    loans_per_book = BookRepository.total_loans_per_book()
    loans_per_age_category = BookRepository.total_loans_per_age_category()
    loans_per_reader = ReaderRepository.total_loans_per_reader()
    books_by_author = AuthorRepository.count_books_by_author()
    books_per_publishing_house = PublishingHouseRepository.total_books_per_publishing_house()

    df_books_per_year = pd.DataFrame(books_per_year).sort_values('publishing_year')
    df_loans_per_book = pd.DataFrame(loans_per_book)
    df_loans_per_age_category = pd.DataFrame(loans_per_age_category)
    df_loans_per_reader = pd.DataFrame(loans_per_reader)
    df_books_by_author = pd.DataFrame(books_by_author)
    df_books_per_publishing_house = pd.DataFrame(books_per_publishing_house)


    source1 = ColumnDataSource(df_books_per_year)
    plot1 = figure(
        title="Total Books Per Year",
        x_axis_label="Publishing Year",
        y_axis_label="Book Count",
        height=400,
        sizing_mode="stretch_width",
        x_range=(df_books_per_year['publishing_year'].min(), df_books_per_year['publishing_year'].max()),
    )
    plot1.varea(x='publishing_year', y1=0, y2='book_count', source=source1, fill_alpha=0.5, color="blue")
    plot1.line(x='publishing_year', y='book_count', source=source1, line_width=2, color="blue")

    source2 = ColumnDataSource(df_loans_per_book)
    plot2 = figure(
        x_range=df_loans_per_book['title'].tolist(),
        title="Total Loans Per Book",
        x_axis_label="Books",
        y_axis_label="Loan Count",
        height=400,
        sizing_mode="stretch_width",
    )
    plot2.vbar(x='title', top='loan_count', width=0.8, source=source2, color="navy")
    plot2.xaxis.major_label_orientation = 0.5

    df_loans_per_age_category['angle'] = df_loans_per_age_category['loan_count'] / df_loans_per_age_category['loan_count'].sum() * 2 * 3.14159
    df_loans_per_age_category['color'] = ["#%02x%02x%02x" % (int(r), int(g), int(b)) for r, g, b in zip(
        np.random.randint(0, 255, len(df_loans_per_age_category)),
        np.random.randint(0, 255, len(df_loans_per_age_category)),
        np.random.randint(0, 255, len(df_loans_per_age_category))
    )]
    source3 = ColumnDataSource(df_loans_per_age_category)
    plot3 = figure(
        title="Total Loans Per Age Category",
        height=500,
        sizing_mode="stretch_width",
        toolbar_location=None,
        tools="hover",
        tooltips="@age_category: @loan_count",
        x_range=(-0.5, 1.0),
    )
    plot3.wedge(x=0, y=1, radius=0.2,
                start_angle=cumsum('angle', include_zero=True),
                end_angle=cumsum('angle'),
                line_color="white", fill_color='color', legend_field='age_category', source=source3)

    df_loans_per_reader = df_loans_per_reader.sort_values('loan_count', ascending=False)
    source4 = ColumnDataSource(df_loans_per_reader)
    plot4 = figure(
        x_range=df_loans_per_reader['first_name'].tolist(),
        title="Total Loans Per Reader",
        x_axis_label="Readers",
        y_axis_label="Loan Count",
        height=400,
        sizing_mode="stretch_width",
    )
    plot4.vbar(x='first_name', top='loan_count', width=0.8, source=source4, color="green")
    plot4.xaxis.major_label_orientation = 0.5


    source5 = ColumnDataSource(df_books_by_author)
    plot5 = figure(
        x_range=df_books_by_author['last_name'].tolist(),
        title="Count of Books by Author",
        x_axis_label="Authors",
        y_axis_label="Book Count",
        height=400,
        sizing_mode="stretch_width",
    )
    plot5.vbar(x='last_name', top='book_count', width=0.8, source=source5, color="purple")
    plot5.xaxis.major_label_orientation = 0.5


    df_books_per_publishing_house['angle'] = df_books_per_publishing_house['book_count'] / df_books_per_publishing_house['book_count'].sum() * 2 * 3.14159
    df_books_per_publishing_house['color'] = ["#%02x%02x%02x" % (int(r), int(g), int(b)) for r, g, b in zip(
        np.random.randint(0, 255, len(df_books_per_publishing_house)),
        np.random.randint(0, 255, len(df_books_per_publishing_house)),
        np.random.randint(0, 255, len(df_books_per_publishing_house))
    )]
    source6 = ColumnDataSource(df_books_per_publishing_house)
    plot6 = figure(
        title="Total Books Per Publishing House",
        height=500,
        sizing_mode="stretch_width",
        toolbar_location=None,
        tools="hover",
        tooltips="@name: @book_count",
        x_range=(-0.5, 1.0),
    )
    plot6.wedge(x=0, y=1, radius=0.2,
                start_angle=cumsum('angle', include_zero=True),
                end_angle=cumsum('angle'),
                line_color="white", fill_color='color', legend_field='name', source=source6)

    layout = column(
        plot1, plot2, plot3, plot4, plot5, plot6,
        sizing_mode="stretch_width",
        spacing=20
    )

    script, div = components(layout)
    return render(request, 'bokeh_dashboard.html', {'script': script, 'div': div})


def bokeh_interactive_dashboard(request):
    books_per_age_category = BookRepository.total_books_per_age_category()
    books_per_type_of_cover = BookRepository.total_books_per_type_of_cover()
    books_per_language = BookRepository.total_books_per_language()

    df_books_per_age_category = pd.DataFrame(books_per_age_category)
    df_books_per_type_of_cover = pd.DataFrame(books_per_type_of_cover)
    df_books_per_language = pd.DataFrame(books_per_language)

    source1 = ColumnDataSource(df_books_per_age_category)
    plot1 = figure(
        x_range=df_books_per_age_category['age_category'].tolist(),
        title="Total Books Per Age Category",
        x_axis_label="Age Category",
        y_axis_label="Book Count",
        height=400,
        sizing_mode="stretch_width",
    )
    plot1.vbar(x='age_category', top='book_count', width=0.8, source=source1, color="blue")
    plot1.xaxis.major_label_orientation = 0.5

    source2 = ColumnDataSource(df_books_per_type_of_cover)
    plot2 = figure(
        x_range=df_books_per_type_of_cover['type_of_cover'].tolist(),
        title="Total Books Per Type of Cover",
        x_axis_label="Type of Cover",
        y_axis_label="Book Count",
        height=400,
        sizing_mode="stretch_width",
    )
    plot2.vbar(x='type_of_cover', top='book_count', width=0.8, source=source2, color="green")
    plot2.xaxis.major_label_orientation = 0.5

    source3 = ColumnDataSource(df_books_per_language)
    plot3 = figure(
        x_range=df_books_per_language['language'].tolist(),
        title="Total Books Per Language",
        x_axis_label="Language",
        y_axis_label="Book Count",
        height=400,
        sizing_mode="stretch_width",
    )
    plot3.vbar(x='language', top='book_count', width=0.8, source=source3, color="purple")
    plot3.xaxis.major_label_orientation = 0.5

    tabs = Tabs(tabs=[
        TabPanel(child=plot1, title="age category"),
        TabPanel(child=plot2, title="type of cover"),
        TabPanel(child=plot3, title="language")
    ], sizing_mode='stretch_width')

    script, div = components(tabs)
    return render(request, 'bokeh_dashboard.html', {'script': script, 'div': div})