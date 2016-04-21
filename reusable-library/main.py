import webapp2
from library import RoomMeasurements
from page import Page
class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
