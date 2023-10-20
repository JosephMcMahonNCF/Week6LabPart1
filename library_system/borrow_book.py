import tkinter as tk
from tkinter import messagebox, simpledialog


library_books = []
library_members = []

def register_members(name):
    """Adds a member to library_members."""
    library_members.append(name)

def add_books(title, author):
    """Adds a book to library_books"""
    library_books.append({"Title": title, "Author": author, "Availability": True})



def display_books():
    print(library_books)

def verify(input, type = "name"):
    if type == "name":
        name = input
        if name in library_members:
            return True
        else:
            member_verification = False
            return member_verification
    elif type == "title":
        title = input
        for book in library_books:
            if title == book["Title"]:
                book_verification = True
                return book_verification
        book_verification = False
        return book_verification



# print(verify("Joey"))
# print(verify("test", "title"))
# print(verify("test2", "title"))










def borrow_book(name, title):
    if name:
        verification = verify(name)
        if verification:
            if title:
                verification = verify(title, "title")
                if verification:
                    for book in library_books:
                        if book['Title'] == title:
                            book['Availability'] = False
                            print(f"{title} borrowed by {name} successfully!")
                            return


# display_books()



