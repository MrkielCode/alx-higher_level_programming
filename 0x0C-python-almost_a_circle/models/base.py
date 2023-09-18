#!/usr/bin/python3

"""
Defining a base class
"""
import json
import os
import csv
import turtle


class Base:
    """
    Defining a base class

    Methods:
        __init__: class constructor
    Args:
        id(int): intger value arguments
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """ initializing id attributes """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ converting dictionary to json string """

        if list_dictionaries is None or len(list_dictionaries) <= 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ saving json to a file """
        filename = cls.__name__ + ".json"

        if list_objs is None:
            json_string = "[]"
        else:
            json_string = cls.to_json_string([obj.to_dictionary()
                                             for obj in list_objs])

        with open(filename, 'w') as file:
            file.write(json_string)

        return json_string

    @staticmethod
    def from_json_string(json_string):
        """ loads list to json representation """
        if json_string is None or json_string == []:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ This creates an instance of a class """
        if cls.__name__ == "Rectangle":
            dummy_attr = cls(1, 1)
        else:
            dummy_attr = cls(1)

        dummy_attr.update(**dictionary)

        return dummy_attr

    @classmethod
    def load_from_file(cls):
        """ This loads a file and create an instance """

        filename = f"{cls.__name__}.json"
        if not os.path.exists(filename):
            return []

        with open(filename, 'r') as f:
            json_string = f.read()

        dicts = cls.from_json_string(json_string)

        return [cls.create(**class_rep) for class_rep in dicts]

    @classmethod
    def save_to_file_csv(cls, list_objs):

        classname = cls.__name__
        filename = classname + ".csv"

        with open(filename, 'w', newline="") as csv_file:
            if list_objs is None or list_objs == []:
                csv_file.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """ To csv file from function """
        filename = f"{cls.__name__}.csv"

        if not os.path.exists(filename):
            return []

        with open(filename, 'r', newline="") as csv_file:
            if cls.__name__ == "Rectangle":
                fieldnames = ["id", "width", "height", "x", "y"]
            else:
                fieldnames = ["id", "size", "x", "y"]

            reader = csv.DictReader(csv_file, fieldnames=fieldnames)
            reader = [dict([k, int(v)] for k, v in d.items()) for d in reader]

            return [cls.create(**d) for d in reader]

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ To create an turtle graphics """
        turtle.speed(0)
        turtle.bgcolor("white")

        for rect in list_rectangles:
            turtle.penup()
            turtle.goto(rect.x, rect.y)
            turtle.pendown()
            for _ in range(2):
                turtle.forward(rect.width)
                turtle.left(90)
                turtle.forward(rect.height)
                turtle.left(90)

        for square in list_squares:
            turtle.penup()
            turtle.goto(square.x, square.y)
            turtle.pendown()
            for _ in range(4):
                turtle.forward(square.size)
                turtle.left(90)

        turtle.exitonclick()
