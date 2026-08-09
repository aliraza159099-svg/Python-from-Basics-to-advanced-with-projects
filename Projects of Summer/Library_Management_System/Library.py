from models import Book


class BookMethods:
    def __init__(self):
         self.dic_book = {}
    def addBook(self,isbn):
        
        if isbn not in self.dic_book:
                print("Book added successfully! ")
        else:
            print(f"The book with {isbn} is already in the library")

    def removeBook(isbn):
        with open("book.txt",mode="r") as f:
                    content = f.read()
        if isbn in content:
             pass