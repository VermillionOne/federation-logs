import webapp2
from library import RoomMeasurements, AreaController, VolumeController
from page import Page
class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')
        self.wall_area = 0

        # Set classes for use in MainHandler
        room = RoomMeasurements()
        area = AreaController()
        volume = VolumeController()

        '''
        Manually Setting Values for testing only
        ---
        Will be replaced by user input values
        '''
        room.length = 12
        room.width  = 15
        room.height = 8
        area.include_ceiling = True

        self.primer_coverage = volume.primer_coverage
        self.finish_coverage = volume.finish_coverage


        self.wall_area = area.find_wall_area(room.length, room.width, room.height)
        print self.wall_area, "wall_area"
        self.ceiling_area = area.find_ceiling_area(room.length, room.width)
        self.wall_primer_volume = volume.find_paint_volume(self.wall_area, self.primer_coverage)
        self.wall_finish_volume = volume.find_paint_volume(self.wall_area, self.finish_coverage)

        self.wall_primer_unit = volume.determine_volume_unit(self.wall_primer_volume)
        print self.wall_primer_unit
        self.wall_finish_unit = volume.determine_volume_unit(self.wall_finish_volume)
        print self.wall_finish_unit

        self.ceiling_primer_volume = volume.find_paint_volume(self.ceiling_area, self.primer_coverage)
        self.ceiling_finish_volume = volume.find_paint_volume(self.ceiling_area, self.finish_coverage)


        self.ceiling_primer_unit = volume.determine_volume_unit(self.ceiling_primer_volume)
        self.ceiling_finish_unit = volume.determine_volume_unit(self.ceiling_finish_volume)
        print self.ceiling_primer_unit
        print self.ceiling_finish_unit
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
