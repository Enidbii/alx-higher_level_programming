#!/usr/bin/python3
""" square module """


from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class """
    def __init__(self, size, x=0, y=0, id=None):
        """
        class constructor
        Args:
            size: length of square
            x: square positions
            y: square position
            id: square id
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ overloading str method """
        return ("[{}] ({}) {}/{} - {}".format(__class__.__name__,
                                             self.id, self.x,
                                             self.y, self.height))
