import datetime


class Transaction:
    def __init__(self, borrower, book):
        self.borrower = borrower
        self.book = book
        self.borrow_date = datetime.date.today()
        self.deadline = 14

    def __repr__(self):
        return f"Borrower: {self.borrower.name}, Book: {self.book.title}, Borrow Date: {self.borrow_date}"

    def is_overdue(self):
        today = datetime.date.today()
        return (today - self.borrow_date).days > self.deadline
