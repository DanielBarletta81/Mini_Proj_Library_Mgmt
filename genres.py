          # Create a class hierarchy


class Genre:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.genres = {}
       
       
    def display_genres(self):
        print(f'**** Should be all genres ****Genre {self.name}:\n Description: {self.description}')   

    def add_new_genre(self, name, description):
     self.genres[name] = Genre(name, description)

    def view_single_genre(self):
          print(f'Genre {self.name}:\n Description: {self.description}')  


    while True:
     
       print("***  Welcome to the Genre Operations Menu! ***")
       print("\n Menu:")
       print("\n 1. Add a new genre")
       print("\n 2. View genre details")
       print("\n 3. Display all genres")
       print("\n 4. Back to Main Menu")

       choice = int(input("Please choose an option (1-4): "))

       if choice == 4:
               break
       
       elif choice == 1:
            add_new_genre()
       
       elif choice == 2:
            view_single_genre()
       
       elif choice == 3:
            display_genres()
       
       else:
              print("Invalid selection, please try again.")



    