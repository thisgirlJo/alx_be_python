class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def __str__(self):
        print(f"Book: {self.title} by {self.author}")

class EBook(Book):
    def __init__(self, title, author, file_size: int):
        self.file_size = file_size
        super().__init__(title, author)
    
    def __str__(self):
        return super().__str__()
        print(f"EBOOK: {self.title} by {self.author}, File Size: {self.file_size}")

class PrintBook(Book):
    def __init__(self, title, author, page_count: int):
        self.page_count = page_count
        super().__init__(title, author)
    
    def __str__(self):
        return super().__str__()
        print(f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}")

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        if EBook:
            return f"EBOOK: {self.title} by {self.author}, File Size: {self.file_size}"
        elif PrintBook:
            return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"
        else:
            return f"Book: {self.title} by {self.author}"