class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully")

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print("Book removed successfully")
        else:
            print("Book not found")


library = Library()

library.add_book("Python Programming")
library.add_book("C++ Programming")

print(library.books)

library.remove_book("Python Programming")

print(library.books)