from django.db.models import Avg, Count

from library.models import Genre
from library.repositories.base_repository import BaseRepository


class GenreRepository(BaseRepository):
    model = Genre

    @classmethod
    def find_by_name(cls, name):
        return cls.model.objects.filter(name__iexact=name).first()

    @classmethod
    def total_books_per_genre(cls):
        return cls.model.objects.annotate(book_count=Count('books')).values('name', 'book_count').order_by('-book_count')

    @classmethod
    def avg_pages_per_genre(cls):
        return cls.model.objects.annotate(avg_pages=Avg('books__number_of_pages')).values('name', 'avg_pages').order_by('-avg_pages')

    @classmethod
    def total_loans_per_genre(cls):
        return cls.model.objects.annotate(loan_count=Count('books__loan')).values('name', 'loan_count').order_by('-loan_count')
