from django.db.models import Count

from library.models import Reader
from library.repositories.base_repository import BaseRepository


class ReaderRepository(BaseRepository):
    model = Reader

    @classmethod
    def find_by_email(cls, email):
        return cls.model.objects.filter(email__iexact=email).first()

    @classmethod
    def find_by_phone_number(cls, phone_number):
        return cls.model.objects.filter(phone_number=phone_number).first()

    @classmethod
    def find_by_city(cls, city):
        return cls.model.objects.filter(city__iexact=city)

    @classmethod
    def total_loans_per_reader(cls):
        return cls.model.objects.annotate(loan_count=Count('loans')).values('first_name', 'last_name', 'loan_count').order_by('-loan_count')
