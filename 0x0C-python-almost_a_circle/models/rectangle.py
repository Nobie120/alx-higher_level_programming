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
            self.__width = value

        @property
        def height(self):
            ''' getter for height '''
            return self.__height

        @height.setter
        def height(self, value):
            ''' setter for height '''
            self.__height = value

        @property
        def x(self):
            ''' getter for x '''
            return self.__x

        @x.setter
        def x(self, value):
            ''' setter for x '''
            self.__x = value

        @property
        def y(self):
            ''' getter for y '''
            return self.__y

        @y.setter
        def y(self, value):
            ''' setter for y '''
            self.__y = value
