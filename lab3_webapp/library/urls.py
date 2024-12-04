from django.urls import path
from . import views
from .views import (
    DynamicListView, DynamicDetailView,
    DynamicUpdateView, DynamicDeleteView, DynamicCreateView, home
)

urlpatterns = [
    path('', home, name='home'),
    path('<str:model_name>/list/', DynamicListView.as_view(), name='list'),
    path('<str:model_name>/<int:pk>/detail/', DynamicDetailView.as_view(), name='detail'),
    path('<str:model_name>/create/', DynamicCreateView.as_view(), name='create'),
    path('<str:model_name>/<int:pk>/update/', DynamicUpdateView.as_view(), name='update'),
    path('<str:model_name>/<int:pk>/delete/', DynamicDeleteView.as_view(), name='delete'),

    path('dashboard1/', views.plotly_dashboard, name='dashboard1'),
    path('interactive_dashboard1/', views.plotly_interactive_dashboard, name='interactive_dashboard1'),
    path('dashboard2/', views.bokeh_dashboard, name='dashboard2'),
    path('interactive_dashboard2/', views.bokeh_interactive_dashboard, name='interactive_dashboard2'),
]
