# user interactions module
from main import main_menu
class User:
    def __init__(self, name, library_id, branch):
        self.__name = name
        self.branch = branch
        self.__library_id = library_id
        self.__books_loaned = []
       

#encapsulation - getters and setters for private user attributes
    def get_user_name(self):
        return self.__name

    def set_user_name(self, new_name):
        self.__name = new_name    

    def get_user_id(self):
        return self.__library_id

    def set_user_id(self, new_library_id):
        self.__library_id = new_library_id   
        
    def get_user_books(self):
        return self.__books_loaned
    
"""  def set_user_books(self):
        self.__books_loaned """
    
def add_new_user(users):
    name = input("Enter name: ")
    library_id = input("Enter new library id: ")
    branch = input("Enter the branch: ")
    users[name] = User(name, library_id, branch)  

def view_user_details(users):
    name = input("Enter users name: ")   
    for item in users: #######################################
         print(f'{name} +++ {item}')   

def display_all_users(users):
        print(f'{users}')   

def user_ops_menu():
     users = {}

     while True:
     
       print("***  Welcome to the User Operations Menu! ***")
       print("\n Menu:")
       print("\n 1. Add a new user")
       print("\n 2. View user details")
       print("\n 3. Display all users")
       print("\n 4. Back to Main Menu")

       choice = int(input("Please choose an option (1-4): "))

       if choice == 4:
            main_menu()
       
       elif choice == 1:
            add_new_user(users)
       
       elif choice == 2:
            view_user_details(users)
       
       elif choice == 3:
            display_all_users(users)
       
       else:
              print("Invalid selection, please try again.")
