
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()
        print p.print_out()
        self.response.write(p.print_out())


class Page(object):
    def __init__(self):
        self.title = "Welcome!"
        self.head = """
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>{self.title}</title>
    </head>
    <body>
        """

        self.body = "Welcome to me OOP Python Page"
        self.close = """
    </body>
</html>

        """

    def print_out(self):
        all = self.head + self.body + self.close
        all = all.format(**locals())
        return all

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
