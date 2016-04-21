'''
RoomMeasurements class
    attributes:
     __length
     __width
     __height
'''
class RoomMeasurements(object):
    def __init__(self):
        # Defining the measurement values to be used to determing room square footage
        self.__length = 0
        self.__width = 0
        self.__height = 0

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
            print self.__length
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
            print self.__width
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
            print self.__height
        else:
            # Otherwise, print error message and set height to 0
            print 'Error: Invalid Height Value'
            self.__height = 0

'''
EvaluateArea class
    attributes:
     __include_ceiling
     __wall_area
     __ceiling_area
'''
class EvaluateArea(object):
    def __init__(self):
        self.__include_ceiling = False

    # Getter for __include_ceiling
    @property
    def include_ceiling(self):
        return self.__include_ceiling
    # Setter for __include_ceiling
    @include_ceiling.setter
    def include_ceiling(self, new_ceiling):
        # if ceiling area is included
        if new_ceiling == True:
            # set __include_ceiling to True
            self.__include_ceiling = True
        else:
            # Otherwise, set __include_ceiling to False
            self.__include_ceiling = False

    '''
    find_wall_area function
        Arguments accepted:
        from RoomMeasurements()
            room.length ==> x_length
            room.width  ==> y_width
            room.height ==> z_height
    '''
    def find_wall_area(self, x_length, y_width, z_height):
        if x_length > 0 and y_width > 0 and z_height > 0:
            return 2*(x_length * z_height) + 2*(y_width * z_height)
        else:
            return "Invalid Values"

    '''
    find_ceiling_area function
        Arguments accepted:
        from RoomMeasurements()
            room.length ==> x_length
            room.width  ==> y_width

    '''
    def find_ceiling_area(self, x_length, y_width):
        if x_length > 0 and y_width > 0:
            return x_length * y_width
        else:
            return "Invalid Values"
'''
EvaluateVolume class
    attributes:
'''
class EvaluateVolume(object):

    '''
    find_paint_volume function
        Arguments accepted:
        surface area ==> area
        paint volume ==> volume
    '''
    def find_paint_volume(self, area, volume):
        print area, '==> area 1'
        area = float(area)
        print area, '==> area 2'
        if area > 0 and volume > 0:
            return area / volume
        else:
            return "Invalid Values"

    def determine_volume_unit(self, volume_decimal):
        print volume_decimal
        volume_decimal = float(volume_decimal)
        print volume_decimal
        volume_decimal = 100 * volume_decimal
        print volume_decimal
        volume_decimal = round(volume_decimal)
        print volume_decimal
        if volume_decimal < 25:
            return '1 quart'
        elif volume_decimal < 50:
            return '2 quarts'
        elif volume_decimal < 75:
            return '3 quarts'
        elif volume_decimal < 100:
            return '4 quarts'
        elif volume_decimal < 125:
            return "1 gallon"
        else:
            return str(round(volume_decimal/100)) + " gallons"
# To Do List:
# Create functions to added page sections
# Finish Adding comments
