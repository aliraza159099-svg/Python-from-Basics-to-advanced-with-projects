
dic_books = {

}
dic_members = {

}
class Book:
    def __init__(self,title,author,isbn,issued=False,issued_to=None):
        self.title  = title
        self.author = author
        self.isbn = isbn
        self.issued = issued
        self.issued_to = issued_to

class Member:
    def __init__(self,name,id):
        self.name  = name
        self.id = id 
        print(f"{self.name} is added successfully")
        if name not in dic_members:
            dic_members.update({name:id})

