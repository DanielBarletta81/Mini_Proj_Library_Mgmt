# main
""" 


1. Create an improved, user-friendly command-line interface (CLI) for the Library Management
 System with separate menus for each class of the system.

    Welcome to the Library Management System! """

#    Main Menu:
#    1. Book Operations
 #   2. User Operations
  #  3. Author Operations
 #   4. Genre Operations
#    5. Quit

def main_menu():


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
            #book_operations_menu()
            pass
       
       elif choice == 2:
            #user_operations_menu()
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