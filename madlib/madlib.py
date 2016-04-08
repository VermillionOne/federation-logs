
ingredients = ['Turnips', 'Rigatoni', 'Mushrooms', 'Eggs', 'Salt', 'Pepper', 'Hotsauce']

number_1 = raw_input('Your favorite number  =>  ')
number_2 = raw_input('The worst number  =>  ')
minutes = raw_input('Pick a cool number between 7 and 15  =>  ')

noun_1 = raw_input('Your favorite food  =>  ')
verb_1 = raw_input('Gimme a Verb!  =>  ')
noun_2  =raw_input('Some sort of container type thing  =>  ')
adjective_1 = raw_input('A one word description of something  =>  ');

temperature = (int(number_1) + int(number_2) * int(minutes)) * 10

print temperature

story = '''

{name_part_1} {name_part_1} Casserole -

Here is a list of ingredients for the recipe:

{ingredients}

If you have {number_1} {noun_1}, then you could make a {adjective_1} entree.
Whip {number_2} in a bowl and {verb_1}, add the {noun_1}, and mix until the ingredients are full incorporated together. Pour the ingredients evenly into a {noun_2}}.

Set the oven to {temperature} and let bake for {minutes} minutes.

Remove when browned and let sit for 10 minutes.

Enjoy!

'''
