#!/usr/bin/python3

"""Defines a magic class """
import math


class MagicClass:
    """ class represent a magic class """
    def _init_(self, radius=0):
        """ initilization of radius """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """ define area of circle """
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """ define area of circle """
        return 2 * math.pi * self.__radius
