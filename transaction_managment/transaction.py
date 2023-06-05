import datetime
from base.base import BaseModel


class Transaction(BaseModel):
    filename = "transactions.csv"
    fieldnames = ["id", "borrower", "book"]

    def __init__(self, borrower, book, deadline=14, id=None):
        super().__init__(id)
        self.borrower = borrower
        self.book = book
        self.borrow_date = datetime.date.today()
        self.deadline = deadline

    def __repr__(self):
        return f"UUID:{self.id}, Borrower: {self.borrower.name}, Book: {self.book.title}, Borrow Date: {self.borrow_date}"

    def get_attr_dict(self):
        attrs = {
            'id': self.id,
            "borrower": self.borrower.personal_number,
            "book": self.book.id
        }

        return attrs

    @property
    def is_overdue(self):
        today = datetime.date.today()
        return (today - self.borrow_date).days > self.deadline

    @classmethod
    def get_search_criteria(cls):
        return ["borrower", "book"]

    # @classmethod
    # def add_transaction(cls, borrower, book):
    #     if book.available:
    #         transaction = Transaction(borrower, book)
    #         cls.transactions.append(transaction)
    #         book.available = False
    #         # csv_handler.save_transactions(cls)
    #         return transaction
    #     else:
    #         print("Book is not available or wrong parameters !")
    #
    # def remove_transaction(self):
    #     self.transactions.remove(self)
    #     csv_handler.remove_transaction_from_csv(self)
    #     print("Transaction has been removed successfully.")
    #
    # @classmethod
    # def transaction_history(cls):
    #     print("Transaction History:")
    #     for transaction in cls.transactions:
    #         print(transaction)
    #
    # def check_overdue_books(self):
    #     today = datetime.date.today()
    #     overdue_transactions = []
    #
    #     for transaction in self.transactions:
    #         if transaction.is_overdue:
    #             overdue_transactions.append(transaction)
    #
    #     if overdue_transactions:
    #         print("Overdue Books:")
    #         for transaction in overdue_transactions:
    #             print(f"Book: '{transaction.book.title}', Borrower: {transaction.borrower.name}")
    #     else:
    #         print("No overdue books found.")
