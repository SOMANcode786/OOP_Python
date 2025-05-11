class Book:

    def __init__(self,title,author,publisher,price):
        '''Initialize the book with title, author, publisher, and price.'''
        self.title = title
        self.author = author
        self.publisher = publisher
        self.price = price
        '''Display the book's information.'''
    def display(self):
        print(f"Title: {self.title} , Author : {self.author} ,Publisher : {self.publisher}, Price : {self.price}")
book1=Book("Python Programming" , "John Doe", "Tech Books", 29.99)
book1.display() 