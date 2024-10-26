class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def __str__(self):
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title, author, file_size: int):
        super().__init__(title, author)
        self.file_size = file_size
    
    def __str__(self):
        super().__repr__()
        return f"EBOOK: {self.title} by {self.author}, File Size: {self.file_size}"


class PrintBook(Book):
    def __init__(self, title, author, page_count: int):
        super().__init__(title, author)
        self.page_count = page_count
    
    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

class Library(Book):
    def __init__(self):
        self.books = [] #Create an empty List

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for x in self.books:
            print(x)