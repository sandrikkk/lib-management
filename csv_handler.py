import csv


def save_books_and_write_in_csv(self):
    if not self.books:
        return

    fieldnames = ["Title", "Author", "ISBN", "Genre"]
    book_filepath = "/home/user/Desktop/lib-management/csv_file/books.csv"

    with open(book_filepath, mode="w", newline="") as file:
        book_writer = csv.DictWriter(file, fieldnames=fieldnames)
        book_writer.writeheader()

        for book in self.books:
            book_writer.writerow({
                "Title": book.title,
                "Author": book.author,
                "ISBN": book.isbn,
                "Genre": book.genre
            })


def remove_book_from_csv(rmbook):
    rows = []
    with open('/home/user/Desktop/lib-management/csv_file/books.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if row[0] != rmbook.title:
                rows.append(row)
    with open('/home/user/Desktop/lib-management/csv_file/books.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(rows)


def save_borrowers_and_write_in_csv(self):
    if not self.borrowers:
        return

    fieldnames = ["name", "last_name", "phone", "address", "personal_number"]
    book_filepath = "/home/user/Desktop/lib-management/csv_file/borrowers.csv"

    with open(book_filepath, mode="w", newline="") as file:
        borrower_writer= csv.DictWriter(file, fieldnames=fieldnames)
        borrower_writer.writeheader()

        for borrower in self.borrowers:
            borrower_writer.writerow({
                "name": borrower.name,
                "last_name": borrower.last_name,
                "phone": borrower.phone,
                "address": borrower.address,
                "personal_number": borrower.personal_number
            })
