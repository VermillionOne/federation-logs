''''
The following lines are to collect data for the number values
'''
number_1 = raw_input('Your favorite number  =>  ')
number_2 = raw_input('The worst number  =>  ')
minutes = raw_input('Pick a cool number greater than 30  =>  ')

'''
The Following lines are to collect string data
'''

noun_1 = raw_input('Your favorite food  =>  ')
verb_1 = raw_input('Gimme a Verb!  =>  ')
noun_2  =raw_input('Some sort of container type thing  =>  ')
adjective_1 = raw_input('A one word description of something  =>  ');

'''
The following line determines temperature value based on the first two numbers added together,
multiplied by the minutes value, and the result multiplied by ten
'''
temperature = (int(number_1) + int(number_2) * int(minutes)) * 10

'''
The following is the first part of the recipe
'''
recipe_heading = '''

{adjective_1} {noun_1} Casserole -

Here is a list of ingredients for the recipe:
'''

'''
Print the recipe_heading to the Console
'''
recipe_heading = recipe_heading.format(**locals())
print recipe_heading

'''
Create ingredients array
'''
ingredients = ['Turnips', 'Rigatoni', 'Mushrooms', 'Eggs', 'Salt', 'Pepper', 'Hotsauce']

'''
Print ingredients per line in console
'''
for i in ingredients:
    print i

'''
Create recipe_ending section
'''
recipe_ending = '''
If you have {number_1} {noun_1}, then you could make a {adjective_1} entree.
Whip {number_2} eggs in a bowl and {verb_1}, add the {noun_1} and other ingredients, and mix until the ingredients are fully incorporated together. Pour the ingredients evenly into a {noun_2}.

Set the oven to {temperature} and let bake for {minutes} minutes.

Remove when browned and let cool for 10 minutes.

Enjoy!
'''
'''
Print recipe_ending to the console
'''
recipe_ending = recipe_ending.format(**locals())
print recipe_ending
