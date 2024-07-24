from genres import Genre
from main import main_menu
# Inheritance: Book inherits Genre class methods to assign books to genres
class Book(Genre):
    def __init__(self, title, author, isbn, published_date):
        super().__init__(self)
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__published_date = published_date
        self.__is_available = True
        self.__books_list = {}
       
        

    def get_title(self):
        return self.__title
        

    def borrow_book(self):
        if self.__is_available:
            self.__is_available = False
            return True
        return False

    def return_book(self, isbn):
        if isbn not in self.__books_list:
            self.is_available = True
            print(f'Book {self.__isbn} ia now available.')

    def book_search(self, book_id):
        if book_id in self.__books_list:
            print(f'Results for search {book_id} \nTitle: {self.__title}\n Author: {self.__author}\n ISBN: {self.isbn}\n Date Published: {self.published_date}')

    def assign_genre(self, assigned_genre):
        pass

    def display_books(self):
        for book in self.__books_list:
            print(f'Full book list: {book}Title: {self.__title}\n Author: {self.__author}\n ISBN: {self.isbn}\n Date Published: {self.published_date}')



    def add_book(self, title, author, isbn, published_date):
        if title in self.__books_list:
            print(f'Error. {title} is already on list.')
            return
        else:
            self.__books_list[title] = Book(title, author, isbn, published_date)
        print(f'{title} by {author} has been added to list.')


    while True:
     
       print("***  Welcome to the Book Operations Menu! ***")
       print("\n Menu:")
       print("\n 1. Add a book")
       print("\n 2. Find a book")
       print("\n 3. Display all books")
       print("\n 4. Back to Main Menu")

       choice = int(input("Please choose an option (1-4): "))

       if choice == 4:
               main_menu()
       
       elif choice == 1:
            add_book()
       
       elif choice == 2:
            book_search()
       
       elif choice == 3:
            display_books()
       
       else:
              print("Invalid selection, please try again.")


#Menu Actions:



#- Allowing users to borrow a book, marking it as "Borrowed."

#- Allowing users to return a book, marking it as "Available."

#- Searching for a book by its unique identifier (ISBN or title) and displaying its details.

#- Displaying a list of all books with their unique identifiers.



