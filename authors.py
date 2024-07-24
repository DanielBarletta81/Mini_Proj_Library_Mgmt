
from main import main_menu

class Author:
    def __init__(self, name, biography):
        self.name = name
        self.biography = biography
        self.authors_list = {}

    def add_new_author(self, name, author):
        name = input("Enter Author's name to add: ")
        biography = input("Add some author highlights: ")
        if author in self.authors_list:
             print(f'Author: {author} already added to list.') 
             return
        self.authors_list[name]= Author(name, biography)

    def view_author(self, author):
         if author in self.authors_list:
              print(f'Details for {author}: Name: {self.name}\n Biography: {self.biography}')
           

    def display_all_authors(self):
        for author in self.authors_list:
             print(f'{author}')  

    while True:
     
       print("***  Welcome to the Author Operations Menu! ***")
       print("\n Menu:")
       print("\n 1. Add a new author")
       print("\n 2. View author details")
       print("\n 3. Display all authors")
       print("\n 4. Back to Main Menu")

       choice = int(input("Please choose an option (1-4): "))

       if choice == 4:
            break
       
       elif choice == 1:
            add_new_author()
       
       elif choice == 2:
            view_author()
       
       elif choice == 3:
            display_all_authors()
       
       else:
              print("Invalid selection, please try again.")
