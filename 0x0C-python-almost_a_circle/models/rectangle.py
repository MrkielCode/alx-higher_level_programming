#!/usr/bin/python3

"""
This class represent the rectangle class
which inherit properties of Base class
"""

from models.base import Base


class Rectangle(Base):
    """
    initialization of attributes

    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Args:
            width(int) - the width of the rectangle
            height(int) - the height of the rectangle
            x(int) - the x value of the rectangle
            y(int) - The y value of the rectangle
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ getting the width value """
        return self.__width

    @width.setter
    def width(self, value):
        """ setting the width value """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):

        """ getting the height value """
        return self.__height

    @height.setter
    def height(self, value):

        """ setting the width value """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ getting the height value """
        return self.__x

    @x.setter
    def x(self, value):
        """ setting the width value """

        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ getting the x value """
        return self.__y

    @y.setter
    def y(self, value):
        """ setting the y value """

        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ This calculate the area of rectangle """
        return self.__width * self.__height

    def display(self):
        """ This diplay "#" depending on the value
        of height and width
        """
        if self.__width == 0 or self.__height == 0:
            return

        for _ in range(self.__y):
            print()

        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """ overriding the str method """

        return (
                f"[Rectangle] ({self.id}) {self.x}/{self.y} - "
                f"{self.width}/{self.height}"
        )

    def update(self, *args, **kwargs):

        """ This accept series of parameters and
        updates the class attributes
        """
        if args:
            for key, value in enumerate(args):
                if key == 0:
                    self.id = value
                elif key == 1:
                    self.width = value
                elif key == 2:
                    self.height = value
                elif key == 3:
                    self.x = value
                elif key == 4:
                    self.y = value
        elif kwargs:
            for (key, value) in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        return dictionary representation of rectangle
        """
        return {
                'x': self.x, 'y': self.y, 'id': self.id,
                'width': self.width, 'height': self.height
                }
