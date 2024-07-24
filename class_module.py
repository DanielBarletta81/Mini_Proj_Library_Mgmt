# Create a class hierarchy

class Genre:
    def __init__(self, genre, description, category):
        self.genre = genre
        self.description = description
        self.category = category

    def add_new_genre(self):
        pass    

    def view_genre(self):
        pass   

    def display_all_genres(self):
        pass  

#Menu Actions:

#- Adding a new book with all relevant details.

#- Allowing users to borrow a book, marking it as "Borrowed."

#- Allowing users to return a book, marking it as "Available."

#- Searching for a book by its unique identifier (ISBN or title) and displaying its details.

#- Displaying a list of all books with their unique identifiers.
 

# Inheritance: Book inherits Genre class methods to assign books to genres
class Book(Genre):
    def __init__(self, title, author, isbn, published_date):
        super().__init__(self)
        self.title = title
        self.author = author
        self.isbn = isbn
        self.published_date = published_date
        self.is_available = True

    def add_book(self):
        pass

    def borrow_book(self):
        pass

    def return_book(self):
        self.is_available = True

    def book_search(self):
        pass

    def display_books(self):
        pass

class Author:
    def __init__(self, name, biography):
        self.name = name
        self.biography = biography

    def add_new_author(self):
        pass    

    def view_author(self):
        pass   

    def display_all_authors(self):
        pass   





    