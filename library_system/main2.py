# main.py
from books import add_book, borrow_book, return_book
from members import register_member, find_member

# Assuming you've already imported necessary functions from books.py and members.py
library_books = []   #stores dictionaries
library_members = [] #stores names of members


# Define a function to display all books
def display_books():
    if not library_books:
        print("There are no books in the library.")
    else:
        print("Books in the library:")
        for book in library_books:
            print(f"Title: {book['Title']}, Author: {book['Author']}, Availability: {'Available' if book['Availability'] else 'Not Available'}")

# Define a function to display all members
def display_members():
    if not library_members:
        print("There are no registered members.")
    else:
        print("Registered members:")
        for member in library_members:
            print(f"Name: {member['Name']}, Borrowed books: {', '.join(member['Borrowed books'])}")

# Add these function definitions before the main() function in your code.




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




title = "Dune"
author = "fred"
name = "Joe"

def mai(choice, title, author, name):
    if choice == 1:
        add_book(title, author)
    elif choice == 2:
        register_member(name)
    elif choice == 3:
        borrow_log(title, name)
    elif choice == 4:
        return_book(title)
    elif choice == 5:
        display_books()
    elif choice == 6:
        display_members()
    elif choice == 7:
        print("Thank you for using the Library Management System. Goodbye!")
    else:
        print("Invalid choice. Please enter a number between 1 and 7.")

def show():
    print("showtime")
    for i in range(len(library_members)):
        print(library_members[i])
    for i in range(len(library_books)):
        print(library_books[i])


for i in range(1, 5):
    print(i)
    mai(i, title, author, name)

show()





def main():
    while True:
        display_menu()

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            add_book(title, author)
        elif choice == "2":
            name = input("Enter member name: ")
            register_member(name)
        elif choice == "3":
            title = input("Enter book title: ")
            name = input("Enter member name: ")
            borrow_log(title, name)
        elif choice == "4":
            title = input("Enter book title: ")
            # Call function to return a book
            return_book(title)
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
