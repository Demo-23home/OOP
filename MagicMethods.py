class Book:
    def __init__(self, title: str, author: str, num_pages: int) -> None:
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self) -> str:
        return f"'{self.title}' by {self.author}"

    def __eq__(self, other) -> bool:
        return self.author == other.author and self.title == other.title

    def __lt__(self, other) -> bool:
        return self.num_pages < other.num_pages

    def __add__(self, other) -> int:
        return self.num_pages + other.num_pages

    def __contains__(self, keyword:str):
        return keyword in self.title or keyword in self.author
    
    
    def __getitem__(self, key:str) -> str:
        return self.title if key == 'title' else self.author


book1 = Book("hello my name is zeyad", "Zeyad", 100)
book2 = Book("book2", "Mohammed", 100)
book3 = Book("book3", "Salama", 150)


print(book1)
print(book2 == book1)
print(book3 < book1)
print(book3 + book1)
print("name" in book1)
print(book1['title'])
