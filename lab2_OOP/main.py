from book import Book
from reader import Reader
from library import Library, DigitalLibrary, CityLibrary

lib = Library("MyLibrary")
print(lib)
city_lib = CityLibrary("MyCityLibrary", "Lviv")
print(city_lib)
dig_lab = DigitalLibrary("MyDLibrary", "dlibrary.com")
print(dig_lab)

b1 = Book("1984", "George Orwell", "0000000000")
b2 = lib.new_book("Brave New World", "Aldous Huxley", "1111111111")
r1 = Reader("John", "White", "john.white@email.com")
r2 = lib.new_reader("Mary", "Black", "mary.black77@gmail.com")
r3 = lib.new_reader("Robert", "Black", "robert.black88@gmail.com")

lib.add_book(b1)
lib.add_book(b1)
lib.add_reader(r1)

lib.take_book(r1, b1)
lib.take_book(r2, b1)
lib.take_book(r3, b1)
lib.return_book(r1, b1)

lib.return_book(r2, b2)
lib.take_book(r2, b2)
lib.take_book(r2, b2)
lib.return_book(r2, b2)