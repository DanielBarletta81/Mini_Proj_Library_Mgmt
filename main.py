# main
from books import book_ops_menu


def main_menu():
  #  library = {}
 

    while True:
     
       print("***  Welcome to the Library Management System! ***")
       print("\n Menu:")
       print("\n 1. Book Operations")
       print("\n 2. User Operations")
       print("\n 3. Author Operations")
       print("\n 4. Genre Operations")
       print("\n 5. Quit")

       choice = int(input("Please choose an option (1-5): "))

       if choice == 5:
              break
       
       elif choice == 1:
            book_ops_menu()
            
       
       elif choice == 2:
            #user_ops_menu()
            pass
       
       elif choice == 3:
            #author_operations_menu()
            pass
       
       elif choice == 4:
            #genre_operations_menu()
            pass
       
       else:
              print("Invalid selection, please try again.")
            

main_menu()