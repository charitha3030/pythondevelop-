#Library Management System
class Book:
    def __init__(self, book_id, title, author, publication_year):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.is_available = True

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_available_books(self):
        available_books = [book for book in self.books if book.is_available]
        if available_books:
            print("Available Books:")
            for book in available_books:
                print(f"Book ID: {book.book_id}, Title: {book.title}, Author: {book.author}, Publication Year: {book.publication_year}")
        else:
            print("No available books in the library.")

    def borrow_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if book.is_available:
                    book.is_available = False
                    print("Book borrowed successfully.")
                else:
                    print("Book is not available for borrowing.")
                return
        print("Book not found in the library.")

    def return_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if not book.is_available:
                    book.is_available = True
                    print("Book returned successfully.")
                else:
                    print("This book is already available in the library.")
                return
        print("Book not found in the library.")

# Example usage
library = Library()

# Adding books to the library
book1 = Book("100", "Book 1", "Author 1", 2002)
book2 = Book("101", "Book 2", "Author 2", 2005)
book3 = Book("102", "Book 3", "Author 3", 2010)
book4 = Book("103", "Book 4", "Author 4", 2014)
book5 = Book("104", "Book 5", "Author 5", 2019)
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)
library.add_book(book5)

# Displaying available books
library.display_available_books()

# Borrowing a book
book_id = input("Enter the book ID to borrow: ")
library.borrow_book(book_id)

# Returning a book
book_id = input("Enter the book ID to return: ")
library.return_book(book_id)

# Displaying available books after borrowing and returning
library.display_available_books()
