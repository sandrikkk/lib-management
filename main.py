from books_management.books import Book
from borrower_managment.borower import Borrower
from transaction_managment.transaction import Transaction
from base.base import BaseModel

# # Add new books
# book1 = Book(title="Title1", author="Author1", isbn="ISBN1", genre="Genre1")
# book1.save()
book2 = Book(title="Title2", author="Author2", isbn="ISBN2", genre="Genre2")
book2.save()
Book.update('cd29d9be-266a-4547-aeb5-3ebb300f4ee9', {'title': 'new title', 'author': 'New Author'})

Book.remove('c63a686a-2904-4a56-a6e5-d7ab13ca48fd')
# Search for books with a specific title and genre
criteria = {"title": "Title1", "author": "Author1"}
results = Book.search(criteria)

for book in results:
    print(book)

# book1.add_books()
# # # #
# # #
# book2 = Book("Title2", "Author2", "ISBN2", "Genre2")
# book2.add_books()
#
# book3 = Book("Title3", "Author3", "ISBN3", "Genre3")
# book3.add_books()
#
# # print(Book.books)
# book5 = Book("Title334", "Author33", "ISBN331", "Genre31")
# book5.add_books()


#
# Update book details
# book1.update_book(title="New Title")

# # print(my_library.books)
#
# # Remove a book
#
# book1.books_list()
#
# # Search a book
# search_results = Book.search_book("author", "Author3")
# print(*search_results)
#
# borrower1 = Borrower("Sandro", "Iashvili", "555555555", "Temqa", "010190724141")
# borrower2 = Borrower("oto", "Iashvili", "555455555", "Temqa", "010190724145")
# borrower1.save()
# borrower2.save()
#
# criteria = {"name": "Sandro", "last_name": "Iashvili"}
# br_results = Borrower.search(criteria)
#
# for result in br_results:
#     print(result)
# Borrower.remove("927adb9e-2ea7-4ebf-bc87-a928dee12969")
#
# Book.update('9532e7eb-caad-424c-9c75-b048686832d0', {'Title': 'New Title', 'Author': 'New Author'})
# Borrower.update("bff84464-f857-4475-9167-c2165a3ddc1c", {'name': 'saa324234234234234sd'})

#
# borrower1.update_borrower_details(name="sandro")
# Borrower.borrower_list()
# search_results1 = Borrower.search_borrowers("personal_number", "010190724141")
#
# print(search_results1)
#
# #
# # search_results1 = my_library.search_borrowers("personal_number", "010190724141")
# # print(search_results1)
# transaction1 = Transaction()
# print(transaction1)
# ,
# transaction1 = Transaction(borrower1, book1)
# transaction1.save()
# transaction2 = Transaction(borrower2, book1)
# transaction2.save()

# Transaction.remove("8b6a2d53-962b-4cf0-a906-e44a40bfe780")


#
# transaction1.remove_transaction()
#
# Transaction.transaction_history()
# print(transaction1)
#
# # transaction2 = my_library.add_transaction(borrower2, book2)
