import math
'''
RoomMeasurements class
    Attributes:
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

'''
EvaluateArea class
    Attributes:
     __include_ceiling
     __wall_area
     __ceiling_area
'''
class AreaController(object):
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
            room.length |-> x_length
            room.width  |-> y_width
            room.height |-> z_height
    '''
    def find_wall_area(self, x_length, y_width, z_height):
        # If the length, width, and height values area all greater than 0
        if x_length > 0 and y_width > 0 and z_height > 0:
            # Determine the combined area of the room walls
            return 2*(x_length * z_height) + 2*(y_width * z_height)
        # If length has no value or is equal to or less than zero
        elif x_length == '' or x_length <= 0:
            # Return that length needs a positive value
            print "Please provide a value for length."
        # If width has no value or is equal to or less than zero
        elif y_width == '' or y_width <= 0:
            # Return that width needs a positive value
            print "Please provide a value for width."
        # If height has no value or is equal to or less than zero
        elif z_height == '' or z_height <= 0:
            # Return that height needs a positive value
            print "Please provide a value for height."

    '''
    find_ceiling_area function
        Arguments accepted:
            room.length |-> x_length
            room.width  |-> y_width
    '''
    def find_ceiling_area(self, x_length, y_width):
        # If the length abd width values area all greater than 0
        if x_length > 0 and y_width > 0:
            # Determine the area of the ceiling
            return x_length * y_width
        # If length has no value or is equal to or less than zero
        elif x_length == '' or x_length <= 0:
            # Return that length needs a positive value
            print "Please provide a value for length."
        # If width has no value or is equal to or less than zero
        elif y_width == '' or y_width <= 0:
            # Return that width needs a positive value
            print "Please provide a value for width."

'''
EvaluateVolume class
    Attributes:
     __primer_coverage
'''
class VolumeController(object):
    def __init__(self):
        self.__primer_coverage = 200
        self.__finish_covergage = 350

    # Getter for primer coverage value
    # Static value - Read Only
    @property
    def primer_coverage(self):
        return self.__primer_coverage
    # Getter for finish coverage value
    # Static value - Read Only
    @property
    def finish_coverage(self):
        return self.__finish_covergage

    '''
    find_paint_volume function
        Arguments accepted:
            self.wall_area, self.ceiling_area
                |-> area
            self.primer_coverage, self.finish_coverage
                |-> volume
    '''
    def find_paint_volume(self, area, volume):
        # If area is greater than 0
        if area > 0:
            # Set area as a decimal number to allow for math manipulation
            area = float(area)
        else: # area may also be a string, in which case
            # Set area to 0 to establish as an operable value
            area = 0

        # If area and volume are both greater than 0
        if area > 0 and volume > 0:
            # return the dividend of the area divided by volume
            return area / volume
        else:
            # Otherwise, set returned value to 0 and report that there are incorrect values
            return 0
            print "Invalid Values"

    '''
    determine_volume_unit function
        Arguments accepted:
            self.wall_primer_volume, self.wall_finish_volume
                |-> volume_decimal
    '''
    def determine_volume_unit(self, volume_decimal):
        # Set volume number as rounded whole number for use in units
        volume_decimal = round(100*(float(volume_decimal)))
        # Determine which volume unit to use: quart or gallon
        # If volume_decimal is less than 25, set unit to be one 1 quart
        if 0 < volume_decimal < 25:
            return '1 quart'
        # If volume_decimal is less than 50, set unit to be one 2 quarts
        elif 26 < volume_decimal < 50:
            return '2 quarts'
        # If volume_decimal is less than 75, set unit to be one 3 quarts
        elif 51 < volume_decimal < 75:
            return '3 quarts'
        # If volume_decimal is less than 100, set unit to be one 1 gallon
        elif 76 < volume_decimal < 100:
            return '1 gallon'
        # If volume_decimal is less than 50, set unit to be one 2 gallons
        elif volume_decimal < 150:
            return '2 gallons'
        # if any other value return, set unit to gallons of next whole number
        else:
            return str(int(math.ceil(volume_decimal/100))) + " gallons"
# To Do List:
# Create functions to added page sections
# Finish Adding comments
