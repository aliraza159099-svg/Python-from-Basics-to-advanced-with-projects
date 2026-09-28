from Library import BookMethods, MemberMethods
from models import Book, Member


books = BookMethods()
members = MemberMethods()

num = 1

while num != 0:

    print("\n1. Add Book : ")
    print("2. Remove Book : ")
    print("3. Search Book : ")
    print("4. Add Member : ")
    print("5. Remove Member : ")
    print("0. Exit")

    num = int(input("Enter your choice : "))

    if num == 1:

        name = input("Enter Book's name : ")
        author = input("Enter Author's name : ")
        isbn = int(input("Enter the isbn no : "))

        b = Book(name, author, isbn)

        books.addBook(b)

    elif num == 2:

        isbn = int(input("Enter the isbn of the book : "))

        books.removeBook(isbn)

    elif num == 3:

        name = input("Enter the name of the book : ")

        books.searchBook(name)

    elif num == 4:

        name = input("Enter the member's name : ")
        id = int(input("Enter member's id : "))

        m = Member(name, id)

        members.addMember(m)

    elif num == 5:

        id = int(input("Enter the id of the member : "))

        members.removeMember(id)

    elif num == 0:

        print("Program ended")

    else:

        print("Invalid choice")
