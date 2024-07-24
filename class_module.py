# Create a class hierarchy

class Book:
    def __init__(self, title, author, isbn, published_date, is_available):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.published_date = published_date
        self.is_available = is_available

    def add_book(self):
        pass

    def borrow_book(self):
        pass

    def return_book(self):
        pass

    def book_search(self):
        pass

    def display_books(self):
        pass

class Author:
    def __init__(self, name, biography):
        self.name = name
        self.biography = biography

class Genre:
    def __init__(self, genre):
        self.genre = genre


class User:
    def __init__(self, name, library_id):
        self.name = name
        self.library_id = library_id
        self.borrowed_titles = []

        
        

    