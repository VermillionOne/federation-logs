'''
Timothy Castillo
April 14, 2016
DWP 1604
Simple form
'''

import webapp2 # Use the webapp2 library
from page_sections import Section
class MainHandler(webapp2.RequestHandler): # declaring a class
    def get(self): # function that gets everything: Catalyst
        page_head = '''<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Document</title>
    </head>
    <body>
        '''
        page_body = '''
        <h1>Hello, World!</h1>

        <form method="GET">
            <label for="username">Username: </label>
            <input type="text" id="username" name="username"/>
            <label for="email" >Email: </label>
            <input type="text" id="email" name="email"/>
            <input type="submit" value="Submit">
        </form>
        '''
        page_close = '''
    </body>
</html>
        '''
        # self.request.GET
        if self.request.GET:
            # Stores the input data into respective variables
            username = self.request.GET['username']
            print self.request.GET['username']
            email = self.request.GET['email']
            print self.request.GET['email']
            self.response.write(page_head + username +  " "  + email + page_body + page_close) # Printing onto the page
        else:

            self.response.write(page_head + page_body + page_close) # Printing onto the page
        # code goes here

    def additional_functions(self):
        pass
        # code goes here

# don't touch this code for now
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
