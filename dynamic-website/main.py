# Timothy Castillo
# DWP1604 Section 01
# Dynamic Site Project
# April 27, 2016

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
