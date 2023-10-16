library_books = []   #stores dictionaries

def question_seperatior(question):
    print("~~~~~~~~~~~~~~~~~")
    print(question)
    print("~~~~~~~~~~~~~~~~~")


def add_book(title, author):
    """Adds a book to library_books"""
    library_books.append({"Title": title, "Author": author, "Availability": True})

add_book("War and Peace", "Tolstoy")
add_book("Crime and Punishment", "Dostoevsky")

#
# question_seperatior("add book")
#
# print(library_books)

def borrow_book(title):
    """Changes the availability of a book to False."""

    for book in library_books:
        if book['Title'] == title:
            book['Availability'] = False
            return
    return

borrow_book("War and Peace")
#
# question_seperatior("borrow book")
#
# print(library_books)


def return_book(title):
    """Changes the availability of a book to True."""

    for book in library_books:
        if book['Title'] == title:
            book['Availability'] = True
            return
    return

return_book("War and Peace")
#
# question_seperatior("return book")
#
# print(library_books)
#



def find_book(title):
    """Returns the book's details if found."""
    for book in library_books:
        if book['Title'] == title:
            return book.items()
#
# question_seperatior("find book")
#
# print(find_book("War and Peace"))



def display_books():
    print(library_books)