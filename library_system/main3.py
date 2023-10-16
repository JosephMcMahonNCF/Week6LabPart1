from books import add_book, borrow_book, return_book
from members2 import register_member

library_books = []   # Stores dictionaries
library_members = [] # Stores names of members

def log_name(title, name):
    name_found = False

    for member in library_members:
        if member['Name'] == name:
            name_found = True
            member["Borrowed books"] = title
    if not name_found:
        print(name + " not found. Please try again")
        return

def borrow_log(title, name):
    """Track who borrowed what book"""
    book_found = False
    available = False

    for book in library_books:
        if book['Title'] == title:
            book_found = True
            available = book.get('Availability')
            print(book_found)
            break
        break

    print(book_found)
    if not book_found:
        print("This library does not carry " + title)
        return

    if available:
        borrow_book(title)
        log_name(title, name)
    else:
        print(title + " is not available at this time.")
        return

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
    for i in range(len(library_members)):
        print(library_members[i])
    for i in range(len(library_books)):
        print(library_books[i])

# Define a sequence of choices
sequence = [
    (1, "Dune", "Fred", "Joe"),  # Add a new book
    (2, "Dune", "", "Joe"),     # Register a new member
    (3, "Dune", "Fred", "Joe"),  # Borrow a book
    (5, "", "", ""),             # Display all books
    (6, "", "", ""),             # Display all members
    (7, "", "", ""),             # Exit
]

for choice, title, author, name in sequence:
    mai(choice, title, author, name)
    show()
