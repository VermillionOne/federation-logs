class Page(object):
    def __init__(self):
        # Head section of HTML
        self.head = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Paint Calculator</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link href='https://fonts.googleapis.com/css?family=Comfortaa:400,300,700' rel='stylesheet' type='text/css'>
  <link rel="stylesheet" href="css/app.css">
</head>
<body>

  <header>
      <h1>Paint Calculator</h1>
      <img src="img/paint-bucket.png" alt="paint bucket" />
  </header>

  <div class="container">
        '''
        # Form Section of HTML
        self.form_body = '''
    <h2>Room Dimensions</h2>
    <p>
      Enter your room dimensions below to learn how much paint you'll need to get to complete the job!
    </p>

    <form method="get">
      <label for="name">Name</label> <input type="text" id="name" name="name" value="">
      <label for="length">Length<sup>*</sup></label> <input type="number" id="length" name="length" value="">
      <label for="width">Width<sup>*</sup></label> <input type="number" id="width" name="width" value="">
      <label for="height">Height<sup>*</sup></label> <input type="number" id="height" name="height" value="">
      <button type="submit">Calculate Paint</button>
      <p><sub><sup>*</sup>required</sub></p>
    </form>
        '''
        # Beginning Tag for Results section due to variance in greeting
        self.results_starting_tag = '''
    <section>
        '''
        # Basic Greeting omitting user name local variable
        self.basic_greeting = '''
      <h2>Here are your results</h2>
        '''
        # Personalized greeting including user name local variable
        self.personalized_greeting = '''
      <h2>Hello, {self.user_name}! Here are your results</h2>
        '''
        # Results body with area and paint volume results
        self.results_body = '''
    <section>
      <div class="area_holder">
        <h3>Wall Area</h3>
        <p>{self.wall_area} square feet.</p>
        <h3>Ceiling Area</h3>
        <p>{self.ceiling_area} square feet.</p>
      </div>
      <h2>Amount of paint you'll need</h2>
      <h3>For your walls</h3>
      <p>{self.wall_primer_unit} of primer. </p>
      <p>{self.wall_finish_unit} of finish. </p>

      <h3>For your ceiling:</h3>
      <p>{self.ceiling_primer_unit} of primer. </p>
      <p>{self.ceiling_finish_unit} of finish. </p>
    </section>
        '''
        # Closing of tags from head section
        self.footer = '''
  </div>
</body>
</html>
        '''

    '''
    compile_form function
    '''
    def compile_form(self):
        # Return sections necessary for form section
        return self.head + self.form_body + self.footer

    '''
    compile_results function
        Arguments accepted:
            self.user_name
                |-> name
    '''
    def compile_results(self, name):
        # if the user name variable is not empty
        if name != '':
            # Return with personalized_greeting included
            return self.head + self.results_starting_tag + self.personalized_greeting + self.results_body + self.footer
        else:
            # Otherwise, return with basic_greeting included instead
            return self.head + self.results_starting_tag + self.basic_greeting + self.results_body + self.footer
