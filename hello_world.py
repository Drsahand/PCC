print ("Hello Python World")

message = "Hello Python World!"
print(message)

message = "Hello Python Crash Course world!"
print(message)

message = "Hello Python Crash Course world!"
print(mesge)

#know the different between variable (python main language) and value

periapical_radio = 'Periapical radiographs that uses in dentistry'
print(periapical_radio)

string = "everything inside quotes can be single or double quote"
print(string)

name = 'ada lovelace'
print(name.title())
print(name.upper())
print(name.lower())

first_name = 'sahand'
last_name = 'shirzadi maryan'
full_name = f"{first_name} {last_name}"
print(full_name)

print(f"Hello, {full_name.title()}")

print("\tPython")
print("Language:\n\tPyhton\n\tC\n\tJavaScript")

favorite_language =' python '
favorite_language = favorite_language.rstrip()
favorite_language
favorite_language = favorite_language.lstrip()
favorite_language = favorite_language.strip()
favorite_language

nostarch_url = 'https://nostarch.com'
nostarch_url.removeprefix('https://')
simple_url = nostarch_url.removeprefix('https:\\')
simple_url

message = "One of Python's strengths is its diverse community."
message

message = 'One of Python's strengths is its diverse community.'
#error becasue of apostoph should be differnt for string and inside text

name = 'Eric'

message = f"Hello {name}, would you like to learn some Python today?"
print(message)

name= "sahand"

print(name.title())
print(name.upper())

name = "Albert Eiinstein"

message = f'{name} once said,"A person who never made a mistake never tried anything"'
print(message)

quote = "A person who never made a mistake never tried anything new"
author = "Alvert Einstein"

print(f'{author} once said, "{quote}"')

name = " Nasim "
name.strip()

print('\tname')

filename = 'python_notes.txt'
filename.removesuffix('.txt')
#to rempve prefix and suffix

3 ** 3
2 + 2 - 1
0.2 + 0.1
4/2
# easy to distinguish 

universe_age = 14_000_000_000
#just to make eaier to read
universe_age

1000 == 10_00

x, y, z = 0, 0, 0
y

print(5+3)
print(2*4)
print(16/2)
print(10-2)

favorite_number = 12
message = "My favorite number always was" + str(favorite_number)
print(message)

import this

#lists 

# Always simple is better than complex moslty in Python 

# Lists all us to store sets of information in one place
# it is import to make name of the list pleural like letters

# we use [] to indicate the list, then we separate with '' each name in the list

bicycles = ['trek' , 'gitane' , 'overload']
print(bicycles)
print(bicycles[0])
print(bicycles[1].title())
# To capitalize

print(bicycles[-1])
# to show the last item

message = f"My first bicycle was a {bicycles[1].title()}."
#you cann use f-strings to create a message based on a value from a list 
print(message)

# ////Excercise
names = ['Mohammad' , 'Saeid' , 'Amin' , 'Soheil' , 'Sahand']
print(names[-1])
# ////Excercise
message = f"I love {names[-2]}."
print(message)
# ////Excercise
favorite_cars = ['bugatti', 'lamborginni' , 'bmw' , 'benz']
text = f"My favorite cars are {favorite_cars[0].title()} and {favorite_cars[1].title()}."
print(text)

# -----------------------------

# Modifying ELements in list

names = ['Sahand', 'Soheil' , 'Amin' , 'Nasim']
print (names)
names[0] = "Mohammad"
print(names)

# adding elements to the list, makes easy to create list sometmes like this
names.append('Saeid')
names.append("Behi")
names.append("Feri")

#inserting elements into a list, normally it adds to a location you want in the list
names.insert(5, 'Vahid')

#removing elements from list
del names[0]
del names [4]
print(names)

#Removing item using the pop() method
popped_names = names.pop()
print(names)
print(popped_names)
older_sister = names.pop()
print(f"My older sister is {older_sister.title()}.")

print(names)
names.append('sahand')
youngest = names.pop(0)


print(names)
names.remove('sahand')

names.append('sahand')

youngest = 'sahand'
names.remove(youngest)
print(f"Youngest person in our family is {youngest.title()}.")

#excersise1
invitation_list = ['mohammad' , 'saeid', 'nasim', 'amin']
message_mohammad = f"Dear {invitation_list[0].title()}, I am really happy and waiting for you tonight"
print(message_mohammad)

#exercise2
del invitation_list[1]
invitation_list.insert(3,'Feri')
print(invitation_list)

#exercise3
invitation_list.insert(0, 'Sahand')
invitation_list.insert(2, 'Soheil')
invitation_list.append('Behi')

#exercise4
message1 = f"You can invite only two people Mr. {invitation_list[0]}"
print(message1)
invitation_list.pop(1)
popped_list = invitation_list.pop(0)
message_pop = f"We are really sorry for lacking space Mr. {popped_list}"
print(message_pop)
del invitation_list[0-1]


#Sorting a List permanently with the sort() method
cars = ['bmw', 'benz', 'audi', 'lamborginni']
cars.sort()
#to sort alphabetically
print(cars)

cars.sort(reverse=True)

#Sort temporarely using sorted()
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list")
print(sorted(cars))

# reverse the list simple
print("\nHere is the original list again:")
print(cars)
cars.reverse()

#Finding the length of a list
len(cars)

#excersise1
locations = ['barcelona','vienna','talesh','budapest']
print(locations)
print(sorted(locations, reverse=True))

locations.reverse()
locations.sort()
locations.sort(reverse=True)
len(cars)

favorites = ['zurich', 'barcelona','lodnon', 'dublin']
favorites.append('talesh')
del favorites[1]
len(favorites)
favorites[-1]
favorites[5]

#summary 1. lists 2. define a list (add or remove or pop) 3. sort the list permanent or temporarily 4. lenths of list

# CHAPTER 4 

magicians = ['sahand', 'saeid', 'nasim']
for magician in magicians:
    print(magician)

magicians = ['sahand', 'saeid', 'nasim']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")

magicians = ['sahand', 'saeid', 'nasim']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I cant wait to see your next trick,{magician.title()}.\n")

magicians = ['sahand', 'saeid', 'nasim']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
print(f"I cant wait to see your next trick,{magician.title()}.\n")    
print("Thank you everyone. That was a great magic show.")

# Always remeber to indent after for in Loop, if you forget you get the indenterror
# if you indent accidently python with inform you with (unexpected indent)
# you will indent when you want to repeat some actions otherwise no nned 

#exersize1
pizzas = ['margareta','carbonara','fredi']
for pizza in pizzas:
    print(pizza)
    print("I like pizza\n")
print('I really love pizza')

#exercise2
animals = ['monkey','snake','rabit']
for animal in animals:
    print(animal)
    print(f"A {animal}, would be a great pet.")
print("What is common between these animals is all of  them have emotion, some how they show it")

#Using range() function

for value in range(10, 50):
    print(value)

#Using range() to make a list of numbers

numbers = list(range(1,10))
print(numbers)

odd_numbers = list(range(1,11,2))
print(odd_numbers)

squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)
print(squares)

squares = []
for value in range(1,11):
    squares.append(value**2)

print(squares)

#Simple statistic with a list of Numbers
digits = [1,2,3,4,5,6,7,8,9,0]
min(digits)
max(digits)
sum(digits)

#Comprehensions list

squares = [value**2 for value in range(1,11)]
print(squares)


#Excersises 4-3
for value in range(1,21):
 print(value)

#Excersises 4-4
for value in range (1,1000001):
    print(value)

#Excersises 4-5
numbers = (1-1000001)
min(numbers)
max(numbers)
sum(numbers)

numbers = list(range(1,1000001))
min(numbers)
max(numbers)
sum(numbers)

#Excersises 4-6
odd = list(range(1,21,2))
print(odd)

for number in range(1,21,2):
    print(number)

#Excersises 4-7
for number in range(3,30):
    multiple = number*3
    print(multiple)


for number in range(3, 31, 3):
    print(number)

#Excersises 4-8
for number in range(1,11):
    cube = number**3
    print(cube)

#Excersises 4-9
cube = [value**3 for value in range(1,11)]
print(cube)


#Slicing a list
players = ['sahand','soheil', 'amin','Mohmmd','nasim']
print(players[0:3])
print(players[:4])
print(players[1:])
print(players[-3:]) #last three

#Looping through slice
players = ['sahand','soheil', 'amin','Mohmmd','nasim']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

#Copying a list
my_foods = ['pizza','kebab','carrot cake','falafel']
friend_foods = my_foods[:]
print('My favorite foods are:')
print(friend_foods)

print('\nMy friends favorite foods are:')
print(friend_foods)

my_foods =['kebab','pizza','ghorme','macaroni']
friend_foods = my_foods[:]

my_foods.append('pasta')
print(my_foods)

print(f'My favorite foods are: \n{my_foods}')
print(f'My friends favorite foods are: \n{friend_foods}')

#Exercise 4-10
players = ['sahand','soheil', 'amin','Mohmmd','nasim']
print(players[:3])
print(players[1:3])
print('Three items from end of the list are:')
print(players[-3:])

#Exercise 4-11
pizzas = ['margareta','carbonara','fredi']
friend_pizzas = pizzas[:]
print(friend_pizzas)
pizzas.append('carbonara')
print(pizzas)
friend_pizzas.append('tomato')
print('My favorite pizzas are:')
for pizza in pizzas:
    print(pizza)

print('My friends favorite pizzas are:')
for friend_pizza in friend_pizzas:
    print(friend_pizza)

#Exercise 4-12
#“More Loops: All versions of foods.py in this section have avoided using for loops when printing, to save space. 
#Choose a version of foods.py, and write two for loops to print each list of foods.”

#Tuples, immutable list
#Defining tuple

dimensions = (200,50)
#we define dimensions in parenthesis instead of square brackets
print(dimensions[0])
print(dimensions[1])
dimensions[0] = 250
# as you see we cannot modify in tuple 


#Looping through all values in a Tuple
dimensions = (200,50)
for dimension in dimensions:
    print(dimension)

#Writing over a tuple
dimensions = (200,50)
print('Original diimensions:')
for dimension in dimensions:
    print(dimension)

dimensions = (400,100)
print('\nModified dimensions:')
for dimension in dimensions:
    print(dimension)

#Exercise 4-13
foods = ('rice', 'tomato', 'chicken', 'gel', 'pasta')
for food in foods:
    print(food)
foods[0]= ('rice')

new_menu = ('rice', 'tomato', 'chicken', 'gharpoz', 'pan')
for menu in new_menu:
    print (menu)


#Styling your code = there are guidielines that we need to use to become professional programmer
#The style guide (python enhancement proposal(PEP))
#Always write a code is easier to read than writing a code that is easier to write
#You can use tap button for indentation as it count four spaces
#each line shoud be less than 80 characters\
#Use blank line to differenatiate between sections

#Summary
#1. using list through a for loop 2. indentation to structure program 
#3. simple numerical list 4. how to slice a list and how to copy the list 
#5. Tuples that there isi degree of importance to dont let to change
#6. Style to make easy read

#CHAPTER 5

cars = ['audi', 'bmw','bez','samand']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

car = 'bmw'
car == 'bmw'

car = 'audi'
car == 'bmw'
# through two equals == we ask a question is value of a car equal to bmw?

# Equality is Case sensitive 

car = 'Audi'
car == 'audi' 

#we can can convert to lower case
car = 'Audi'
car.lower() == 'audi'
car # So here you see we dont change car name to lower case, it is just for test

#checking for inequality
requested_topping ='mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies")
#because this two value are not matched therfore Python returns True and executes this code

#Numerical Comparison
age = 18
age == 18

answer = 17
if answer !=42:
    print('That is not correct answer, please try again!')

age = 19
age < 21
age <= 21
age >21
age >=21

if age >=19:
    print('You are no more young')

#Checking Multiple Conditions
age_0 = 22
age_1 = 18
age_0 >= 21 and age_1 >= 21

age_1 = 22
(age_0 >= 21) and (age_1 >= 21) #with parenthesis to look nicer

#Using or to Check Multipe Conditions (even one of them is True prints True)
age_0 = 22
age_1 = 18
age_0 >= 21 or age_1 >= 21 #(even one of them is true it prints it)

#Checking wether a value is in the List
requested_toppings = ['mushrooms','onions','pineapple']
'mushrooms' in requested_toppings
'pepperoni' in requested_toppings

#Checking whether a value is Not in the list 
banned_users = ['andrew','david','sahand']
user = 'marie'
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish, so.")

#Boolean Expressions(another name for conditional test)
game_active = True
can_edit = False

#exercise 5-1
cars = ['bmw','samand','subaro','gt','lamborginni']
car = 'capra'
if car in cars:
    print(f"{car.title()}, SUV car that I like to have")
if car not in cars:
    print(f"I expected {car.title()} to be in my favorite cars.")

permitted_age = >=18
age = 17
if age >= 18:
    print('Welcome')
if age < 18:
    print('adios')

age_0 = 25
age_1 = 17
age_0 <= 30 and age_1 <= 30
age_0 >= 21 or age_1 >= 21

#exercise 5-2
car = 'BMW'

car == 'bmw'
car.lower() == 'bmw'

#if Statements
if conditional_test:
    do something

#if the conditional test evaluates to True, Python executes the code following the if statement
#if the conditional test evaluate to False, Python ignores the code following the if statement

age = 19
if age >= 18:
    print("You are old enough to vote")
    print("Have you registered to vote yet?")

#if-else Statements (else statement allows you to define an action or set of actions that are executed when the conditional test fails)
age = 17
if age >= 18:
    print("You are old enough to vote")
    print('Have you registered to vote yet?')
else:
    print("Sorry, you are too young to vote.")
    print("PLease register to vote as soon as you get 18")


#if-elif-else Chain (for more than two possible situations)
#admission for anyone under age 4 is free
#admission for anyone between the ages of 4 and 18 is 25$
#admission for anyone more than 18 40$

age = 12 
if age <4:
    print("Your admission cost is 0$")
elif age <18:
    print("Your admission cost is 25$")
else:
    print("your admission const is 40$")

#Use Multiple elif Blocks
age = 19

if age <4:
    price = 0
elif age <18:
    price = 25
elif age <65:
    price = 40
else:
    price = 20

print(f"Your admission cost is ${price}.")

#Omitting the else Block (sometimes you dont need else, you can just continue with elif)

age = 12
if age <4:
    price = 0
elif age <18:
    price = 25
elif age <65:
    price = 40
elif age >65:#here you see it is clearer to use elif than else
    price = 20
print(f"Your admission cost is ${price}.")

#Testing Multiple Conditions

requested_toppings = ['mushrooms','chicken']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms")
if 'pepperoni' in requested_toppings: #no matter of elif Python tests if it passes correctly or not
    print("Adding pepperoni")
if 'chicken' in requested_toppings:
    print("Adding chicken")
print("\nFinished making your pizza!")
# with if-elif-else would not work this code, becasuse would stop after only one test passes

requested_toppings = ['mushrooms','chicken']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms")
elif 'pepperoni' in requested_toppings: #no matter of elif Python tests if it passes correctly or not
    print("Adding pepperoni")
elif 'chicken' in requested_toppings:
    print("Adding chicken")
print("\nFinished making your pizza!")

#SUMMARY if you want one block of code to run, use an if-elif-else chain, if more than one block of code needs to run, use a series of indepedent if statement

#EXERCISE 5-3
alien_color = ['green','yellow']
if 'green' in alien_color:
    print("Player just earned 5 points")

if 'red' in alien_color:
    print("Player just earned 5 points")
else:
    print("PLayer lost his mind, adios")

#EXERCISE 5-4
if 'green' in alien_color:
    print("Player got 5 point for shooting")
else:
    print("Player earned 5 points for shooting the alien")

#EXERCISE 5-5
if 'green' in alien_color:
    print("Player earned 5 points")
elif 'yellow' in alien_color:
    print("Player earned 10 points")
else:
    print("Player earned 15 points")

#EXERCISE 5-6
age = 1
if age < 2:
    print("Baby")
elif age < 4:
    print("Toddler")
elif age < 13:
    print("Kid")
elif age < 20:
    print("Teenager")
elif age < 65:
    print("Adult")
else:
    print("elder")

#EXERCISE 5-7
favorite_fruits = ['orange','apple','limon']
if 'orange' in favorite_fruits:
    print(f"I really like {favorite_fruits[0]} ")
if 'apple' in favorite_fruits:
    print(f"{favorite_fruits[1]}, is so yummy")


#Checking for Special items

requested_toppings = ['mushrooms','green peppers','chicken']
for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}")
print("\nFinished making your pizza")

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now")
    else:
        print(f"Adding{requested_topping}")
print("\nFinished making your pizza!")


#Checking That a List Is Not Empty
requested_toppings = [] #Python return to True if the list contains at least one item; an empty list evaluates to False
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

#Using Multiple List
available_toppings = ['mushrooms','olives','green peppers', 'pepperoni','pineaplle','extra cheese']
requested_toppings = ['mushrooms','french fries','extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we dont have {requested_topping}.")
print("\nFinished making your pizza")


#EXERCISE 5-8
usernames = ['admin','sahand','soheil','saeid','amin']

for username in usernames:
    if username == "admin":
        print(f"Hello Mr {username.title()}, We are very welcoming you!")
    if username in usernames:
        print(f"Hey {username}, welcome to your website")

#EXERCISE 5-9
usernames = []
if username == "admin":
        print(f"Hello Mr {username.title()}, We are very welcoming you!")
if username in usernames:
        print(f"Hey {username}, welcome to your website")
else:
        print('No username')

#EXERCISE 5-10
current_usernames = ['sahand','admin','nasim','shirin','ss2']
new_usernames = ['feri','sahand','behi','nasim','soheil']

for new_username in new_usernames:
    if new_username in current_usernames:
        print(f"Sorry {new_username.title()}, this username is choosen by others, try new")
    else:
        print(f"{new_username} This username is valid")

#EXERCISE 5-11
numbers = 1,2,3,4,5,6,7,8,9

for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")
#according to PEP 8 use single space around comparison like if age < 4: better than if age<4:

#SUMMARY
#1. how to write conditional test (which evaluate True or False) 2. How to write somple if statement(if-else and if-elif-else chain)
#3. to handle certain items in a list differently than all other iitems while continuing to utiliize the effiiciency oof a for looop
#4. Python style recommendations

#CHAPTER 6

#A Simple Dictionary

alien_0 = {'color': 'green','points':5 }
print(alien_0['color'])
print(alien_0['points'])

#Working with Dictionsries
#in Python dictionary wraps in braces{ with a series of key-value pairs inside the braces}
#The simplest dictioanry has exactly one key-value pair, as shwon in this modified version of the aalien_0
alien_0 = {'color': 'green'} #string 'color' is a key in this dictionary, and it is associated value is 'green'

#Accessign Value in a Dictionary 
alien_0 = {'color': 'green'}
print(alien_0['color'])

alien_0 = {'color': 'green','points':5 }

new_points = alien_0['points']
print(f"You just earned {new_points} points!")

#Adding New Key-Value Pairs
alien_0 = {'color': 'green','points':5 }
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

#Starting with an Empty Dictionary
alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

#Modifying Values in a Dictionary
alien_0 = {'color':'green'}
print(f"The alien is {alien_0['color']}")

alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}")



alien_0 = {'x_position': 0, 'y_position': 25, 'speed':'medium' }
print(f"Original position: {alien_0['x_position']}")
# Move the alien to the right
# Determine how far to move the alien based on its current
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien
    x_increment = 3
#This new position is the old position plus the increment 

alien_0['x_position'] = alien_0['x_position'] + x_increment 

print(f"New position: {alien_0['x_position']}")


alien_0 = {'x_position': 0, 'y_position': 25, 'speed':'medium' }
alien_0['speed'] = 'fast'
print(f"Original position: {alien_0['x_position']}")
# Move the alien to the right
# Determine how far to move the alien based on its current
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien
    x_increment = 3
#This new position is the old position plus the increment 

alien_0['x_position'] = alien_0['x_position'] + x_increment 

print(f"New position: {alien_0['x_position']}")

#Removing Key-Value Pair (to remove information that stored in a dictionary (del statement))
alien_0 = {'color': 'green','points':5 }
print(alien_0)

del alien_0['points']
print(alien_0)

#Dictionary of Similar Objects
favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'édward': 'rust',
    'phil' : 'python',
}
print(favorite_language)
favorite_language['jen']

language = favorite_language['sarah'].title()
print(f"Sarah's favorite language is {language}")

#Using get() to Access Values
alien_0 = {'color': 'green', 'speed': 'slow'}
print(alien_0['points'])# you will get the error because we dont have this key

point_value = alien_0.get('points', 'No point value ssigned.')
print(point_value)

#EXERCISE 6-1
sahand = {'first_name':'sahand', 'last_name':'shirzadi', 'age':'27', 'city':'talesh'}
print(sahand['first_name'])
print(sahand['last_name'])
print(sahand['age'])

#EXERCISE 6-2
favorite_number = {
    'sahand':12,
    'soheil':22,
    'nasim':2,
    'amin':4,
    'feri':14
}
print(favorite_number['sahand'])
for person, number in favorite_number.items():
    print(person + "'s favorite number is", number)

#EXERCISE 6-3
glossary = {
    'command': 'after each part',
    'dictionary':'to save meaning of the word in keys',
    'highligher':'to highlight each section',
    'modifying values': 'to modify each value in a section',
    'math': 'to calculate each section'
}
for word, meaning in glossary.items():
    print(word+ ':')
    print(meaning + '\n')

#Looping Through a Dictionary
#you can loop through all of a dicionary's key value pairs

user_0 = {
    'username': 'sahandshzd',
    'first': 'sahand',
    'last': 'shirzadi'
}

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")


favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil' : 'python',
}

for name, language in favorite_language.items():
    print(f"\n{name.title()}'s favoorite language is {language.title()}")

#Looping Through All the Keys in a Dictionary
for name in favorite_language.keys(): # with .key makes easier to read but both are same
    print(name.title()) #This for loop tells python to pull all the keys from the dictionary favorite_languages

#for the first line you can use also
for name in favorite_language: 
    print(name.title())

friends = ['phil', 'sarah']

for name in favorite_language.keys():
    print(f"Hi {name.title()}.")

    if name in friends: 
        language = favorite_language[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

    if 'erin' not in favorite_language.keys():
        print("Erin, please take out poll")

#Loopinig Through a Dictionary's Keys in a Particular Order
for name in sorted(favorite_language.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

#Looping Through All Values ini a Dictionary

favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil' : 'python',
}

print("The following languages have been mentioned")
for language in favorite_language.values(): #.keys referes to names, .value referes to languages
    print(language.title())

#EXERCISE 6-4
glossary = {
    'command': 'after each part',
    'dictionary':'to save meaning of the word in keys',
    'highligher':'to highlight each section',
    'modifying values': 'to modify each value in a section',
    'math': 'to calculate each section'
}
del glossary['command']
print(glossary)

for key, value in glossary.items():
    print(key)
for meaning in glossary.values():
    print(meaning)
for words in sorted(glossary.keys()):
    print(words)

    
glossary['keys'] = 'dictionary with words'
glossary['values'] = 'meaning of dictionaries'
glossary['dek'] = 'you can use this function to remove item'
glossary['list'] = 'when you want to prepare list of items'
glossary['sorted'] = 'you can use this function to sort item alphabeticallly'

print(glossary)

for word, meaning in glossary.items():
    print(word + ':')
    print(meaning + '\n')

#EXERCISE 6-5:
rivers = {
    'iran':'aras',
    'hungary': 'danub',
    'egypt': 'nile',
    'slovaki': 'danub',
    'austria': 'danube'
}

for country, river in rivers.items():
    print(f"The {river.title()}, passes through {country}")

for river in rivers.values():
    print(river)
for country in rivers.keys():
    print(country.title())

#EXERCISE 6-6: Polling
favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil' : 'python',
}

people_to_poll = ['jen', 'sahand', 'phil', 'soheil']

for person in people_to_poll:
    if person in favorite_language:
        print(f"Thank you for registering the poll, you already in, {person}")
    
    if  person not in favorite_language:
        print(f"Hey {person}, you already are not registered in the poll first for and register")


#Nesting ( Youcan nest dictionaries inside a list, a list of items inside a diictionart or even diciotnary iinside another dictionary)

#A list of Dictionaries 
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points':10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)
# Make an empty list for storing alieins
aliens = []

# Make 30 green aliens
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed':'slow'}
    aliens.append(new_alien)

# Show the first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")

# Show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}")


#NEW CODE AGAIN
# Make an empty list for storing aliens.
aliens = []
#make 30 green aliens
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed':'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
#show the first 5 aliens
for alien in aliens[:5]:
    print(alien)

for alien in aliens[4:6]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

for alien in aliens:
    print(alien)

# A list of Dictionaries 

# Store informatio about pizza being ordered

pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra chease']} 
#summorize the order 
print(f"You ordered a {pizza['crust']}-crust pizza "
      "with the following toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")

favorite_languages = {
    'jen': ['python','rust'],
    'soheil': ['python','c++'],
    'sahand': ['python'],
    'phil':['go']
}
for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")

    for language in languages:
        print(f"\t{language.title()}")

# A Dictionary in a Dictionary

users = {
    'aeinstein':{
        'first':'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}
for username, user_info in users.items():
    print(f"\nUsername: {username} ")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")

#EXERCISE 6.7
sahand = {'first_name':'sahand', 'last_name':'shirzadi', 'age':'27', 'city':'talesh'}
print(sahand['first_name'])
print(sahand['last_name'])
print(sahand['age'])

people = {
    'sahandshzd':{
        'first': 'sahand',
        'last': 'shirzadi',
        'age': 27, 
        'city': 'talesh'
    },
    'soheilshzd':{
        'first': 'soheil',
        'last': 'shirzadi',
        'age': 29, 
        'city': 'talesh'
    },
    'nasimshzd':{
        'first': 'nasim',
        'last': 'shirzadi',
        'age': 34, 
        'city': 'barcelona'
    }
}
for username, user_info in people.items():
    print(f"\tUsername: {username}")
    full_name = f"{user_info ['first']} {user_info['last']}"
    location = f"{user_info['city']}"
    ages = f"{user_info['age']}"

    print(f"{full_name}")
    print(f"From {location}")
    print(f"{ages} years old")

#EXERCISE 6-8

pets = {
    'rabit':{
        'name': 'julia',
        'owner': 'ari',
    },
    'dog':{
        'name': 'saymaz',
        'owner': 'soheil',
    },
    'toti':{
        'name': 'shosho',
        'owner': 'nasim',
    }
}

for pet, pet_info in pets.items():
    print(f"\nPet: {pet}")
    pet_name = f"{pet_info['name']}"
    pet_owner = f"{pet_info['owner']}"

    print(f"\tPet Name: {pet_name.title()}")
    print(f"\tPet Owner: {pet_owner.title()}")

#EXERCISE 6-9

favorite_places = {
    'sahand': {
        'talesh',
        'barcelona',
        'budapest'
    },
    'nasim': {
        'talesh',
        'rasht',
        'barcelona'
    },
    'soheil': {
        'rasht',
        'barcelona'
    }
}

for names, places in favorite_places.items():
    print(f"Hey {names.title()}, tell me what are your favorite places?")
    favorite = f"{places}"
    
    print(f"\tOh, thank you for asking my favorite places are: {favorite}")

#EXERCISE 6-10

favorite_numbers = {
    'sahand': {
        1, 2, 3
    },
    'soheil':{
        22, 25, 28 
    },
    'nasim': {
        2, 1,  13, 23
    }
}

for name, numbers in favorite_numbers.items():
    print(f"\tNames: {name.title()}")
    fav_numbers = f"{numbers}"

    print(f"Favorite Numbers: {fav_numbers}")

#EXERCISE 6-11

cities = {
    'barcelona': {
        'country': 'spain',
        'population':40000000,
        'fact': 'touritic city'
    },

    'budapest': {
        'country': 'hungary',
        'population':10000000,
        'fact': 'nice to visit'
    },
    'talesh': {
        'country': 'iran',
        'population':80000000,
        'fact': 'historic city'
    }
}

for city, city_info in cities.items():
    print(f"\nCity: {city}")

    country = f"{city_info['country']}"
    populations = f"{city_info['population']}"
    facts = f"{city_info['fact']}"

    print(f"\tCountry: {country}")
    print(f"\tPopulation: {populations}")
    print(f"\tfacts: {facts}")

    #EXERCISE 6-12


#SUMMARY
#define a dictionary and how to work with the information stored in a dictionary. 
# You learned how to access and modify individual elements in a dictionary, and
#  how to loop through all of the information in a dictionary. 
# You learned to loop through a dictionary’s key-value pairs, its keys, and its values. 
# You also learned how to nest multiple dictionaries in a list, nest lists in a dictionary, and 
# nest a dictionary inside a dictionary.

#CHAPTER 7 USER INPUT AND WHILE LOOPS

#How the input() Function Works
message = input("Tell me something, and I will repat it back to you: ")
print(message)
