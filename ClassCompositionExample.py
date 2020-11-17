from typing import List #List, tuple, set... etc
import sys

class BookShelf:
    def __init__(self, *books): #When calling a function, the * operator can be used to unpack an iterable into the arguments in the function call
        self.books = books
    #Type hinting -> the value that must be returned or ": str" after an argument to mention the type of variable is expected.
    def __str__(self) -> str: 
        return f"Bookshelf with {len(self.books)} books."
class Book:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Book {self.name}."


book = Book("HArry Potter")
book2 = Book ("Python 101")
shelf = BookShelf(book, book2)

print(shelf)
print(shelf.books)
print(sys.path)

#-----------Note--------------
#Visit this URL to know more about https://treyhunner.com/2018/10/asterisks-in-python-what-they-are-and-how-to-use-them/
#Using * and ** to pass arguments to a function
#Using * and ** to capture arguments passed into a function
#Using * to accept keyword-only arguments
#Using * to capture items during tuple unpacking
#Using * to unpack iterables into a list/tuple
#Using ** to unpack dictionaries into other dictionaries