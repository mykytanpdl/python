from django.db.models import Count

from library.models import Book
from library.repositories.base_repository import BaseRepository


class BookRepository(BaseRepository):
    model = Book

    @classmethod
    def find_by_title(cls, title):
        return cls.model.objects.filter(title__icontains=title)

    @classmethod
    def find_by_genre(cls, genre_name):
        return cls.model.objects.filter(genres__name__iexact=genre_name)

    @classmethod
    def find_by_author(cls, author_name):
        return cls.model.objects.filter(bookauthor__author__last_name__icontains=author_name)

    @classmethod
    def find_by_language(cls, language):
        return cls.model.objects.filter(language__iexact=language)

    @classmethod
    def find_by_age_category(cls, age_category):
        return cls.model.objects.filter(age_category=age_category)

    @classmethod
    def available_books(cls):
        return cls.model.objects.filter(total_copies__gt=0)

    @classmethod
    def total_loans_per_book(cls):
        return (cls.model.objects.annotate(loan_count=Count('loan')).values('title', 'loan_count')
                .order_by('-loan_count'))

    @classmethod
    def total_loans_per_age_category(cls):
        return cls.model.objects.values('age_category').annotate(loan_count=Count('loan')).values('age_category', 'loan_count').order_by('-loan_count')

    @classmethod
    def total_books_per_year(cls):
        return cls.model.objects.values('publishing_year').annotate(book_count=Count('id')).values('publishing_year', 'book_count').order_by('-publishing_year')

    @classmethod
    def total_books_per_age_category(cls):
        return cls.model.objects.values('age_category').annotate(book_count=Count('id')).values('age_category', 'book_count').order_by('-book_count')

    @classmethod
    def total_books_per_type_of_cover(cls):
        return cls.model.objects.values('type_of_cover').annotate(book_count=Count('id')).values('type_of_cover', 'book_count').order_by('-book_count')

    @classmethod
    def total_books_per_language(cls):
        return cls.model.objects.values('language').annotate(book_count=Count('id')).values('language', 'book_count').order_by('-book_count')
