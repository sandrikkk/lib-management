import csv


class Library:
    def __init__(self):
        self.books = []

    def add_books(self, book):
        self.books.append(book)
        Csv.save_books_and_write_in_csv(self)

    def remove_books(self, book):
        if not self.books:
            print("There are not any books in library !")

        if book in self.books:
            self.books.remove(book)
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
        Csv.save_books_and_write_in_csv(self)

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
