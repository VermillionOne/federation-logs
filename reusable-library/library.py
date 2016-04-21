'''
RoomMeasurements class
    attributes:
    - length
    - width
    - height
'''
class RoomMeasurements(object):
    def __init__(self):
        # Defining the measurement values to be used to determing room square footage
        self.length = 0
        self.width = 0
        self.height = 0

    # Getter for room length
    @property
    def length(self):
        # Return value of length
        return self.__length
    # Setter for room length
    @length.setter
    def length(self, new_length):
        # If the length is greater than 0
        if new_length > 0:
            # set length to new value
            self.__length = new_length
        else:
            # Otherwise, print error message and set length to 0
            print 'Error: Invalid Length Value'
            self.__length = 0

    # Getter for room width
    @property
    def width(self):
        # Return value of width
        return self.__width
    # Setter for room width
    @width.setter
    def width(self, new_width):
        # If the width is greater than 0
        if new_width > 0:
            # set width to new value
            self.__width = new_width
        else:
            # Otherwise, print error message and set width to 0
            print 'Error: Invalid Width Value'
            self.__width = 0

    # Getter for room height
    @property
    def height(self):
        # Return value of height
        return self.__height
    # Setter for room height
    @height.setter
    def height(self, new_height):
        # If the height is greater than 0
        if new_height > 0:
            # set height to new value
            self.__height = new_height
        else:
            # Otherwise, print error message and set height to 0
            print 'Error: Invalid Height Value'
            self.__height = 0
