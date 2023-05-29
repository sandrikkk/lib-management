import csv_handler


class Library:
    def __init__(self):
        self.books = []
        self.borrowers = []

    def add_books(self, book):
        self.books.append(book)
        csv_handler.save_books_and_write_in_csv(self)

    def remove_books(self, book):
        if not self.books:
            print("There are not any books in library !")

        if book in self.books:
            self.books.remove(book)
            csv_handler.remove_book_from_csv(book)
            print("Book has been deleted successfully !")
        else:
            print("Book not found in the library.")

    def books_list(self):
        print("Book list was accessed !")
        if self.books:
            for book in self.books:
                print(f"Title: {book.title},"
                      f" Author: {book.author},"
                      f" ISBN: {book.isbn},"
                      f" Genre: {book.genre}")
        else:
            print("There are not any books in library !")

    def update_book(self, bk, title=None, author=None, isbn=None, genre=None):
        if not self.books:
            print("There are no books in the library!")
            return

        for book in self.books:
            if book == bk:
                if title:
                    book.title = title
                if author:
                    book.author = author
                if isbn:
                    book.isbn = isbn
                if genre:
                    book.genre = genre
                break
        csv_handler.save_books_and_write_in_csv(self)

    def search_book(self, book_value, book_search):
        search_list_books = []

        for book in self.books:
            if book_value == 'title' and book_search in book.title:
                search_list_books.append(book)
            if book_value == 'author' and book_search in book.author:
                search_list_books.append(book)
            if book_value == 'isbn' and book_search in book.isbn:
                search_list_books.append(book)
            if book_value == 'genre' and book_search in book.genre:
                search_list_books.append(book)

        if search_list_books:
            return search_list_books
        else:
            return "not found any books or parameters are invalid !"

    def add_borrowers(self, borrower):
        self.borrowers.append(borrower)
        csv_handler.save_books_and_write_in_csv(self)

    def remove_borrowers(self, borrower):
        if not self.borrowers:
            print("There are not book borrowers in library !")

        if borrower in self.borrowers:
            self.borrowers.remove(borrower)
            csv_handler.remove_book_from_csv(borrower)
            print("Book borrower has been deleted successfully !")
        else:
            print("Book borrower not found.")

    def borrower_list(self):
        print("Book list was accessed !")
        if self.borrowers:
            for borrower in self.borrowers:
                print(f"Name: {borrower.name},"
                      f"Last Name: {borrower.last_name}"
                      f"Personal Number: {borrower.personal_number}"
                      )

    def update_borrower_details(self, bk, name=None, last_name=None, address=None, number=None, personal_number=None):
        if not self.borrowers:
            print("There are no books borrowers in the library!")
            return

        for borrower in self.borrowers:
            if borrower == bk:
                if name:
                    borrower.name = name
                if last_name:
                    borrower.last_name = last_name
                if address:
                    borrower.address = address
                if number:
                    borrower.number = number
                if personal_number:
                    borrower.personal_number = personal_number
                break
        csv_handler.save_borrowers_and_write_in_csv(self)

    def search_borrowers(self, borrower_value, borrower_search):
        search_list_borrowers = []

        for borrower in self.borrowers:
            if borrower_value == 'personal_number' and borrower_search in borrower.personal_number:
                search_list_borrowers.append(borrower)

            else:
                print("Personal number not found or trying to search other fields.")
