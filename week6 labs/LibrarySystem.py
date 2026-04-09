class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True


class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def borrow_book(self, book, member):
        if book.available:
            book.available = False
            member.borrowed_books.append(book)
            print(f"{member.name} borrowed '{book.title}'")
        else:
            print(f"'{book.title}' is not available")

    def return_book(self, book, member):
        if book in member.borrowed_books:
            book.available = True
            member.borrowed_books.remove(book)
            print(f"{member.name} returned '{book.title}'")
        else:
            print(f"{member.name} did not borrow '{book.title}'")

    def display_books(self):
        print("\nLibrary Books:")
        for book in self.books:
            status = "Available" if book.available else "Borrowed"
            print(f"{book.title} by {book.author} - {status}")


# --- Testing the system ---

library = Library()

# Create books
book1 = Book("Harry Potter", "J.K. Rowling")
book2 = Book("The Hobbit", "J.R.R. Tolkien")

# Create member
member1 = Member("Sudip")

# Add to library
library.add_book(book1)
library.add_book(book2)
library.add_member(member1)

# Display books
library.display_books()

# Borrow a book
library.borrow_book(book1, member1)

# Display again
library.display_books()

# Return the book
# library.return_book(book1, member1)

# Final display
library.display_books()
