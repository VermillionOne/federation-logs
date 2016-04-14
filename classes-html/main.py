
import webapp2
from index import Page

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()
        print p.print_out()
        self.response.write(p.print_out())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
