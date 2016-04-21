import webapp2
from library import RoomMeasurements, EvaluateArea, EvaluateVolume
from page import Page
class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')
        self.wall_area = 0

        # Set classes for use in MainHandler
        room = RoomMeasurements()
        area = EvaluateArea()
        volume = EvaluateVolume()

        room.length = 15
        room.width  = 9
        room.height = 17

        area.include_ceiling = True

        self.wall_area = area.find_wall_area(room.length, room.width, room.height)
        self.ceiling_area = area.find_ceiling_area(room.length, room.width)
        print self.ceiling_area, "==> ceiling area"
        self.wall_primer_volume = volume.find_paint_volume(self.wall_area, 200)
        print self.wall_primer_volume
        self.wall_finish_volume = volume.find_paint_volume(self.wall_area, 350)
        print self.wall_finish_volume

        self.wall_primer_unit = volume.determine_volume_unit(self.wall_primer_volume)
        print self.wall_primer_unit
        self.wall_finish_unit = volume.determine_volume_unit(self.wall_finish_volume)
        print self.wall_finish_unit

        self.ceiling_primer_volume = volume.find_paint_volume(self.ceiling_area, 200)
        print self.ceiling_primer_volume, "self.ceiling_primer_volume"
        self.ceiling_finish_volume = volume.find_paint_volume(self.ceiling_area, 350)
        print self.ceiling_finish_volume

        self.ceiling_primer_unit = volume.determine_volume_unit(self.ceiling_primer_volume)
        print self.ceiling_primer_unit, "Ceiling Primer Volume"
        self.ceiling_finish_unit = volume.determine_volume_unit(self.ceiling_finish_volume)
        print self.ceiling_finish_unit, "Ceiling Finish Volume"

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
