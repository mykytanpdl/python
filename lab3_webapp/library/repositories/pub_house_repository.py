from django.db.models import Count

from library.models import PublishingHouse
from library.repositories.base_repository import BaseRepository


class PublishingHouseRepository(BaseRepository):
    model = PublishingHouse

    @classmethod
    def find_by_city(cls, city):
        return cls.model.objects.filter(city__iexact=city)

    @classmethod
    def find_by_country(cls, country_name):
        return cls.model.objects.filter(country__name__iexact=country_name)

    @classmethod
    def total_books_per_publishing_house(cls):
        return cls.model.objects.annotate(book_count=Count('book')).values('name', 'book_count').order_by('-book_count')