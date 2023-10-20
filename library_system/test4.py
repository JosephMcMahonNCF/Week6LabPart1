import tkinter as tk
from tkinter import messagebox, simpledialog
from borrow_book import verify


library_books = []
library_members = []



def add_book():
    """Capture details and add a book to the library."""
    title = simpledialog.askstring("Input", "Enter the book's title:")
    if title:
        author = simpledialog.askstring("Input", "Enter the book's author:", initialvalue="")
        if author:
            library_books.append({"Title": title, "Author": author, "Availability": True})
            messagebox.showinfo("Success", "Book added successfully!")
        else:
            messagebox.showwarning("Warning", "Book addition cancelled. Author was not provided.")
    else:
        messagebox.showwarning("Warning", "Book addition cancelled. Title was not provided.")

def register_member():
    """Adds a member to library_members."""

    name = simpledialog.askstring("Input", "Enter the member's name here:")
    if name:
        library_members.append(name)
        messagebox.showinfo("Success", f"{name} added successfully!")
    else:
        messagebox.showwarning("Warning", "Member registration cancelled. Member name was not provided.")




def borrow_book():
    member_name = simpledialog.askstring("Input", "Enter the member's name:")
    if member_name:
        member_verification = verify(member_name)
        if member_verification:
            book_title = simpledialog.askstring("Input", "Enter the book's title:")
            if book_title:
                book_verification = verify(book_title, "title")
                if book_verification:
                    for book in library_books:
                        if book['Title'] == book_title:
                            if not book['Availability']:
                                messagebox.showinfo("Failure", f"{book_title} has already been checked out.")
                            else:
                                book['Availability'] = False
                                messagebox.showinfo("Success", f"{book_title} borrowed by {member_name} successfully!")
                else:
                    messagebox.showwarning("Warning", f"Borrowing book cancelled. {book_title} not found.")
            else:
                messagebox.showwarning("Warning", "Borrowing book cancelled. Book title was not provided.")
        else:
            messagebox.showwarning("Warning", f"Borrowing book cancelled. {member_name} not found.")
    else:
        messagebox.showwarning("Warning", "Borrowing book cancelled. Member name was not provided.")




def display_books():
    print(library_books)

def display_members():
    print(library_members)

def exit_app():
    root.destroy()


root = tk.Tk()
root.title("Library Management System")


add_book_btn = tk.Button(root, text="Add a new book", command=add_book)
add_book_btn.pack(padx=10, pady=10)

register_member_btn = tk.Button(root, text="Register a new member", command=register_member)
register_member_btn.pack(pady=10)

borrow_book_btn = tk.Button(root, text="Borrow a book", command=borrow_book)
borrow_book_btn.pack(pady=10)

display_books_btn = tk.Button(root, text="Display all books", command=display_books)
display_books_btn.pack(pady=10)

display_members_btn = tk.Button(root, text="Display all members", command=display_members)
display_members_btn.pack(pady=10)

exit_btn = tk.Button(root, text="Exit", command=exit_app)
exit_btn.pack(pady=10)



root.mainloop()


