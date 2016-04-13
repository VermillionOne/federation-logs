class Page(object):
    def __init__(self):
        self.title = "Welcome!"
        self.css = "css/app.css"
        self.head = """
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>{self.title}</title>

        <link rel="stylesheet" type="text/css" href="{self.css}" />
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
