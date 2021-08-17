from domainmodel.publisher import Publisher
from domainmodel.Author import Author


class Book:
    def __init__(self, book_id, title):
        if isinstance(title, str):
            if len(title.strip()) != 0:
                self.__title = title.strip()
            else:
                raise ValueError
        else:
            raise ValueError

        if isinstance(book_id, int):
            self.__book_id = book_id
        else:
            raise ValueError

        self.__description = None
        self.__publisher = None
        self.__authors = []
        self.__release_year = None
        self.__ebook = None

    @property
    def book_id(self) -> int:
        return self.__book_id

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        if isinstance(title, str):
            if len(title.strip()) != 0:
                self.__title = title.strip()
            else:
                raise ValueError
        else:
            raise ValueError

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, des):
        if isinstance(des, str):
            if len(des.strip()) == 0:
                raise ValueError
            else:
                self.__description = des
        else:
            raise ValueError

    @property
    def publisher(self):
        return self.__publisher

    @publisher.setter
    def publisher(self, pub):
        if isinstance(pub, Publisher):
            self.__publisher = pub
        else:
            raise ValueError

    @property
    def authors(self):
        return self.__authors

    @authors.setter
    def authors(self, aut):
        if isinstance(aut, Author):
            self.__authors.append(aut)
        else:
            raise ValueError

    @property
    def release_year(self):
        return self.__release_year

    @release_year.setter
    def release_year(self, year):
        if isinstance(year, int):
            if year < 0:
                raise ValueError
            else:
                self.__release_year = year
        else:
            raise ValueError

    @property
    def ebook(self):
        return self.__ebook

    @ebook.setter
    def ebook(self, bo):
        if isinstance(bo, bool):
            self.__ebook = bo
        else:
            raise ValueError

    def __repr__(self):
        # we use access via the property here
        return f'<Book {self.__title}, book id = {self.__book_id}>'

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return other.__book_id == self.__book_id

    def __lt__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.__book_id < other.__book_id

    def __hash__(self):
        return hash(self.__book_id)

    def add_author(self, author):
        if isinstance(author, Author):
            self.__authors.append(author)

    def remove_author(self, author):
        if isinstance(author, Author):
            if author in self.__authors:
                self.__auhtors.remove(author)


if __name__ == "__main__":
    book = Book(84765876, "Harry Potter")
    print(book)

    publisher = Publisher("Bloomsbury")
    book.publisher = publisher
    print(book.publisher)

    author = Author(635, "J.K. Rowling")
    book.add_author(author)
    print(book.authors)