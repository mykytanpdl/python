from django.db.models import F
from django.utils import timezone

from library.models import Loan
from library.repositories.base_repository import BaseRepository


class LoanRepository(BaseRepository):
    model = Loan

    @classmethod
    def find_by_reader(cls, reader_id):
        return cls.model.objects.filter(reader_id=reader_id)

    @classmethod
    def find_by_book(cls, book_id):
        return cls.model.objects.filter(book_id=book_id)

    @staticmethod
    def all_loans():
        return Loan.objects.select_related('book').values(
            'id', 'loan_date', 'due_date', 'return_date', 'reader', book_title=F('book__title')
        )

    @staticmethod
    def overdue_loans():
        return Loan.objects.filter(return_date__isnull=True, due_date__lt=timezone.now()).select_related('book').values(
            'id', 'loan_date', 'due_date', 'return_date', 'reader', book_title=F('book__title')
        )

    @staticmethod
    def active_loans():
        return Loan.objects.filter(return_date__isnull=True).select_related('book').values(
            'id', 'loan_date', 'due_date', 'return_date', 'reader', book_title=F('book__title')
        )

    @staticmethod
    def returned_loans():
        return Loan.objects.filter(return_date__isnull=False).select_related('book').values(
            'id', 'loan_date', 'due_date', 'return_date', 'reader', book_title=F('book__title')
        )