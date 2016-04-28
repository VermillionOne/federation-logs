import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = FormPage()
        p.inputs = [['first_name', 'text', 'First Name'],['last_name', 'text', 'First Name'],['Submit', 'submit']]
        self.response.write(p.print_out_form())

class Page(object):
    def __init__(self):
        self._head = '''<!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <title>Document</title>
    </head>
    <body>
    '''
        self._body = '''
        <h1>Testing</h1>
        '''

        self._close = '''
    </body>
</html>
'''

    def print_out(self):
        return self.head + self.body + self.close

class FormPage(Page):
    def __init__(self):
        #constructor function for the super class
        super(FormPage, self).__init__() #Page.__init__()
        self._form_open = '<form method="GET">'
        self._form_close = '</form>'
        self.__inputs = []
        self._form_inputs = ''
        # <input type="text" value="" name="first_name" placeholder="First Name" />
        # ['First_name', 'text', 'First Name']
        # <input type="text" value="" name="last_name" placeholder="Last Name" />
        # <input type="submit" value="Submit" />

    @property
    def inputs():
        pass

    @inputs.setter
    def inputs(self, arr):
        # change my private inputs variable
        self.__inputs = arr
        # sort through the mega array and create HTML inputs based on the info there
        for item in arr:
            self._form_inputs += '<input type="' + item[1] + '" name="' + item[0]
            # if there is a third item, add it in
            try:
                self._form_inputs += '" placeholder="' + item[2] + '" />'
            # Otherwise, end the tag
            except:
                 self._form_inputs += '" />'

        print self._form_inputs

    def print_out_form(self):
        return self._head + self._body + self._form_open + self._form_inputs + self._form_close + self._close


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
