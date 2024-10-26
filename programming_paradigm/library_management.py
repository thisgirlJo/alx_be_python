# Implementing Basic OOP for a Library Management System

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False
    def check_out(self):
        if  not self._is_checked_out:
            return True
        else:
            return False
class Library(Book):
    def __init__(self):
        #@classmethod
        #super.__init__(title, author)
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    self._book.remove(book)

    def return_book(self, title):
        pass
    def list_available_books(self):
        #print(f"{self.title} by {self.author}")
        pass