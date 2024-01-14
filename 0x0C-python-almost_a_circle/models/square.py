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

        return f"[{self.__class__.__name__} ({self.id}) {self.x}/{self.y} - {self.width}]"

    @property
    def size(self):
        """ Getter for size """
       
        return self.width

    @size.setter
    def size(self, value):
        """ Setter for size """
       
        self.width = value
        self.height = value

