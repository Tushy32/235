from datetime import datetime

from domainmodel.publisher import Publisher
from domainmodel.Author import Author
from domainmodel.book import Book

class Review:
    def __init__(self, parameters_book, review_text, rating):
        if isinstance(parameters_book, Book):
            self.__parameters_book = parameters_book
        else:
            self.__parameters_book = None

        if isinstance(review_text, str):
            self.__review_text = review_text.strip()
        else:
            self.__review_text = "N/A"

        if isinstance(rating, int):
            if 5 >= rating >= 1:
                self.__rating = rating
            else:
                raise ValueError
        else:
            raise ValueError

        self.__timestamp = datetime

    @property
    def parameters_book(self):
        return self.__parameters_book
    @property
    def review_text(self):
        return self.__review_text
    @property
    def rating(self):
        return self.__rating
    @property
    def timestamp(self):
        return self.__timestamp

    def __repr__(self):
        # we use access via the property here
        return f'<{self.__parameters_book}, {self.__rating}, {self.__timestamp}>'

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return other.__timestamp == self.__timestamp



if __name__ == "__main__":
    book = Book(2675376, "Harry Potter")
    review_text = "  This book was very enjoyable.   "
    rating = 4
    review = Review(book, review_text, rating)

    print(review.parameters_book)
    print("Review: {}".format(review.review_text))
    print("Rating: {}".format(review.rating))