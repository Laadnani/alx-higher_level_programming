#!/usr/bin/python3
""" rectangle ogject creation """

from models.base import Base

class Rectangle(Base):
    """ a new class that create rectangles based on given dimentions """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    """ Width Getter and setter """
    @property
    def width(self):
        """ width Getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ width Setter """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
            
        if value <= 0:
            raise ValueError("width must be > 0")
            
        self.__width = value

    """ height Getter and setter """
    @property    
    def height(self):
        """ height Getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ Height Setter """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    """ X Axis Getter and setter """
    @property    
    def x(self):
        """ X axis Getter """
        return self.__x

    @x.setter
    def x(self, value):
        """ X Axis Setter """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be > 0")
            
        self.__x = value

    """ Y Axis Getter and setter """
    @property    
    def y(self):
        """ Y Axis Getter """
        return self.__y

    @y.setter
    def y(self, value):
        """ Y Axis Setter """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
            
        if value < 0:
            raise ValueError("y must be > 0")
        
        self.__y = value

    def area(self):
        """ define the aread of the Rectangle """
        return self.__width * self.__height
