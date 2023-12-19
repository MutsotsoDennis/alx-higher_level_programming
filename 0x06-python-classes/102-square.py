#!/usr/bin/python3
"""Square class definition"""

class Square:
    """Square class"""

    def __init__(self, size=0):
        """Square constructor 
        Args:
            size (int): length of a side of Square
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    @property
    def size(self):
        """The property of size as the length 
        of a side of Square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method for size property
        Args:
            value (int): new size value
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Get the area instance for comparators"""
        return self.__size * self.__size

    # ... (comparator methods)
