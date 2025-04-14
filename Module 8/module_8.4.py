# Name: Miguel Angelo B. Basinillo
# Section: BSIT 2A
# MODULE 8.4 - Formative Test
# Create a class Book with attributes title and author. Define another class Library that holds a list of Book objects. Implement methods to add a book to the library and display all books in the library.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        for book in self.books:
            print(f"{book.title} by {book.author}")

library = Library()

book1 = Book("Python Programming", "John Smith")
book2 = Book("Data Science Essentials", "Jane Doe")

library.add_book(book1)
library.add_book(book2)

library.display_books()