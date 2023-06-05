from base.base import BaseModel


class Book(BaseModel):
    filename = "books.csv"
    fieldnames = ["id", "title", "author", "isbn", "genre", "available"]

    def __init__(self, title, author, isbn, genre, available=True, id=None):  # noqa
        super().__init__(id)
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.available = available

    def __repr__(self):
        return f"UUID: {self.id}, Title: {self.title}, Author: {self.author}, " \
               f"ISBN: {self.isbn}, Genre: {self.genre}, Available: {self.available}"

    def get_attr_dict(self):
        attrs = {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "genre": self.genre,
            "available": self.available
        }

        return attrs

    @classmethod
    def get_search_criteria(cls):
        return ["title", "author", "isbn", "genre"]

    # def remove_books(self):
    #     if not self.books:
    #         print("There are not any books in library !")
    #     self.books.remove(self)
    #     csv_handler.remove_book(self)
    #     print("Book has been deleted successfully !")
    #
    # @classmethod
    # def books_list(cls):
    #     print("Book list was accessed !")
    #     if cls.books:
    #         for book in cls.books:
    #             print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}, Genre: {book.genre}")
    #
    #     else:
    #         print("There are not any books in the library !")
    #
    # def update_book(self, title=None, author=None, isbn=None, genre=None):
    #     if not self.books:
    #         print("There are no books in the library!")
    #         return
    #
    #     for book in self.books:
    #         if book.id == self.id:
    #             if title:
    #                 book.title = title
    #             if author:
    #                 book.author = author
    #             if isbn:
    #                 book.isbn = isbn
    #             if genre:
    #                 book.genre = genre
    #             break
    #     csv_handler.save_book(self)
    #
    # @classmethod
    # def search_book(cls, book_value, book_search):
    #     search_list_books = []
    #
    #     for book in cls.books:
    #         if book_value == 'title' and book_search in book.title:
    #             search_list_books.append(book)
    #         if book_value == 'author' and book_search in book.author:
    #             search_list_books.append(book)
    #         if book_value == 'isbn' and book_search in book.isbn:
    #             search_list_books.append(book)
    #         if book_value == 'genre' and book_search in book.genre:
    #             search_list_books.append(book)
    #
    #     if search_list_books:
    #         return search_list_books
    #     else:
    #         return "Not found any books or parameters are invalid!"
