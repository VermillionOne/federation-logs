class Page(object):
    """docstring for Page"""
    def __init__(self):
        # Header section for the main page template
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
        # Sidebar section for the sovereign class
        self.aside = '''
    <aside class="main-menu">
      <ul>
        <li><a href="?id=main">Main</a></li>
        '''
        # Menu element to select Sovereign class
        self.aside_sovereign = '''
        <li><a href="?id=sovereign">Sovereign</a></li>
        '''
        # Menu element to select Galaxy class
        self.aside_galaxy = '''
        <li><a href="?id=galaxy">Galaxy</a></li>
        '''
        # Menu element to select Excelsior class
        self.aside_excelsior = '''
        <li><a href="?id=excelsior">Excelsior</a></li>
        '''
        # Menu element to select Constitution class
        self.aside_constitution = '''
        <li><a href="?id=constitution">Constitution</a></li>
        '''
        # Menu element to select Intrepid class
        self.aside_intrepid = '''
        <li><a href="?id=intrepid">Intrepid</a></li>
        '''
        # Menu element to close side bar
        self.aside_close = '''
      </ul>
      <div class="side-bar"></div>
    </aside>
        '''
        # Menu element to show active class
        self.aside_active = '''<p class="active-block"></p>'''
        # Main body section for the main page template
        self.body = '''
    <section>

      <img class="federation-logo" src="img/federation-logo.png" alt="United Federation of Planets Insignia" />

      <h2>
        Starfleet Starship Database
      </h2>

    </section>
        '''
        # Footer section for the main page template
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

    def print_main_page(self):
        return self.header + self.aside + self.aside_active + self.aside_sovereign + self.aside_galaxy + self.aside_excelsior + self.aside_constitution + self.aside_intrepid + self.aside_close + self.body + self.footer

class ContentPage(Page):
    #docstring for ContentPage
    def __init__(self, arg):
        super(ContentPage, self).__init__()

        self.body = '''
    <section>

      <dl>
        <dt>Name:</dt>
          <dd>{self.name}</dd>
        <dt>Class:</dt>
          <dd>{self.class}</dd>
        <dt>Armaments:</dt>
          <dd>{self.armaments}</dd>
        <dt>Decks:</dt>
          <dd>{self.decks}</dd>
        <dt>Crew:</dt>
          <dd>{self.crew}</dd>
        <dt>Cruising Speed:</dt>
          <dd>{self.cruise_speed}</dd>
        <dt>Max Cruising Speed:</dt>
          <dd>{self.max_cruise_speed}</dd>
        <dt>Maximum Speed:</dt>
          <dd>{self.maximum_speed}</dd>
      </dl>

      <img src="{self.img_url}" alt="{self.img_description}" />

      <p class="description">
        {self.description}
      </p>


    </section>
        '''
