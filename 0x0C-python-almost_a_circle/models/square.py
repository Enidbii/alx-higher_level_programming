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

    @property
    def size(self):
        """ size getter """
        return self.width

    @size.setter
    def size(self, value):
        """ sets size using both height and width """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ update class """
        if args:
            list_attr = ['id', 'size', 'x', 'y']
            j = 0
            for arg in args:
                setattr(self, list_attr[j], arg)
                j += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ returns dict representation of class """
        return {'id': self.id,'x': self.x,'size': self.size,
                'y': self.y}
