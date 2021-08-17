
class Author:
    def __init__(self, author_id, author_full_name):
        self.__coauthor = []
        if type(author_id) == int and type(author_full_name) == str:
            if author_id > 0 and author_full_name.strip():
                self.__author_id = author_id
                self.__author_full_name = author_full_name
            else:
                raise ValueError
        else:
            raise ValueError

    @property
    def full_name(self) -> str:
        return self.__author_full_name

    @full_name.setter
    def full_name(self, publisher_name):
        self.__author_full_name = publisher_name
        return self.__author_full_name

    @property
    def unique_id(self) -> int:
        return self.__author_id

    def __repr__(self):
        # we use access via the property here
        return f'<Author {self.__author_full_name}, author id = {self.__author_id}>'

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return other.__author_id == self.__author_id

    def __lt__(self, other):
        return self.__author_id < other.__author_id

    def __hash__(self):
        return hash((self.__author_id))

    def add_coauthor(self, coauthor):
        self.__coauthor.append(coauthor)
        coauthor.__coauthor.append(self)

    def check_if_this_author_coauthored_with(self, author):
        if author in self.__coauthor:
            return True
        return False

def main():
    author1 = Author(3675, "Barack Obama")
    print(author1)
    try:
        author2 = Author(123, "  ")
        print(author2)
    except ValueError:
        print("ValueError was raised!")
    try:
        author3 = Author(42, 42)
        print(author3)
    except ValueError:
        print("ValueError was raised!")
    author4 = Author(23, "J.R.R. Tolkien")
    print(author4.unique_id, author4.full_name)
main