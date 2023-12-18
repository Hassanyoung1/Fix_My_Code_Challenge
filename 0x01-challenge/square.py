#!/usr/bin/python3
"""Define the Square class."""


class Square():
    """A class representing a square.

    Attributes:
    - width (int): The width of the square.
    - height (int): The height of the square.

    Methods:
    - __init__(self, width=0, height=0, **kwargs): Constructor to
    initialize the square.
    - area_of_my_square(self): Calculate the area of the square.
    - perimeter_of_my_square(self): Calculate the perimeter of the square.
    - __str__(self): String representation of the square, including division
    result.
    """

    def __init__(self, width=0, height=0, **kwargs):
        """Initialize a Square instance with optional width, height, and
        additional attributes."""
        self.width = width
        self.height = height

        # Set additional attributes from kwargs
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """Calculate the area of the square."""
        return self.width * self.height

    def perimeter_of_my_square(self):
        """Calculate the perimeter of the square."""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """Return a string representation of the square, including division
        result."""
        division_result = self.width / self.height
        return "{}/{} = {}".format(self.width, self.height,
                                                   division_result)


if __name__ == "__main__":
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
