from book import Book
from loan import Loan
from reader import Reader


class Library:
    def __init__(self, name):
        self.name = name
        self._readers = {}
        self._books = {}
        self._loans = []

    def add_book(self, book):
        if book.title in self._books.keys():
            self._books[book.title][1] += 1
        else:
            self._books[book.title] = [book, 1]
        print(f'Book "{book.title}" is now on the shelves of {self}!')

    def add_reader(self, reader):
        if reader.id not in self._readers.keys():
            self._readers[reader.id] = reader
            print(f"{reader}, welcome to {self}!")
        else:
            print(f"{reader} is already a member of {self}")

    def new_book(self, title: str, author: str, isbn: str):
        book = Book(title, author, isbn)
        self.add_book(book)
        return book

    def new_reader(self, first_name: str, last_name: str, email: str):
        for reader in self._readers.values():
            if reader.email == email:
                print(f"Reader with email {email} already exists.")
                return reader
        reader = Reader(first_name, last_name, email)
        self.add_reader(reader)
        return reader

    def get_reader_by_id(self, id_: int):
        return self._readers.get(id_)

    def get_book_by_title(self, title: str):
        return self._books.get(title)

    def take_book(self, reader, book):
        if reader.id in self._readers.keys() and book.title in self._books.keys():
            if reader.has_book(book):
                print(f"{reader} already has {book}")
            elif self._books[book.title][1] > 0:
                self._loans.append(Loan(reader, book))
                self._books[book.title][1] -= 1
                reader.borrow_book(book)
            else:
                print(f"The {book} is not available now")
        else:
            print("Reader or book title does not exist")

    def return_book(self, reader, book):
        if reader.id in self._readers.keys() and book.title in self._books.keys():
            for l in self._loans:
                if l.reader == reader and l.book == book:
                    l.set_returned()
                    self._books[book.title][1] += 1
                    reader.return_book(book)
                    break
            else:
                print(f"{reader} did not borrow {book}")
        else:
            print("Reader or book title does not exist")

    @property
    def readers(self):
        return self._readers

    @property
    def books(self):
        return self._books

    @property
    def loans(self):
        return self._loans

    def __repr__(self):
        return f"{self.name} library"


class OnlineResource:
    def __init__(self, url: str):
        self.url = url

    def __repr__(self):
        return f"Online resource at {self.url}"

    def access_resource(self):
        print(f"Accessing online resource at {self.url}")


class DigitalLibrary(Library, OnlineResource):
    def __init__(self, name: str, url: str):
        Library.__init__(self, name)
        OnlineResource.__init__(self, url)

    def __repr__(self):
        return f'"{self.name}" digital library located at {self.url}'


class CityLibrary(Library):
    def __init__(self, name: str, city: str):
        super().__init__(name)
        self.city = city

    def __repr__(self):
        return f'"{self.name}" library located in {self.city}'
