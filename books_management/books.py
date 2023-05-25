class Book:
    def __init__(self, title, author, isbn, genre):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre

    def __repr__(self):
        return f"Title:{self.title}, Author:{self.author}, isbn:{self.isbn}, Genre:{self.genre}"
