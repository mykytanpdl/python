from django import forms
from .models import Country, PublishingHouse, Genre, Author, Book, Reader, Loan

class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ['name']

class PublishingHouseForm(forms.ModelForm):
    class Meta:
        model = PublishingHouse
        fields = ['name', 'phone_number', 'email', 'country', 'city', 'street', 'house_number']

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name']

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'year_of_birth', 'year_of_death', 'country']

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title', 'publishing_house', 'publishing_year', 'ISBN',
            'number_of_pages', 'type_of_cover', 'language',
            'age_category', 'total_copies',
        ]
        """
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'publishing_year': forms.NumberInput(attrs={'class': 'form-control'}),
            'ISBN': forms.TextInput(attrs={'class': 'form-control'}),
            'number_of_pages': forms.NumberInput(attrs={'class': 'form-control'}),
            'type_of_cover': forms.Select(attrs={'class': 'form-select'}),
            'language': forms.TextInput(attrs={'class': 'form-control'}),
            'age_category': forms.TextInput(attrs={'class': 'form-control'}),
            'total_copies': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        """

class ReaderForm(forms.ModelForm):
    class Meta:
        model = Reader
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'passport_series', 'passport_number', 'city', 'street', 'house_number', 'apartment_number', 'zip_code']

class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ['book', 'reader', 'due_date', 'return_date']