# one line comments lika soooo

'''
Doc strings
'''

first_name = 'Kermit'
last_name = ' de Frog'

# response = raw_input("Enter Your Name:   ")
# print 'Hello ' + response

birth_year = 1988
current_year = 2016
age = current_year - birth_year
# print 'You are ' + str(age) + ' years old.'

# budget = raw_input('Enter your budget:   ')
budget = 1;
# budget = int(budget)

if budget > 100:
    pass
    # brand = 'nike'
    # print 'Yay! we can buy ' + brand + ' shoes!'
elif budget > 50:
    pass
    # print 'At least I can get some nice sneakers'
else:
    pass
    # print 'Darn! I can\'t get cool shoes...'

# characters = ['Luke', 'Leia', 'Han', 'Chewy']
# characters.append('Obi Wan')
# # print characters
#
# movies = dict() # creating movies dictionary
# movies = {'Star Wars':'Darth Vader', 'Silence of the Lambs':'Hannibal Lecter'}
#
# print movies['Star Wars']

'''
While Loop
'''

#
# i = 0
# while i<9:
#     print "The count is at ", i
#     i += 1

'''
For Loop
'''
# i = 0
# for i in range(0,9):
#     print 'The count is ', i
#     i += 1


'''
For Each Loop
'''

# weapons = ['Lightsabers', 'Bat\'leths', 'Sting']
# for w in weapons:
#     print 'A great weapon in fiction is ' + w


'''
Functions
'''

# def calcArea(h, w):
#     area = h * w
#     return area
#
# a = calcArea(20, 40);
#
# print 'My area is ' + str(a) + ' sq. ft.'
#



'''
Strings and variables
'''

title = 'Testing Python String Variables'
body = 'Hello, World!'
html_doc = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>{title}</title>
</head>
<body>
  {body}
</body>
</html>
'''

html_doc = html_doc.format(**locals())
print html_doc
