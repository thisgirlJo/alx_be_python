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
        self._books = []
        self._return = []

    def add_book(self, book):
        self._books.append(book)
        self._return.append(book)
        #print(f"{self._books[0].author}")
        #print(f"{self._books[0].title}: added successfully")

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    self._books.remove(book)

    def list_available_books(self):
        for book in self._books:
            print(f"{book.title} by {book.author}")
        #return f"{} by {self._books.author}"

    def return_book(self, title):
        for book in self._return:
            if book.title == title:
                self._books.append(book)