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
        # Setting Attributes for calling stylesheet
        self.css = "css/app.css"
        # Setting Attributes for use in the request.GET
        self.username = ""
        self.email = ""
        self.trail_name = ""
        self.difficulty = ""
        self.miles_hiked = ""
        self.time_hiked = ""
        self.rating = ""
        # Accessing the Page class in page.py
        page = Page()

        if self.request.GET:
            # Storing input data into the respective variables
            self.username = self.request.GET['username']
            self.email = self.request.GET['email']
            self.trail_name = self.request.GET['trail_name']
            self.difficulty = self.request.GET['difficulty']
            self.miles_hiked = self.request.GET['miles_hiked']
            self.time_hiked = self.request.GET['time_hiked']
            self.rating = self.request.GET['rating']
            # Storing the print_tracking result into the tracking_page variable
            tracking_page = page.print_tracking()
            # Formatting the variables inside the page with the values received through the form
            tracking_page = tracking_page.format(**locals())
            # Printing the HTML onto the page
            self.response.write(tracking_page)
        else:
            # Storing the print_form result into the form_page variable
            form_page = page.print_form()
            # Formatting the CSS variable with the preset value
            form_page = form_page.format(**locals())
            # Printing the HTML onto the page
            self.response.write(form_page)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
