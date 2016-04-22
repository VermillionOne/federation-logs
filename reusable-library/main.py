import webapp2
from library import UserInfo, RoomMeasurements, AreaController, VolumeController
from page import Page
class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')
        self.wall_area = 0

        # Set classes for use in MainHandler
        user = UserInfo()
        room = RoomMeasurements()
        area = AreaController()
        volume = VolumeController()

        '''
        Manually Setting Values for testing only
        ---
        Will be replaced by user input values
        '''
        user.name ='Tim Castillo'
        user.email = "tjc0609@gmail.com"
        room.length = 0
        room.width  = 0
        room.height = 0
        area.include_ceiling = True
        '''
        End of manually entered values
        '''

        # Find primer coverage
        self.primer_coverage = volume.primer_coverage
        # Find Finish coverage
        self.finish_coverage = volume.finish_coverage

        # Find room's wall area with given form data
        self.wall_area = area.find_wall_area(room.length, room.width, room.height)
        # Find ceiling with given form data
        self.ceiling_area = area.find_ceiling_area(room.length, room.width)
        # Find the volume of primer needed for the wall area
        self.wall_primer_volume = volume.find_paint_volume(self.wall_area, self.primer_coverage)
        # Find the volume of finish needed for the wall area
        self.wall_finish_volume = volume.find_paint_volume(self.wall_area, self.finish_coverage)

        # Find the unit of primer needed for wall area presentable for UI output
        self.wall_primer_unit = volume.determine_volume_unit(self.wall_primer_volume)
        # Find the unit of finish needed for wall area presentable for UI output
        self.wall_finish_unit = volume.determine_volume_unit(self.wall_finish_volume)

        print self.wall_primer_unit
        print self.wall_finish_unit


        # Find the volume of primer needed for the ceiling area
        self.ceiling_primer_volume = volume.find_paint_volume(self.ceiling_area, self.primer_coverage)
        # Find the volume of finish needed for the ceiling area
        self.ceiling_finish_volume = volume.find_paint_volume(self.ceiling_area, self.finish_coverage)

        # Find the unit of primer needed for ceiling area presentable for UI output
        self.ceiling_primer_unit = volume.determine_volume_unit(self.ceiling_primer_volume)
        # Find the unit of finish needed for ceiling area presentable for UI output
        self.ceiling_finish_unit = volume.determine_volume_unit(self.ceiling_finish_volume)

        print self.ceiling_primer_unit
        print self.ceiling_finish_unit

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
