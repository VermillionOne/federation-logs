'''
Timothy Castillo
April 14, 2016
DWP 1604
Simple Form
'''
import webapp2
from page import Page
class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
