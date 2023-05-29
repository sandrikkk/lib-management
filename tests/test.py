from unittest import TestCase
from books_management.library import Library
from books_management.books import Book
from borrower_managment.borower import Borrower


class BookTest(TestCase):
    def test_getting_borrowersbook(self):
        borrower1 = Borrower("Sandro", "Iashvili", "555555555", "Temqa", "010190724141")
        borrower2 = Borrower("oto", "Iashvili", "555455555", "Temqa", "010190724145")

        my_library = Library()

        my_library.add_borrowers(borrower2)

        my_library.add_borrowers(borrower1)

        my_library.borrower_list()

