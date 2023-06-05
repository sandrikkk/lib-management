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

