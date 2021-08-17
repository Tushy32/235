class Publisher:
    def __init__(self, publisher_name: str):
        self.__name = publisher_name

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, publisher_name):
        if isinstance(publisher_name, Publisher):
            self.__publisher = publisher_name
        else:
            raise ValueError

    def __repr__(self):
        # we use access via the property here
        return f'<Publisher {self.name}>'

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return other.name == self.name

    def __lt__(self, other):
        # TODO
        pass

    def __hash__(self):
        # TODO
        pass
