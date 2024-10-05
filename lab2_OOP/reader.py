class Reader:
    _counter = 1

    @staticmethod
    def validate_email(email: str):
        if email.count("@") != 1 or email.count(".") < 1:
            raise ValueError(f"{email} is not a valid email")
        return True

    def __init__(self, first_name: str, last_name: str, email: str):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self._id = Reader._counter
        Reader._counter += 1
        self.borrowed_books = []

    def borrow_book(self, book):
        self.borrowed_books.append(book)
        print(f"{self} borrowed {book}")

    def return_book(self, book):
        self.borrowed_books.remove(book)
        print(f"{self} returned {book}")

    def has_book(self, book):
        return book in self.borrowed_books

    @property
    def id(self):
        return self._id

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        assert Reader.validate_email(email)
        self._email = email

    def __repr__(self):
        return f"Reader {self.first_name} {self.last_name}"