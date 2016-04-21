import webapp2
from library import RoomMeasurements, EvaluateArea
from page import Page
class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')
        self.wall_area = 0

        # Set classes for use in MainHandler
        room = RoomMeasurements()
        evaluate = EvaluateArea()

        room.length = 15
        room.width  = 9
        room.height = 17

        evaluate.include_ceiling = True

        self.wall_area = evaluate.find_wall_area(room.length, room.width, room.height)
        self.ceiling_area = evaluate.find_ceiling_area(room.length, room.width, evaluate.include_ceiling)
        print self.ceiling_area, "==> ceiling area"
        self.wall_primer_volume = evaluate.find_paint_volume(self.wall_area, 200)
        print self.wall_primer_volume
        self.wall_finish_volume = evaluate.find_paint_volume(self.wall_area, 350)
        print self.wall_finish_volume

        self.ceiling_primer_volume = evaluate.find_paint_volume(self.ceiling_area, 200)
        print self.ceiling_primer_volume
        self.ceiling_finish_volume = evaluate.find_paint_volume(self.ceiling_area, 350)
        print self.ceiling_finish_volume

        print self.wall_area
        print self.ceiling_area

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
