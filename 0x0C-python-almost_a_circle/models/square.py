#!/usr/bin/python3
""" a new rectangle with special size """

from models.rectangle import Rectangle

class Square(Rectangle):
    """ our new special guest """

    def __init__(self, size, x=0, y=0, id=None):
        """ Constructor of our new guest THE SQUAAAARE"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ String representing our new guest """

        return f"[{self.__class__.__name__}] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """ Getter for size """
       
        return self.width

    @size.setter
    def size(self, value):
        """ Setter for size """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be >= 0")

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ updating the square values if needed """

        attributes = ["id", "size", "x", "y"]

        if args:
            for i in range(len(args)):
                if i < len(attributes):
                    setattr(self, attributes[i], args[i])
                else:
                    break

        elif kwargs:
            for keys, values in kwargs.items():
                if keys in attributes:
                    setattr(self, keys, values)
    

    def to_dictionary(self):
        """ Return dictionary representation of our Cute guest """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
