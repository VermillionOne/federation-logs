class Page(object):
    """docstring for Page"""
    def __init__(self):
        self.header = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Document</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">

  <script type="text/javascript" src="js/app.js"></script>

  <link href='https://fonts.googleapis.com/css?family=BenchNine:400,700' rel='stylesheet' type='text/css'>
  <link rel="stylesheet" href="css/app.css">
</head>
  <body>

    <header>

      <svg class="top-left" version="1.1" x="0px" y="0px" width="222px" height="84px">
        <path fill="#FF9900" d="M63.9,0C28.6,0,0,28.6,0,63.9V84h181v-5c0-17.1,13.9-31,31-31h10V0H63.9z"/>
      </svg>

      <div class="header-bar"></div>

      <h1 class="main-header">{self.header}</h1>

      <svg class="top-right" version="1.1" x="0px" y="0px" width="27px" height="48px">
        <path fill="#FF9900" d="M3,0H0v48h3c13.3,0,24-10.7,24-24v0C27,10.7,16.3,0,3,0z"/>
      </svg>

    </header>
        '''
        self.footer = '''

    <footer>
      <svg class="bottom-left" version="1.1" x="0px" y="0px" width="222px" height="43px">
        <path fill="#FF9900" d="M181,7V0H0v15.8C0,30.8,12.2,43,27.2,43H222V19h-29C186.4,19,181,13.6,181,7z"/>
      </svg>

      <div class="footer-bar"></div>

      <div class="bottom-right"></div>
    </footer>


  </body>
</html>
        '''

class ContentPage(Page):
    """docstring for ContentPage"""
    def __init__(self, arg):
        super(ContentPage, self).__init__()
        self.arg = arg
