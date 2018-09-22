"""Class to represent the m*n table
"""


class Table(object):

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    @property
    def length(self):
        return self.__length

    @property
    def breadth(self):
        return self.__breadth

    @length.setter
    def length(self, value):
        if not isinstance(value, int):
            raise TypeError("sides must be set to an integer")
        self.__length = value

    @breadth.setter
    def breadth(self, value):
        if not isinstance(value, int):
            raise TypeError("sides must be set to an integer")
        self.__breadth = value

    def position_validator(self, pos):
        if pos >= self.breadth or pos >= self.length:
            return False
        else:
            return True
