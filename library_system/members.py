library_members = [] #stores names of members

def register_member(name):
    """Adds a member to library_members."""

    library_members.append(name)

register_member("Joey")

# print(library_members)


def find_member(name):
    """Checks if a member is registered."""

    return name in library_members


# print(find_member("Joey"))

def display_members():
    print(library_members)