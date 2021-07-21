class Library:
    books = []

    def find_book(self, title):
        for b in self.books:
            if b.title == title:
                return b


class Book:
    def __init__(self, title, author, location):
        self.title = title
        self.author = author
        self.location = location
        self.page = 0


class ExploreBook:
    @staticmethod
    def page(book):
        return book.page

    @staticmethod
    def location(book):
        return book.location

    @staticmethod
    def title(book):
        return f"{book.title} - {book.author}"
