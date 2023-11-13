#!/usr/bin/python3
''' rectangle class '''
from base import Base



class Rectangle(Base):
    ''' the class rectagle '''

    def __init__(self, width, height, x=0, y=0, id=None):
        ''' class constructor '''

        super().__init__(id)
        self.width = width
        silf.height = height
        self.x = x
        self.y = y

        @property
        def width(self):
            ''' width getter '''
            return self.__width

        @width.setter
        def width(self, value):
            ''' setter for wifth '''
            self.validate_func("width", value)
            self.__width = value

        @property
        def height(self):
            ''' getter for height '''
            return self.__height

        @height.setter
        def height(self, value):
            ''' setter for height '''
            self.validate_func("height", value)
            self.__height = value

        @property
        def x(self):
            ''' getter for x '''
            return self.__x

        @x.setter
        def x(self, value):
            ''' setter for x '''
            self.validate_func("x", value, False)
            self.__x = value

        @property
        def y(self):
            ''' getter for y '''
            return self.__y

        @y.setter
        def y(self, value):
            ''' setter for y '''
            self.validate_func("y", value, False)
            self.__y = value

        def validate_func(self, name, value, eq=True):
            ''' method for validating the attributes '''
            if type(value) is not int:
                raise TypeError(f"{name} must be an integer.")
            if eq and value <= 0:
                raise ValueError(f"{name} must be > 0")
            elif not eq and value < 0:
                raise ValueError(f"{name} must be >= 0")

        def area(self):
            ''' method for finding area of rectangle '''
            return self.width * self.height

        def display(self):
            ''' method for displaying '''
            s = '\n' * self.y + \
                (' ' * self.x + '#' * self.width + '\n') * self.height
            print(s, end="")

        def __str__(self):
            '''Returns string info about this rectangle.'''
            return '[{}] ({}) {}/{} - {}/{}'.\
                format(
                        type(self).__name__, self.id, self.x, self.y,
                        self.width, self.height)

        def __update(self, id=None, width=None, height=None, x=None, y=None):
            '''updates instance attributes via */**args.'''
            if id is not None:
                self.id = id
            if width is not None:
                self.width = width
            if height is not None:
                self.height = height
            if x is not None:
                self.x = x
            if y is not None:
                self.y = y

        def update(self, *args, **kwargs):
            '''Updates attributes via no-keyword & keyword args.'''
            # print(args, kwargs)
            if args:
                self.__update(*args)
            elif kwargs:
                self.__update(**kwargs)

        def to_dictionary(self):
            '''Returns dictionary representation of this class.'''
            return {"id": self.id, "width": self.__width,
                    "height": self.__height, "x": self.__x, "y": self.__y}
