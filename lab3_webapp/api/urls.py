from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.get_books, name='get_books'),
    path('books/<int:book_id>/', views.get_book, name='get_book'),
    path('books/add/', views.add_book, name='add_book'),
    path('books/<int:book_id>/update/', views.update_book, name='update_book'),
    path('books/<int:book_id>/delete/', views.delete_book, name='delete_book'),

    path('readers/', views.get_readers, name='get_readers'),
    path('readers/<int:reader_id>/', views.get_reader, name='get_reader'),
    path('readers/add/', views.add_reader, name='add_reader'),
    path('readers/<int:reader_id>/update/', views.update_reader, name='update_reader'),
    path('readers/<int:reader_id>/delete/', views.delete_reader, name='delete_reader'),

    path('authors/', views.get_authors, name='get_authors'),
    path('authors/<int:author_id>/', views.get_author, name='get_author'),
    path('authors/add/', views.add_author, name='add_author'),
    path('authors/<int:author_id>/update/', views.update_author, name='update_author'),
    path('authors/<int:author_id>/delete/', views.delete_author, name='delete_author'),

    path('genres/', views.get_genres, name='get_genres'),
    path('genres/<int:genre_id>/', views.get_genre, name='get_genre'),
    path('genres/add/', views.add_genre, name='add_genre'),
    path('genres/<int:genre_id>/update/', views.update_genre, name='update_genre'),
    path('genres/<int:genre_id>/delete/', views.delete_genre, name='delete_genre'),

    path('loans/', views.get_loans, name='get_loans'),
    path('loans/<int:loan_id>/', views.get_loan, name='get_loan'),
    path('loans/add/', views.add_loan, name='add_loan'),
    path('loans/<int:loan_id>/update/', views.update_loan, name='update_loan'),
    path('loans/<int:loan_id>/delete/', views.delete_loan, name='delete_loan'),

    path('countries/', views.get_countries, name='get_countries'),
    path('countries/<int:country_id>/', views.get_country, name='get_country'),
    path('countries/add/', views.add_country, name='add_country'),
    path('countries/<int:country_id>/update/', views.update_country, name='update_country'),
    path('countries/<int:country_id>/delete/', views.delete_country, name='delete_country'),

    path('publishing_houses/', views.get_publishing_houses, name='get_publishing_houses'),
    path('publishing_houses/<int:publishing_house_id>/', views.get_publishing_house, name='get_publishing_house'),
    path('publishing_houses/add/', views.add_publishing_house, name='add_publishing_house'),
    path('publishing_houses/<int:publishing_house_id>/update/', views.update_publishing_house, name='update_publishing_house'),
    path('publishing_houses/<int:publishing_house_id>/delete/', views.delete_publishing_house, name='delete_publishing_house'),

    path('genres/total_books/', views.total_books_per_genre, name='total_books_per_genre'),
    path('genres/avg_pages/', views.avg_pages_per_genre, name='avg_pages_per_genre'),
    path('genres/total_loans/', views.total_loans_per_genre, name='total_loans_per_genre'),
    path('publishing_houses/total_books/', views.total_books_per_publishing_house,
         name='total_books_per_publishing_house'),
    path('books/total_loans/', views.total_loans_per_book, name='total_loans_per_book'),
    path('books/total_loans_per_age_category/', views.total_loans_per_age_category,
         name='total_loans_per_age_category'),
    path('books/total_books_per_year/', views.total_books_per_year, name='total_books_per_year'),
    path('readers/total_loans/', views.total_loans_per_reader, name='total_loans_per_reader'),
    path('authors/count_books/', views.count_books_by_author, name='count_books_by_author'),
]