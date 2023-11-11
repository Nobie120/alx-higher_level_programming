#!/usr/bin/python3
''' rectangle class '''


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
            self.validate_func("x", value, eq = False)
            self.__x = value

        @property
        def y(self):
            ''' getter for y '''
            return self.__y

        @y.setter
        def y(self, value):
            ''' setter for y '''
            self.validate_func("y", value, eq = False)
            self.__y = value

        def validate_func(self, name, value, eq = True):
            ''' method for validating the attributes '''
            if type(value) is not int:
                raise TypeError(f"{name} must be an integer.")
            if eq and value <= 0:
                raise ValueError(f"{name} must be > 0")
            elif not eq and value < 0:
                raise ValueError(f"{name} must be >= 0")
