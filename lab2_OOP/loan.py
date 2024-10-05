from datetime import date


class Loan:
    def __init__(self, reader, book):
        self._reader = reader
        self._book = book
        self._date = date.today()
        self.returned = False

    def set_returned(self):
        self.returned = True

    @property
    def reader(self):
        return self._reader

    @property
    def book(self):
        return self._book

    @property
    def date(self):
        return self._date
