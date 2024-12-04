from django.db.models import Q, Count

from library.models import Author
from library.repositories.base_repository import BaseRepository


class AuthorRepository(BaseRepository):
    model = Author

    @classmethod
    def find_by_name(cls, first_name=None, last_name=None):
        query = Q()
        if first_name:
            query &= Q(first_name__icontains=first_name)
        if last_name:
            query &= Q(last_name__icontains=last_name)
        return cls.model.objects.filter(query)

    @classmethod
    def find_by_country(cls, country_name):
        return cls.model.objects.filter(country__name__iexact=country_name)

    @classmethod
    def find_living_authors(cls):
        return cls.model.objects.filter(year_of_death__isnull=True)

    @classmethod
    def find_deceased_authors(cls):
        return cls.model.objects.filter(year_of_death__isnull=False)

    @classmethod
    def count_books_by_author(cls):
        return cls.model.objects.annotate(book_count=Count('books')).values('first_name', 'last_name', 'book_count').order_by('-book_count')
