class Book:
    def __init__(self,book_name,author,page):
        self.book_name = book_name
        self.author = author
        self.page = page
        self.current_page = 0

    def description(self):
        return f"The book {self.book_name} is written by {self.author} has {self.page} number of pages "

    def read_pages(self, pages_read):
        self.current_page += pages_read
        print(f"You read {pages_read} pages. You are now on page {self.current_page}/{self.page}.")



b1 = Book("The Art of Life","Alex Barick",1200)
print(b1.description())
b1.read_pages(12)
b2 = Book("The Archamedis","Paulo Coulee",360)
b1.read_pages(20)
print(b2.description())