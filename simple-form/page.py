class Page(object):
    def __init__(self):
        # Creating page sections using class attributes
        self.head = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Hikr | New User</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href='https://fonts.googleapis.com/css?family=Cabin:700,500,400' rel='stylesheet' type='text/css'>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.6.1/css/font-awesome.min.css">
    <link rel="stylesheet" href="{self.css}">
</head>
<body>
    <div class="container">
        <header class="main-header">
            <img src="img/hikr-logo.png" class="logo" alt="Hikr Logo" />
        '''
        self.head_2 = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Hikr | New User</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href='https://fonts.googleapis.com/css?family=Cabin:700,500,400' rel='stylesheet' type='text/css'>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.6.1/css/font-awesome.min.css">
    <link rel="stylesheet" href="{self.css}">
</head>
<body class="view-2">
    <div class="container">
        <header class="main-header">
            <img src="img/hikr-logo.png" class="logo" alt="Hikr Logo" />
        '''
        self.login_section = '''
            <div class="login">
                <i class="fa fa-sign-in" aria-hidden="true"></i>
            </div>
        '''
        self.user_section = '''
            <div class="user">
                {self.username} <i class="fa fa-user"></i>
            </div>
        '''
        self.form_body = '''
        </header>
        <section class="form-section">
            <h1>New User</h1>
            <form method="GET" class="">
                <label for="username">Username</label><input type="text" name="username" id="username">
                <label for="email">Email</label><input type="email" name="email" id="email">
                <label for="trail_name">Trail Name</label><input type="text" name="trail_name" id="trail_name">
                <label for="difficulty">Difficulty</label>
                <select class="" name="difficulty" id="difficulty">
                    <option value="easy">Easy</option>
                    <option value="moderate">Moderate</option>
                    <option value="difficult">Difficult</option>
                    <option value="extreme">Extreme</option>
                </select>
                <label for="miles_hiked">Miles Hiked</label><input type="text" name="miles_hiked" id="miles_hiked">
                <label for="time_hiked">Time Hiked</label><input type="text" name="time_hiked" id="time_hiked">
                <label>Your Trail Rating</label>
                <div class="rating-section">
                    <input type="radio" name="rating" value="1" id="rating1" ><label for="rating1">1</label>
                    <input type="radio" name="rating" value="2" id="rating2" ><label for="rating2">2</label>
                    <input type="radio" name="rating" value="3" id="rating3" ><label for="rating3">3</label>
                    <input type="radio" name="rating" value="4" id="rating4" ><label for="rating4">4</label>
                    <input type="radio" name="rating" value="5" id="rating5" ><label for="rating5">5</label>
                </div>
                <input class="submit-button" type="submit" value="Track Hike">
            </form>
        </section>
        '''
        self.tracking_body = '''
        </header>
        <section class="tracking_section">
            <header>
                <h2>Hikr Tracking</h2>
                <p>
                    {self.email}
                </p>
            </header>
            <div class="tracking-body">
                <article>
                    <h3 >{self.trail_name}</h3>
                    <p>Difficulty: {self.difficulty}</p>
                    <p>Miles: {self.miles_hiked} miles</p>
                    <p>Time: {self.time_hiked} hours</p>
                    <p>Rating: {self.rating}</p>
                </article>
            </div>
        </section>
        '''
        self.footer = '''
    </div>
</body>
</html>
        '''
    # Setting the printed section for the form page view
    def print_form(self):
        form_page = self.head + self.login_section + self.form_body + self.footer
        return form_page

    # Setting the printed section for the tracking page view
    def print_tracking(self):
        tracking_page = self.head_2 + self.user_section + self.tracking_body + self.footer
        return tracking_page
