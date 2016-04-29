# Timothy Castillo
# DWP1604 Section 01
# Dynamic Site Project
# April 27, 2016

# Import necessary assets
import webapp2
from page import Page, ContentPage
from data import Ship, ShipClass

class MainHandler(webapp2.RequestHandler):
    def get(self):
        page = Page()
        ship - Ship()
        print ship
        if self.request.GET:
            pass
        else:
            self.main_page = page.print_main_page()

        self.response.write(self.main_page)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
