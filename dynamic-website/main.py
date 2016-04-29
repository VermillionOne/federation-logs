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
        ship = ShipClass()
        self.header = ship.header

        if self.request.GET:
            pass
        else:
            # Grab main page concatenation
            current_view = page.print_main_page()
            # Insert local variables
            current_view = current_view.format(**locals())
        # Print
        self.response.write(current_view)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
