from library import Library
from books import Book
from borrower_managment.borower_managment import Borrower

my_library = Library()
# Add new books
book1 = Book("Title1", "Author1", "ISBN1", "Genre1")
my_library.add_books(book1)

book2 = Book("Title2", "Author2", "ISBN2", "Genre2")
my_library.add_books(book2)

book3 = Book("Title3", "Author3", "ISBN3", "Genre3")
my_library.add_books(book3)

# Update book details
my_library.update_book(bk=book2, title="New Title")

print(my_library.books)

# Remove a book
my_library.remove_books(book1)
my_library.remove_books(book2)


# Search a book
search_results = my_library.search_book("author", "Author1")
print(*search_results)

borrower1 = Borrower("Sandro", "Iashvili", "555555555", "Temqa", "010190724141")
my_library.add_borrowers(borrower1)
my_library.borrower_list()
my_library.update_borrower_details(borrower1, name="Sandro")
my_library.borrower_list()

search_results1 = my_library.search_borrowers("personal_number", "010190724141")
print(*search_results1)
my_library.remove_borrowers(borrower1)

