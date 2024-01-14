#!/usr/bin/python3
""" id managment base object """

import json

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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Return the JSON string representation of list_dictionaries """
        
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

     @classmethod
    def save_to_file(cls, list_objs):
        """ Write the JSON string representation of list_objs to a file """
        
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, mode="w", encoding="utf-8") as file:
            file.write(cls.to_json_string([obj.to_dictionary() for obj in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """ Return the list of the JSON string representation """
        
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    
    @classmethod
    def create(cls, **dictionary):
        """ Return an instance with all attributes already set """
        
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        else:
            raise NotImplementedError("Class not supported in create method")

        dummy_instance.update(**dictionary)
        return dummy_instance
