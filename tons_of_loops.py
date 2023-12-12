
def add_numbers(x, y):
      return x + y
  

def multiply(a, b):
      return a * b
  

multiply(4, 5)
# 20
add_numbers(1, 2479)
# 2480

  ## using string formatting to get more fancy
  print(f"Michael Phelps eats {multiply(10, 1000)} per day so he maintains his weight")
# Michael Phelps eats 10000 per day so he maintains his weight
  print(f"Michael Phelps eats {multiply(10, 1000)} calories  per day so he maintains his weight")
# Michael Phelps eats 10000 calories  per day so he maintains his weight

  x = 12
  y = 13
      
def add_numbers(x, y):
    print(f"Inside the function, x = {x} and y = {y}")
    return x + y
  
    print(f"outside the function, x = {x} and y = {y}")
# outside the function, x = 12 and y = 13
    print(f"The sum of 5 and 6 is {add_numbers(5, 6)}")
# Inside the function, x = 5 and y = 6
# The sum of 5 and 6 is 11

# NUMBER OF ARGUMENTS MATTER

# ALSO BE CAREFUL ABOUT INDENTS

def add(x,y):
    return x + y
  
add(59, 1)
# 60
add(1, 2, 3)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: add() takes 2 positional arguments but 3 were given
add(1,2)
#   File "<stdin>", line 1
add(1,2)
# IndentationError: unexpected indent

def add(x, y, operation='add')
#   File "<stdin>", line 1
def add(x, y, operation='add')
                                  ^
# SyntaxError: expected ':'
def add(x, y, operation='add'):
      if operation == 'add':
              return x + y
      else:
              return x - y
add(5, 3)
#   File "<stdin>", line 6
add(5, 3)
    ^^^
# SyntaxError: invalid syntax
add(5,3)
# 8
add(5, 3, operation='add')

add(5, 3, operation='foo')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: add() got an unexpected keyword argument 'operation'

# FIRST SIX OPERATORS TEST OBJECT'S VALUE; firs six operators test objects value. first six operators test objects value  'is' and 'is not' test whether two objects are the same thing; 

# useful for singletons such as None and False

# None, True, and False are when you want to use the 'is' keyword b/c we're not comparing two different values; wanna make sure the singleton is what that variable is pointing at;

 5 < 3 == True
# False

5<3
# False
3<5
# True

def calculate_nums(x, y, operation="add"):
      if operation == "add":
              return x + y
      elif operation == "subtract":
              return x - y
  
  #testing new function; default is 'add' if we do not pass in keyword argument
calculate_nums(4, 3)
# 7
calculate_nums(4, 21)
# 25
calculate_nums(4, 21, operation="subtract")
# -17

10 > 10
# False
10 >= 10
# True
5 != 10
# True
5 == True
# False
if 5:
    print("number 5 is truthy")
  
# number 5 is truthy
  # number 5 is truthy for an if test!

# true or false can be represented by 1 or 0. true can be represented as 1 and false as 0. 1 represents true and 0 represents false. (the poison for Kuzco, Kuzco's poison )

if, else, elif
    - elif: short for 'else if'; optional branch that'll let you add another if test
    - else: optional branch that will catch anything not previously caught by if or elif; catches anything not previously caught by if or elif;

def test_numbers(number):
    if number < 100:
              print("This is a pretty small number")
    elif number == 100:
              print("Aight")
    else:
              print("Woah that number's biggun")
  

test_numbers(129837)
# Woah that number's biggun
test_numbers(12)
# This is a pretty small number
test_numbers(100)
# Aight

def fizzbuzz(number):
    if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
  
fizzbuzz(3)
  
fizzbuzz(5)
fizzbuzz(15)
# FizzBuzz
fizzbuzz(30)
# FizzBuzz
fizzbuzz(30)
# FizzBuzz
def fb(number):
    if number % 3 == 0:
              print("Fizz")
    if number % 5 == 0:
              print("Buzz")
    elif number % 3 == 0 and number % 5 == 0:
              print("FizzBuzz")
  
fb(30)
//Fizz
# Buzz
fb(25)
# Buzz
fb(21)
# Fizz

# using if to test for an empty list: 
#   empty list is "falsey", or resolves to False 
    # This is a function that prints a list of elements of a list or an error message if the list is empty. Print special message if list item is None. 

def my_func(my_list):
      if my_list:
              for item in my_list:
                      if item is None:
                              print("got  none dood")
              else:
                      print(item)
      else:
              print("Got empty list")
  
my_func([1, 2, 3])
# 3
my_func([2, None, "hello", 42])
# got  none dood
# 42
my_func([])
# Got empty list

# For loop, range, enumerate: 

# - making a list a loping it
my_list = [0, 1, 2]
for num in my_list:
      print(f"next value: {num}")
      
next value: 0
next value: 1
next value: 2

# - looping over list of numbers. can use range() function instead; first argument is inclusive and second is inclusive
for num in range(0, 5):
    print(f"next value: {num}")
      
next value: 0
next value: 1
next value: 2
next value: 3
next value: 4

# - enumerate: iterates over an iterable like a list and also gives you automatic counter; returns a tuple in the form of (counter, item)

my_list = ['milk', 'bread', 'eggs']    
for index, item in enumerate(my_list):
    print(f"Item {index}: {item}")
  
# Item 0: milk
# Item 1: bread
# Item 2: eggs

# - loopng over dictionaries keys and/or values; 

my_dict = {"foo": "barr", "Hello": "world"}
for key in my_dict:
    print(f"Key: {key}")
  
# Key: foo
# Key: Hello
for value in my_dict: 
      print(f"Value: {value}")
  
# Value: foo
# Value: Hello
for value in my_dict.values():
    print(f"Value: {value}")
  
# Value: barr
# Value: world
for key, value in my_dict.items():
      print(f"Item {key} = {value}")
  
# Item foo = barr
# Item Hello = world

# 'can use return keyword to break out of a loop within a function, while optionally returning to a value'
my_list = [1, 2, 3, 4, 5, 6, 7]
def is_num_in_list(num_to_check, list_to_search):
    for num in list_to_search:
        print(f"checking {num}...")
            if num == num_to_check:
                return True
      return False
  
is_num_in_list(27, my_list)
# checking 1 
# checking 2 
# checking 3 
# checking 4 
# checking 5 
# checking 6 
# checking 7 
# False
is_num_in_list(4, my_list)
# checking 1 
# checking 2 
# checking 3 
# checking 4 
# True

# - while loops

# instead of looping over a sequence, while loops continue looping while a certain condition is met (or not met) condition is checked at beginning of every iteration

while counter < 3:
    print(f"counter = {counter}")
    counter += 1
  
# counter = 0
# counter = 1
# counter = 2

# loop ends once counter == 3; remainder of loop is bypassed

# could loop forever doing while True or while False; should make sure you have solid break connections, or progran will loop forever

while True:
      print(f"counter = {counter}")
      if counter == 3:
              break
      counter += 1
  
# counter = 0
# counter = 1
# counter = 2
# counter = 3

# - nested loops
#     break keyword only gets you our of whichever loop you're breaking;
#     only way to exit all loops is with multiple break statements

names = ["Bob", "Bill", "Jim"]
target_letter = 'l'
found = False
for name in names:
    for char in name:
            if char == target_letter:
                    found = True
                    break
    if found:
            print(f"Found {name} with letter: {target_letter}")
            break
  
# Found Bill with letter: l

for x in range (0, 5):
      for y in range(0, 5):
              print(f"x = {x}, y = {y}")
              if y == 2:
                      break
  
# x = 0, y = 0
# x = 0, y = 1
# x = 0, y = 2
# x = 1, y = 0
# x = 1, y = 1
# x = 1, y = 2
# x = 2, y = 0
# x = 2, y = 1
# x = 2, y = 2
# x = 3, y = 0
# x = 3, y = 1
# x = 3, y = 2
# x = 4, y = 0
# x = 4, y = 1
# x = 4, y = 2