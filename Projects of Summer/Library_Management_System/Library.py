from models import Book, Member


class BookMethods:
    def __init__(self):
        self.dic_book = {}

    def addBook(self, book):

        if book.isbn not in self.dic_book:
            self.dic_book.update({book.isbn: book})
            print("Book added successfully!")
        else:
            print(f"The book with {book.isbn} is already in the library")

    def removeBook(self, isbn):

        if isbn in self.dic_book:
            del self.dic_book[isbn]
            print("Book removed successfully!")
        else:
            print(f"The book with {isbn} is not in the library")

    def searchBook(self, name):

        found = False

        for isbn, book in self.dic_book.items():
            if book.title.lower() == name.lower():
                print("Book found!")
                print(f"Name: {book.title}")
                print(f"Author: {book.author}")
                print(f"ISBN: {book.isbn}")
                found = True

        if not found:
            print("Book not found")


class MemberMethods:
    def __init__(self):
        self.dic_member = {}

    def addMember(self, member):

        if member.id not in self.dic_member:
            self.dic_member.update({member.id: member})
            print(f"{member.name} is added successfully")
        else:
            print("This member is already in the library")

    def removeMember(self, id):

        if id in self.dic_member:
            del self.dic_member[id]
            print("Member removed successfully!")
        else:
            print("Member not found")
