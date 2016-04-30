# Timothy Castillo
# DWP1604 Section 01
# Dynamic Site Project
# April 27, 2016

# Import necessary assets
import webapp2
from page import Page, ContentPage
from data import Ship, ShipClass
from library import PageFinder
class MainHandler(webapp2.RequestHandler):
    def get(self):
        page = Page()
        content = ContentPage()
        ship = Ship()
        finder = PageFinder()
        ship_class = ShipClass()
        self.header = ship.header
        current_view = ''
        ship_data = []
        # if there has been a request
        if self.request.GET:
            new_view = self.request.GET['id']
            # try to turn the new_view variable into an integer
            try:
                ship_data = ship_class.ship_class_list[int(new_view)]
                # Define local variables/
                self.header = ship_data.header
                self.armaments = ship_data.armaments
                self.defenses = ship_data.defenses
                self.decks = ship_data.decks
                self.crew = ship_data.crew
                self.cruise_speed = ship_data.cruise_speed
                self.max_cruise_speed = ship_data.max_cruise_speed
                self.maximum_speed = ship_data.maximum_speed
                self.img_url = ship_data.img_url
                self.img_description = ship_data.img_description
                self.description = ship_data.description
            #if the new_view is not an integer
            except:
                # define ship data as default data
                ship_data = ship
                # Insert local variables

            # Define the current view from the new_view value
            current_view = finder.get_content_page(new_view)
            # current_view = current_view.format(**locals())
        else:
            # Grab main page concatenation
            current_view = page.print_main_page()


        # Insert local variables
        current_view = current_view.format(**locals())
        # Print page
        self.response.write(current_view)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
