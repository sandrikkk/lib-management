import csv


def save_books_and_write_in_csv(self):
    if not self.books:
        return

    fieldnames = ["Title", "Author", "ISBN", "Genre"]
    filepath = "/home/user/Desktop/Library managment System/csv_file/books.csv"

    with open(filepath, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for book in self.books:
            writer.writerow({
                "Title": book.title,
                "Author": book.author,
                "ISBN": book.isbn,
                "Genre": book.genre
            })
