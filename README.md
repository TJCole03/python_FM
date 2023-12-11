# python_FM

- variables and data types: 
    - dont name your variables things like int, str, list, etc... 
    -helpful REPL meethods, help() type() and dir()

>>> superman = 8484
>>> type(superman)
<class 'int'>
- >>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
    ---DOUBLE UNDERSCORED ONES ARE INTERNAL METHODS THAT AREN'T MEANT TO BE USED (USUALLY)

 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill'
 
 
 ]

 NameError: name 'lottery_numbers' is not defined
>>> lottery_nums = [2, 5, 23, 20458, 334, 333]
>>> sorted(lottery_nums)
[2, 5, 23, 333, 334, 20458]
>>> lottery_nums.sort()
>>> lottery_nums
[2, 5, 23, 333, 334, 20458]

>>> lottery_nums.append(98, 5000000)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: list.append() takes exactly one argument (2 given)
>>> lottery_nums.append(98)
>>> lottery_nums.append(5000000)
>>> lottery_nums
[2, 5, 23, 333, 334, 20458, 98, 5000000]
>>> sorted(lottery_nums)
[2, 5, 23, 98, 333, 334, 20458, 5000000]

>>> lottery_nums.insert(0, 24)
>>> lottery_nums)
  File "<stdin>", line 1
    lottery_nums)
                ^
SyntaxError: unmatched ')'
>>> lottery_nums
[24, 2, 5, 23, 333, 334, 20458, 98, 5000000]
>>> lottery_nums.sort()
>>> lottery_nums
[2, 5, 23, 24, 98, 333, 334, 20458, 5000000]

METHODS HAD DEF KEYWORD IN FRONT OF THEM

When we start a python program from the command line, the entry point will be something like: 
    if __name__ === "__main__":

F STRINGS: 
    strings with built-in formatting; 
    allows us to provide variables inside curlybraces and the representations gets
        inserted right into the string
        f"stars:>{min_stars}"

    in example: 
        starts with base of query, loop through every language in list of languages
        and then append onto the query  a string like: 
            query += f"language:{language}"

R STRINGS: REGULAR EXPRESSION 
B STRINGS: BYTE STRINGS 

python_variables_should_look_like_this

it_is_called_snake_casing

special keywords in python you cannot use
    - if 
    - list () 
    - str

>>> list()
[]
>>> list = 'hey'
>>> list()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object is not callable

>>> string = 'hella'
>>> help(string.isalpha)
isalpha() method of builtins.str instance
    Return True if the string is an alphabetic string, False otherwise.
    
    A string is alphabetic if all characters in the string are alphabetic and there
    is at least one character in the string.

NUMBERS
min(), max(), round()

IN PYTHON, EVERYTHING UNDER THE HOOD IS AN OBJECT

STRINGS
    >>> >>> a_long_st = """
... a
... long
... long
... long
... long
... long 
... long 
... long 
... loooooooong
... ass 
... string
... """
>>> a_long_st
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'a_long_st' is not defined. Did you mean: 'a_long_string'?
>>> a_long_string
'\na\nlong\nlong\nlong\nlong\nlong \nlong \nlong \nloooooooong\nass \nstring\n'
>>> print(a_long_string)

a
long
long
long
long
long 
long 
long 
loooooooong
ass 
string
^^^^
not how pythog stores it under the hood

can print out strings, variables, and multiples things as long as theyere
    separated by commas


f strings again
    >>> f"hey"
'hey'
>>> f"hey {superman}"
'hey 8484'
>>> 
'hey 8484'
>>> name = "Spider-Man"
>>> name.replace("Sp", "P")
'Pider-Man'
>>> name
'Spider-Man'
>>> new = name.replace("Sp", "P")
>>> new
'Pider-Man'
>>> name
'Spider-Man'

>>> list()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object is not callable
>>> []
[]
>>> type([])
<class 'list'>
>>> names = ['bob', 'joe', 'bill']
>>> names
['bob', 'joe', 'bill']

>>> names[1]
'joe'
>>> names[1] = 'vinny'
>>> names
['bob', 'vinny', 'bill']
>>> f"I am {names[1]}{12/2}"
'I am vinny6.0'
>>> names.append("Mickey")
>>> names
['bob', 'vinny', 'bill', 'Mickey']
>>> names.pop
<built-in method pop of list object at 0x104a557c0>
>>> names.pop()
'Mickey'
>>> names
['bob', 'vinny', 'bill']

WE USE HELPER FUNCTIONS TO DIAGNOSE AND SOLVE PROBLEMS
    - type(), dir(), str()

- strings can have 'single' or "double" quotes

TUPLES
    - lightweight collections that keep track of different but related items
        - Pokeballs; pokeball, great ball, ultra, etc
    - in comparison: lists contain items that are all similar in nature
    - once you initialize/create a tuple, it'll be IMMUTABLE (unlike a list)
        -can't push, can't pop, can't do anything
    - they're sorted so they have an order to how they're stored
    - Tuples hold data and information securely; 
        - one good use is storing information in a row in a spreadsheet
    - 
>>> # list []
>>> # tuple () 
>>> ()
()
>>> my_tup = ()
>>> type(my_tup)
<class 'tuple'>
>>> my_tup = ('hulk')
>>> type(my_tup)
<class 'str'>
    - why is it a string? 
        - python REPL doensn't recognize the syntax the same way JS would
        - need a comma
>>> # tuple (,)
>>> (1,)
(1,)
>>> ('hulk',)
('hulk',)
>>> my_tup = ('hulk',)
>>> type(my_tup)
<class 'tuple'>

>>> student = ('billy', 7, 'detention', 0.5)
>>> student[3]
0.5
>>> billy
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'billy' is not defined
>>> 'billy'
'billy'
>>> student[1] = 10
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment

>>> student
('billy', 7, 'detention', 0.5)
>>> name, age, class, gpa = student
  File "<stdin>", line 1
    name, age, class, gpa = student
               ^^^^^
SyntaxError: invalid syntax
>>> name, age, subject, gpa = student
>>> name
'billy'
>>> age
7
>>> subject
'detention'
>>> gpa
0.5

SETS
    - Mutable data types that only allow storage on immutable items in unsorted way
    - CANNOT CONTAIN: lists, dictionaries, other sets
    - Can ONLY contain unique items within them
        - benefit is speed
    - 

>>> type({1,2})
<class 'set'>
>>> my_set = {}
>>> type(my_set)
<class 'dict'>
>>> type(set())
<class 'set'>
>>> type({3})
<class 'set'>
>>> type({3, 3, 4})
<class 'set'>
>>> my_set
{}
>>> >>> my_set = {3, 4, 3}
  File "<stdin>", line 1
    my_set = {3, 4,, 4, 3}
                   ^
SyntaxError: invalid syntax
>>> my_set = {3,4,3}
>>> type(my_set)
<class 'set'>
>>> my_set
{3, 4}
>>> 
>>> # shortcut to check for mutability
>>> # hash()
>>> hash(4)
4
>>> hash("name")
-4814052813746128978
>>> hash([])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'

if you see this exceptions like this, read them from the bottom up and consider where else you could've seen it

SETS ARE UNORDERED
    >>> my_set = {"a", 1, 2, 4, "TJ"}
    >>> my_set
    {1, 2, 4, 'a', 'TJ'}

    >>> my_set
{1, 2, 4, 'a', 'TJ'}
>>> my_set.add("yayy")
>>> my_set
{1, 2, 4, 'a', 'TJ', 'yayy'}
>>> my_set.discard(2)
>>> my_set
{1, 4, 'a', 'TJ', 'yayy'}
>>> colors = {'red', 'orange'}
>>> numbers = {4,2,0,6,9}
>>> colors.update(numbers)
>>> colors
{0, 'orange', 2, 4, 6, 9, 'red'}


DICTIONARIES
    - data types that allow us to store key-value pairs
    - mutable; but just like sets, dictionary KEYS need to be immutable
    - fast item lookup, fast membership testing
        - why? dictionary keys must be HASHABLE 
    - CANNOT HAVE LIST AS KEY IN DICTIONARY BECAUSE LIST IS MUTABLE
    - CANNOT HAVE MUTABLE DATATYPES IN DICTIONARIES
    - CAN HAVE TUPLE BECAUSE TUPLES ARE IMMUTABLE
    - DICTIONARIES DO NOT HAVE AN ORDER
    - TO ACCESS ITEMS IN DICTIONARY, PROVIDE KEY AND USE SQUARE BRACKETS
    - IF I WANTED TO GET SOMETHING FROM MY DICTIONARY AND NOT DEAL WITH AN EXCEPTION THAT I THEN HAVE TO CATCH, I CAN USE GET METHOD
    - DICTIONARIES CAN HAVE LISTS AS VALUES

>>> # dictionaries
>>> {1,2,3}
{1, 2, 3}
>>> # dictionary {:}
>>> type({})
<class 'dict'>
>>> {"one": 1, "two": 2}
{'one': 1, 'two': 2}
>>> my_dict = {"one": 1, "two": 2}
>>> type(my_dict)
<class 'dict'>
>>> my_number = {"one": [1, 1, 1]}
>>> {'one': 1, 'two': 2}
{'one': 1, 'two': 2}
>>> my_dict[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 0
>>> my_dict("one")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'dict' object is not callable
>>> my_dict["one"]
1
>>> my_dict
{'one': 1, 'two': 2}
>>> my_dict.get("three", "default")
'default'
>>> my_dict.get("three")
>>> my_dict.get("two", "default")
2
>>> my_dict
{'one': 1, 'two': 2}
>>> my_dict["two"] = 'wqjahrenovf'
>>> my_dict["three"] = 3
>>> my_dict
{'one': 1, 'two': 'wqjahrenovf', 'three': 3}
>>> my_nums = {"one": [1, 1, 1]}
>>> my_nums["one"]
[1, 1, 1]
>>> my_nums["one"].append([1, 1, 1])
>>> my_nums
>>> my_nums
{'one': [1, 1, 1, [1, 1, 1]]}
>>> my_dict
{'one': 1, 'two': 'wqjahrenovf', 'three': 3}
>>> my_nums
{'one': [1, 1, 1, [1, 1, 1]]}
>>> type(my_nums["one"])
<class 'list'>
>>> my_nums
{'one': [1, 1, 1, [1, 1, 1]]}
>>> my_dict.keys()
dict_keys(['one', 'two', 'three'])
>>> my_dict.values()
dict_values([1, 'wqjahrenovf', 3])
>>> my_dict.items()    




LISTS, SETS, AND DICTIONARIES ARE MUTABLE!!

type_your_stuff_like_this kepe files names SHORT

python files need to end in .py

NO CAMEL-CASE, ALL CAPS, OR LONG-ASS NAMES

.gitignore for +_pyc
PYC files: compiled intermediary files for optimization; 

(env) timothycole@Timothys-MacBook-Pro python-workshop-frontend-masters % ls
README.md       env             hello.py        project.py      tictactoe
(env) timothycole@Timothys-MacBook-Pro python-workshop-frontend-masters % cat hello.py
# in file: hello.py

greetings = ['hello', 'bonjour', 'hola']
worlds = ['planet earth', 'monde', 'mundo']

for greeting in greetings:
    print(f'{greeting} {worlds}!')
(env) timothycole@Timothys-MacBook-Pro python-workshop-frontend-masters % hello.py
zsh: command not found: hello.py
(env) timothycole@Timothys-MacBook-Pro python-workshop-frontend-masters % python hello.py
hello ['planet earth', 'monde', 'mundo']!
bonjour ['planet earth', 'monde', 'mundo']!

>>> long_list= list(range(25))
>>> long_list
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
>>> from pprint import pprint
>>> pprint(long_list)
[0,
 1,
 2,
 3,
 4,
 5,
 6,
 7,
 8,
 9,
 10,
 11,
 12,
 13,
 14,
 15,
 16,
 17,
 18,
 19,
 20,
 21,
 22,
 23,

 FUNCTIONS; 
    - 'def' keyword
        - everything that's indented in that functions belongs to that function 
    - NO CURLY BRACES
    - def my_func():
        print("Hi")
    my_func (calling the function)
    can save function into variable but would have to redefine the funciton and have it return the value instead of printing it. it'll return the string and NOW we can save that to a variable
    >>> def my_func():
...     print("Hi")
... 
>>> my_func()
Hi
>>> greeting = my_func()
Hi
>>> type(greeting)
<class 'NoneType'>
>>> def my_func():
...     return "hi"
... 
>>> my_func()
'hi'
>>> greeting =  my_func()
>>> greeting 
'hi'

>>> def add_numbers(x, y):
...     return x + y
... 
>>> add_numbers(2, 5)
7
>>> result = add_numbers(10, 20)
>>> result
30
>>> add_numbers(x, y, z=1):
  File "<stdin>", line 1
    add_numbers(x, y, z=1):
                          ^
SyntaxError: invalid syntax
>>> def add_numbers(x, y, z=1):
...     return x + y + z
... 
>>> add_numbers(4, 2)
7
>>> add_numbers(90, 4)
95
>>> add_numbers(3, 6, 6)
15

>>> def create_query(language="JavaScript", num_stars=10, sort="desc"):
...     return f"language: {language}, num_stars is {num_stars}, sort is {sort}"
... 
>>> create_query()
'language: JavaScript, num_stars is 10, sort is desc'
>>> create_query(language="python")
'language: python, num_stars is 10, sort is desc'
>>> create_query(num_stars=20)
'language: JavaScript, num_stars is 20, sort is desc'

DONT USE MUTABLE TYPES AS DEFAULT ARGUMENTS 
DONT USE MUTABLE TYPES AS DEFAULT ARGUMENTS 
DONT USE MUTABLE TYPES AS DEFAULY ARGUMENTS

HERE'S WHY: 
>>> def do_stuff(my_list=[]):
...     my_list.append("stuff!")
...     return my_list
... 
>>> do_stuff()
['stuff!']
>>> do_stuff()
['stuff!', 'stuff!']
>>> do_stuff()
['stuff!', 'stuff!', 'stuff!']
>>> do_stuff()
['stuff!', 'stuff!', 'stuff!', 'stuff!']

The way python works under the hood, my_list=[] gets declared once. if you use my_list=[], you will continue to get the same instance of my_list=[] every time you call that function.

NO MUTABLE DEFAULT ARGUMENTS!!!!

DO THIS INSTEAD: 

>>> def do_stuff(my_list=None):
...     if my_list == None:
...             my_list = []
...             my_list.append("Winner chicken dinner")
...     return my_list
... 
>>> do_stuff()
['Winner chicken dinner']
>>> do_stuff()
['Winner chicken dinner']
>>> do_stuff()

>>> def print_name(name):
...     print(name)
... 
>>> print_name("TJ")
TJ
>>> name
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'name' is not defined
>>> name = "TJ"
>>> print(f"name outside function: {name}")
name outside function: TJ
>>> 
>>> def try_change_name():
...     name = "max"
...     print(f"name INSIDE of function: {name}")
... 
>>> try_change_name()
name INSIDE of function: max
>>> name
'TJ'

DONT TRY CHANING VARIABLES IN A FUNCTION THAT WERE DECLARED OUTSIDE OF IT

BOOLEANS 

    - list, tuple, set, dict
    - empty containers evaluate to false, containers with items eval to true
    - 0 is False, all other numbers are true (including negative)
    - 
    - bool: used to figure out the truthiness your expression has
        - bool maps to the constructor for the built in true or false
    -
    >> 3 < 5
True
>>> 5 < 3
False
>>> bool 
<class 'bool'>
>>> bool(0)
False
>>> bool(1)
True
>>> bool(3 < 5)
True
>>> bool([])
False

>>> list1 = [1, 2, 3]
>>> list2 = [1, 2, 3]
>>> list1 == list2
True
>>> list1 is list2 # checks for identity: do they point to the same place in MEMORY?
False (they're stored at different variables)

- in order to check for equality, with these keywords, we want to use the is keyword to check for identity- do they point to the same place in memory? 
- handy with None because an empty list evauates to false

>>> bool(None)
False
>>> bool([])
False
>>> x = None
>>> is x None
  File "<stdin>", line 1
    is x None
    ^^
SyntaxError: invalid syntax
>>> x is None
True
>>> [] is None
False
>>> # dont do a == True
>>> a = True
>>> a is True
True
>>> # Python has and, or not
>>> # none of this: NOT, &&, ||
>>> a = True
>>> b = True
>>> a and b
True
>>> True and False
False
>>> True or False
True
>>> True or True
True
>>> False or False
False
>>> False
False
>>> a
True
>>> not a
False
>>> True and (True or False)
True
>>> if 3 < 5: 
...     print("hi")
... 
hi
>>> if 3 > 5: 
...     print("hi")
...

>>> if 3 < 5
  File "<stdin>", line 1
    if 3 < 5
            ^
SyntaxError: expected ':'
>>> if 3 < 5
  File "<stdin>", line 1
    if 3 < 5
            ^
SyntaxError: expected ':'
>>> if 3 < 5: 
...     print("hi")
... 
hi
>>> if 3 > 5: 
...     print("hi")
... 
>>> a = True
>>> b = False
>>> if not b:
...     print("hi")
... 
hi
>>> if not a: 
...     pring("hi")
... 
>>> if []:
... 
  File "<stdin>", line 2
    
    ^
>>> if [1, 2]:
...     print('hi')
... 
hi
>>> b = []
>>> if b:
...     print("HI")
... 
>>> if b == True # dont do this!
  File "<stdin>", line 1
    if b == True # dont do this!
                 ^^^^^^^^^^^^^^^
SyntaxError: expected ':'
>>> if b == True: # dont do this!
... 
  File "<stdin>", line 2
    
    ^
IndentationError: expected an indented block after 'if' statement on line 1
>>> if b == True: # dont do this!
...     print("HI")
... 
>>> if 5 < 3:
...     print("HI")
... else:
...     print("bye"
... )
... 
bye
>>> 

PRACTICE TIME 

SETS 

>>> # create empty set
>>> my_set = {}
>>> type(my_set)
<class 'dict'>
>>> # {} make dictionaries {} make dictionaries {} make dicts
>>> my_set = set()
>>> # () makes sets
>>> type(my_set)
<class 'set'>
>>> # creating non-empty set
>>> my_set = {1, 2, 3}
>>> # can add and remove items from set
>>> my_set.add(4)
>>> my_set.remove(2)
>>> my_set 
{1, 3, 4}
>>> 2 in my_set
False
>>> # unlike lists, every item in a set must be unique; every item in a set must be unique. every item in a set must be unique
>>> my_set
{1, 3, 4}
>>> my_set.add(3)
>>> my_set
{1, 3, 4}
>>> # see? nothing added since it isnt unique
>>> other_set = {1, 2, 3}
>>> # can combine two sets
>>> my_set.union(other_set)
{1, 2, 3, 4}
>>> # can get intersection of two sets
>>> my_set.intersection(other_set)
{1, 3}

TUPLES
>>> my_tuple = 1
>>> my_tuple
1
>>> # lets add to the tuple
>>> my_tuple[1] = 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object does not support item assignment
>>> # doesn't work because tuples are immutable; canot change them once they've been created
>>> # great for moving data around in a lightweight way 
>>> # can unpack them easily into multiple variables
>>> person = ('Jim', 29, 'Austin, TX')
>>> name, age, hometown = person
>>> name
'Jim'
>>> age 
29
>>> hometown
'Austin, TX'
>>> person.add('Drums')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'tuple' object has no attribute 'add'
>>> type(person)
<class 'tuple'>


DICTIONARIES
>>> my_dict = {"key": "value":}
  File "<stdin>", line 1
    my_dict = {"key": "value":}
                             ^
SyntaxError: invalid syntax
>>> my_dict = {"key": "value"}
>>> # dictionaries DO NOT HAVE nuerical indexes, dicts don't have numberical indexes, dicts dont have numerical indexes
>>> # if we try using an index number, we get a KeyError
>>> UNLESS 0 happens to be a key
  File "<stdin>", line 1
    UNLESS 0 happens to be a key
           ^
SyntaxError: invalid syntax
>>> my_dict[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 0
>>> my_dict["hola"] = "mundo"
>>> my_dict["foo"] = "bar"
>>> my_dict
{'key': 'value', 'hola': 'mundo', 'foo': 'bar'}
>>> # what is the value for 'hola'?
>>> my_dict['hola']
'mundo'
>>> #can also use get() get get a key
>>> my_dict.get('hola')
'mundo'
>>> my_dict['baz']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'baz'
>>> my_dict["baz"]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'baz'
>>> 
>>> # we get KeyError when the key we're searching for doesn't exist
>>> "baz
  File "<stdin>", line 1
    "baz
    ^
SyntaxError: unterminated string literal (detected at line 1)
>>> 'baz' in my_dict
False
>>> # or we can use a defauly value; if 'baz' doesn't exist, return 'default response':
>>> my_dict.get('baz', 'default response')
'default response'
>>> # separating dictionary into list of keys
>>> my_dict.keys()
dict_keys(['key', 'hola', 'foo'])
>>> my_dict.values()
dict_values(['value', 'mundo', 'bar'])
>>> # items() for when we want to get both key and value pairs; gets list of tuples; items() for getting both key and value pairs to get a list of tuples; items() to get both key/value pairs, returns a tuple
>>> my_dict.items()
dict_items([('key', 'value'), ('hola', 'mundo'), ('foo', 'bar')])
>>> 

MUTABILITY

>>> # lists are mutable; lists are mutable; lists are mutable
>>> my_list = [1, 2, 3]
>>> my_list[0] = 'a'
>>> my_list
['a', 2, 3]
>>> #dictionaries are mutable; dicts are mutable; dicts are mutable
>>> my_dict = {"sup": "dude"}
>>> my_dict["foo"] = "bar"
>>> my_dict
{'sup': 'dude', 'foo': 'bar'}
>>> # sets are mutable, sets are mutable. sets are mutable
>>> my_set = {1, 2, 3}
>>> my_set[0] = 'a'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'set' object does not support item assignment
>>> my_set.add('a')
>>> my_set
{1, 2, 3, 'a'}
>>> # tuples are immutable. tuples are immutable. tuples are immutable
>>> my_tuple = {1, 2, 3}
>>> my_tuple[0] = 'a'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'set' object does not support item assignment