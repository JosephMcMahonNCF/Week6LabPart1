import tkinter as tk
from tkinter import messagebox, simpledialog
import main
import members
import books


def register_member():
    """Adds a member to library_members."""
    messagebox.showinfo("Info", "Register member functionality here")


def borrow_book(title):
    """Changes the availability of a book to False."""
    borrow_book(title)
    messagebox.showinfo("Info", "Borrow book functionality here")


def return_book(title):
    """Changes the availability of a book to True."""
    return_book(title)
    messagebox.showinfo("Info", "Return book functionality here")


def display_books():
    print(library_books)
    messagebox.showinfo("Info", "Display books functionality here")


def display_members():
    print(library_members)
    messagebox.showinfo("Info", "Display members functionality here")


def add_book():
    """Capture details and add a book to the library."""
    title = simpledialog.askstring("Input", "Enter the book's title:")
    if title:  # Check if the user provided a title (didn't press cancel)
        author = simpledialog.askstring("Input", "Enter the book's author:")
        if author:  # Check if the user provided an author
            add_book(title, author)  # Using the function from books.py
            messagebox.showinfo("Success", "Book added successfully!")
        else:
            messagebox.showwarning("Warning", "Book addition cancelled. Author was not provided.")
    else:
        messagebox.showwarning("Warning", "Book addition cancelled. Title was not provided.")


root = tk.Tk()
root.title("Library Management System")

# Menu buttons
add_book_btn = tk.Button(root, text="Add a new book", command=add_book)
add_book_btn.pack(pady=10)

register_member_btn = tk.Button(root, text="Register a new member", command=register_member)
register_member_btn.pack(pady=10)

borrow_book_btn = tk.Button(root, text="Borrow a book", command=borrow_book)
borrow_book_btn.pack(pady=10)

return_book_btn = tk.Button(root, text="Return a book", command=return_book)
return_book_btn.pack(pady=10)

display_books_btn = tk.Button(root, text="Display all books", command=display_books)
display_books_btn.pack(pady=10)

display_members_btn = tk.Button(root, text="Display all members", command=display_members)
display_members_btn.pack(pady=10)

root.mainloop()