from library import Library
from books import Book

my_library = Library()
# Add new books
book1 = Book("Title1", "Author1", "ISBN1", "Genre1")
my_library.add_books(book1)

book2 = Book("Title2", "Author2", "ISBN2", "Genre2")
my_library.add_books(book2)

# Update book details
my_library.update_book(bk=book2, title="New Title")

print(my_library.books)

# Remove a book
my_library.remove_books(book2)

# Search a book
search_results = my_library.search_book("author", "Author1")
print(*search_results)
