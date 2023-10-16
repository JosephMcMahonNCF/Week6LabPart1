library_members = [] # stores dictionaries of member info

def register_member(name):
    """Adds a member to library_members."""

    library_members.append({"Name": name, "Borrowed books": "none"})

register_member("Joey")




def find_member(name):
    """Checks if a member is registered."""
    for member in library_members:
        if member['Name'] == name:
            return member.items()


print(find_member("Joey"))



#Extra shit that does not work
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

    if not book_found:
        print("This library does not carry " + title)
        return

    if available:
        borrow_book(title)
        log_name(title, name)
    else:
        print(title + " is not available at this time.")
        return

    print("Book successfully checked out")