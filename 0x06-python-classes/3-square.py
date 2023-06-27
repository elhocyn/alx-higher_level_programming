#!/usr/bin/python3
"""Class Square"""


class Square:
    """Defines a square class:
    - Private instance attribute: size
    - Instantatiation with optional size: def __init__(self, size=0)"""

    def __init__(self, size=0):
        """size is a private attribute:
            - size must be an integer, otherwise raise a TypeError
            exception with the message size must be an integer
            - if size is less than 0, raise a ValueError exception
            with the message size must be >= 0"""
        if (type(size) is not int):
            raise (TypeError("size must be an integer"))
        elif (size < 0):
            raise (ValueError("size must be >= 0"))
        else:
            self.__size = size

    def area(self):
        """- Public instance method: def area(self): that returns
            the current square area"""
        return (self.__size * self.__size)
