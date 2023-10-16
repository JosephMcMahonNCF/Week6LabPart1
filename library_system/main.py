from books import add_book, borrow_book, return_book, display_books
from members import register_member, display_members

library_books = []
library_members = []


def display_menu():
    print("\nLibrary Management System")
    print("----------------------------")
    print("1. Add a new book to the library.")
    print("2. Register a new library member.")
    print("3. Borrow a book.")
    print("4. Return a book.")
    print("5. Display all books.")
    print("6. Display all members.")
    print("7. Exit.")
    print("----------------------------")


def main():
    while True:
        display_menu()

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            # Call function to add a new book
            add_book(input("Enter the name of the book: ",), input("Enter the Author of the book: "))
        elif choice == "2":
            # Call function to register a new member
            register_member(input("Enter your name: "))
        elif choice == "3":
            # Call function to borrow a book
            borrow_book(input("Enter the name of the book you would like to borrow: "))
        elif choice == "4":
            # Call function to return a book
            return_book(input("Enter the name of the book you would like to return: "))
        elif choice == "5":
            # Call function to display all books
            display_books()
        elif choice == "6":
            # Call function to display all members
            display_members()
        elif choice == "7":
            print("Thank you for using the Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")


if __name__ == "__main__":
    main()
