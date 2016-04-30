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
        content = ContentPage()
        ship = Ship()
        ship_class = ShipClass()
        self.header = ship.header
        current_view = ''
        ship_data = []
        # if there has been a request
        if self.request.GET:
            new_view = self.request.GET['id']

            if new_view == '0':
                print new_view
                # Grab sovereign page concatenation
                current_view = content.print_sovereign_page()
                # Get Data for ship class
                ship_data = ship_class.ship_class_list[int(new_view)]
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
                # Insert local variables
                current_view = current_view.format(**locals())

            #if the response yields galaxy
            elif new_view == '1':
                print new_view
                # Grab sovereign page concatenation
                current_view = content.print_galaxy_page()
                # Get Data for ship class
                ship_data = ship_class.ship_class_list[int(new_view)]
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
                # Insert local variables

                current_view = current_view.format(**locals())

            #if the response yields excelsior
            elif new_view == '2':
                print new_view
                # Grab sovereign page concatenation
                current_view = content.print_excelsior_page()
                # Get Data for ship class
                ship_data = ship_class.ship_class_list[int(new_view)]
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
                # Insert local variables
                current_view = current_view.format(**locals())

            #if the response yields constitution
            elif new_view == '3':
                print new_view
                # Grab sovereign page concatenation
                current_view = content.print_constitution_page()
                # Get Data for ship class
                ship_data = ship_class.ship_class_list[int(new_view)]
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
                # Insert local variables
                current_view = current_view.format(**locals())

            #if the response yields intrepid
            elif new_view == '4':
                print new_view
                # Grab sovereign page concatenation
                current_view = content.print_intrepid_page()
                # Get Data for ship class
                ship_data = ship_class.ship_class_list[int(new_view)]
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
                # Insert local variables
                current_view = current_view.format(**locals())

            elif new_view == 'main':
                # Grab main page concatenation
                current_view = page.print_main_page()
                # change data back to main page
                ship_data = ship
                # Insert local variables
                current_view = current_view.format(**locals())

        #if the response yields anything else
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
