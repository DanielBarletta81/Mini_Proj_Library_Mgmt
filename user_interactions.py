# user interactions module
from main import main_menu # to go back to main menu from User menu
class User:
    def __init__(self, name, library_id, branch):
        self.__name = name
        self.branch = branch
        self.__library_id = library_id
        self.users_list = {}
        
       

#encapsulation - getters and setters for private user attributes
    def get_user_name(self):
        return self.__name

    def set_user_name(self, new_name):
        self.__name = new_name    

    def get_user_id(self):
        return self.__library_id

    def set_user_id(self, new_library_id):
        self.__library_id = new_library_id   
        
    
    def add_new_user(self):
        name = input("Enter name: ")
        library_id = input("Enter new library id: ")
        branch = input("Enter the branch: ")
        self.users_list[name] = User(name, library_id, branch)  

    def view_user_details(self):
        name = input("Enter users name: ")
        if name not in self.users_list:
            print(f'User {name} not found.')
            return   
        for item in self.users_list: #######################################
         print(f'{name} +++ {item}')   

    def display_all_users(self):
        print(f'{self.users_list}')   
    

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
            add_new_user()
       
       elif choice == 2:
            view_user_details()
       
       elif choice == 3:
            display_all_users()
       
       else:
              print("Invalid selection, please try again.")
