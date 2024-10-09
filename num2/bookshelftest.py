# ファイル bookshelftest.py
from book import Book
from bookshelf2 import BookShelf2

book_shelf2 = BookShelf2()

book_shelf2.append_book(Book("Isaac Asimov", "I, Robot"))
book_shelf2.append_book(Book("Andy Weir", "Project Hail Mary"))
book_shelf2.append_book(Book("Ray Bradbury", "Fahrenheit 451"))
book_shelf2.append_book(Book("Cixin Liu", "The Three-Body Problem"))
book_shelf2.append_book(Book("Philip Kindred Dick", "Do Androids Dream of Electric Sheep?"))

for book in book_shelf2:
    book.print_title()