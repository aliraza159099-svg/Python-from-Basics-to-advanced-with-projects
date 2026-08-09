from Library import BookMethods
from models import Book

num = 1
while num!=0:
    print("1. Add Book : ")
    print("2. Remove Book : ")
    print("3. Search Book : ")
    print("4. Add Member : ")
    print("5. Remove Memd tober : ")
    num = int(input("Enter your choice : "))
    if num == 1:
        name = input("Enter Book's name : ")
        author = input("Enter Author's name : ")
        isbn = int(input("Enter the isbn no : "))
        b = Book(name,author,isbn)
        BookMethods.addBook(,b)

        

    elif num == 2:
        name = input("Enter the name of the book : ")
       

    elif num == 3:
         name = input("Enter the name of the book : ")
         

    elif num == 4:
         name = input("Enter the member's name : ")
     

    elif num == 5:
            name = input("Enter the name of the Author : ")