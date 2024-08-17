

class Library:
    def __init__(self, name:str) -> None:
        self.name = name
        self.books:list[Book] = []
        
    def add_book(self, book: "Book") -> None:
        self.books.append(book)
        
    def list_books(self) -> None:
        for book in self.books:
            print(book.title, book.author)


class Book:
    def __init__(self, author:str, title:str):
        self.author = author
        self.title = title
        
        
library = Library("NDAM")
book1 = Book("Zeyad", "Not Now!")
book2 = Book("Mohammed", "Not Now2!")
book3 = Book("Salama", "Not Now3!")


library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

library.list_books()