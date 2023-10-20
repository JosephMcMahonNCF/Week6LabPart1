# library_ui.py

import tkinter as tk
from tkinter import messagebox, simpledialog
import main  # Assuming main.py contains the functions for the library operations
import members
import books

# Define the missing functions

def register_member():
    member_name = simpledialog.askstring("Input", "Enter the member's name:")
    if member_name:
        members.register_member(member_name)
        messagebox.showinfo("Success", "Member registered successfully!")
    else:
        messagebox.showwarning("Warning", "Member registration cancelled. Name was not provided.")

def borrow_book():
    book = simpledialog.askstring("Input", "Enter the title of the book:")
    if book:
        success = borrow_book(book)
        if success:
            messagebox.showinfo("Success", f"{book} borrowed registered successfully!")



def return_book():
    member_name = simpledialog.askstring("Input", "Enter the member's name:")
    if member_name:
        book_title = simpledialog.askstring("Input", "Enter the book's title:")
        if book_title:
            success = main.return_book(member_name, book_title)
            if success:
                messagebox.showinfo("Success", f"{book_title} returned by {member_name} successfully!")
            else:
                messagebox.showwarning("Warning", f"Returning {book_title} by {member_name} failed.")
        else:
            messagebox.showwarning("Warning", "Returning book cancelled. Title was not provided.")
    else:
        messagebox.showwarning("Warning", "Returning book cancelled. Member name was not provided.")

def display_books():
    all_books = books.get_all_books()
    if all_books:
        book_list = "\n".join(all_books)
        messagebox.showinfo("All Books", book_list)
    else:
        messagebox.showinfo("Info", "No books available in the library.")

def display_members():
    all_members = members.get_all_members()
    if all_members:
        member_list = "\n".join(all_members)
        messagebox.showinfo("All Members", member_list)
    else:
        messagebox.showinfo("Info", "No members registered in the library.")

def add_book():
    title = simpledialog.askstring("Input", "Enter the book's title:")
    if title:
        author = simpledialog.askstring("Input", "Enter the book's author:")
        if author:
            books.add_book(title, author)
            messagebox.showinfo("Success", "Book added successfully!")
        else:
            messagebox.showwarning("Warning", "Book addition cancelled. Author was not provided.")
    else:
        messagebox.showwarning("Warning", "Book addition cancelled. Title was not provided.")

def exit_app():
    root.destroy()

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

exit_btn = tk.Button(root, text="Exit", command=exit_app)
exit_btn.pack(pady=10)

root.mainloop()
