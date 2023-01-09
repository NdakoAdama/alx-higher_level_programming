PrincessRuth90
/
alx-higher_level_programming
Public
Code
Issues
Pull requests
Actions
Projects
Security
Insights
alx-higher_level_programming/0x0A-python-inheritance/11-square.py
@PrincessRuth90
PrincessRuth90 Square #2
 1 contributor
Executable File  35 lines (30 sloc)  1.02 KB
#!/usr/bin/python3
"""
Contains parent class BaseGeometry
with public instance method area and integer_validation
Contains subclass Rectangle
with instantiation of private attributes width and height, validated by parent,
extends parent's area method and prints with __str__
Contains subclass Square
with instantiation of private attribute size, validated by superclass,
and prints with __str__
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """inherits from Rectangle, who inherits from BaseGeometry
    methods:
        __init__(self, size)
        __str__(self)
    """
    def __init__(self, size):
        """initializes size
        Args:
            size (int): private
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """prints [Square] <width>/<height>"""
        return "[{:s}] {:d}/{:d}".format(self.__class__.__name__,
                                         self.__size, self.__size)
