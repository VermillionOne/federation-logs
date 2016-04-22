class Page(object):
    def __init__(self):

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

        self.form_body = '''
    <h2>Room Dimensions</h2>
    <p>
      Enter your room dimensions below to learn how much paint you'll need to get to complete the job!
    </p>

    <form action="index.html" method="get">
      <label for="name">Name</label> <input type="text" id="name" name="name" value="">
      <label for="length">Length<sup>*</sup></label> <input type="number" id="length" name="length" value="">
      <label for="width">Width<sup>*</sup></label> <input type="number" id="width" name="width" value="">
      <label for="height">Height<sup>*</sup></label> <input type="number" id="height" name="height" value="">
      <label for="ceiling"><input type="checkbox" id="ceiling" name="ceiling" value="true">Include ceiling area</label>
      <button type="submit" name="name">Calculate Paint</button>
      <p><sub><sup>*</sup>required</sub></p>
    </form>
        '''

        self.results_starting_tag = '''
    <section>
        '''

        self.basic_greeting = '''
      <p>Here are your results</p>
        '''
        self.personalized_greeting = '''
      <p>Hello, {self.user_name}! Here are your results</p>
        '''

        self.basic_results_body = '''
      <div class="area_holder">
        <h3>Wall Area</h3>
        <p>{self.wall_area} square feet.</p>
      </div>
      <h2>Amount of paint you'll need</h2>
      <h3>For your walls</h3>
      <p>{self.wall_primer_volume} of primer. </p>
      <p>{self.wall_finish_volume} of finish. </p>
    </section>
        '''

        self.extended_results_body = '''
    <section>
      <div class="area_holder">
        <h3>Wall Area</h3>
        <p>{self.wall_area} square feet.</p>
        <h3>Ceiling Area</h3>
        <p>{self.ceiling_area} square feet.</p>
      </div>
      <h2>Amount of paint you'll need</h2>
      <h3>For your walls</h3>
      <p>{self.wall_primer_volume} of primer. </p>
      <p>{self.wall_finish_volume} of finish. </p>

      <h3>For your ceiling:</h3>
      <p>{self.ceiling_primer_volume} of primer. </p>
      <p>{self.ceiling_finish_volume} of finish. </p>
    </section>
        '''

        self.footer = '''
  </div>
</body>
</html>
        '''
