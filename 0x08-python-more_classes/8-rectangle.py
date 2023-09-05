#!/usr/bin/python3
"""
Defining a class named Rectangle
that has width and height as an
attributes
"""


class Rectangle:
    """
    This class represent a Rectangle

    Args:
        width(int): the width of the rectangle
        height(int): the height ofthe rectangle
    """
    """ count number of Rectangle instance created """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        initialize a Rectangle objects

        Args:
            width(int): The width of the rectangle
            height(int): The height of the rectangle
        """

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        To get the width of rectangle

        Return:
            int: The width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle

        Args:
            values(int): the value to be set to the width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Get the heigth of the rectangle

        Return:
            int: The height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        To set height of the rectangle
        Args:
            value(int): value to be set to height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        This method calculate the area of a rectangle
        """
        return self.__width * self.__height

    def perimeter(self):

        """ calculate the perimeter of rectangle """

        if self.__width == 0 or self.__height == 0:
            perimeter = 0
        else:
            perimeter = 2 * (self.__width + self.__height)
        return perimeter

    def __str__(self):
        """ draw "#" using the attributes of height and weight """

        if self.__width == 0 or self.__height == 0:
            return ""

        draw_rec = ""
        for i in range(self.__height):
            draw_rec += str(self.print_symbol) * self.__width
            if i < self.__height - 1:
                draw_rec += "\n"
        return draw_rec

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """ To delete an instance """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
