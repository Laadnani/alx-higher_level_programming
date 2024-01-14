#!/usr/bin/python3
""" id managment base object """

class Base:
    """
    This class will be the “base” of all other classes in this project.
    The goal of it is to manage id attribute in all your future classes 
    and to avoid duplicating the same code (by extension, same bugs)
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            Base.id = id
        else:
            Base.__nb_objects += 1
            Base.id = Base.__nb_objects
