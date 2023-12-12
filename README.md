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

>>> hash(5)
5
>>> hash(hi)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'hi' is not defined
>>> hash('hi')
4933047920458786035
>>> hash('hi')
4933047920458786035
>>> hash("hi")
4933047920458786035
>>> 
>>> ()
()
>>> type(())
<class 'tuple'>
>>> (1)
1
>>> type(1)
<class 'int'>
>>> type((1))
<class 'int'>
>>> (1,)
(1,)
>>> type((1,))
<class 'tuple'>

>>> student = ("John", 8, "math", 2.5)
>>> name, age, subject, gpa = student
>>> name
'John'
>>> age
8
>>> gpa
2.5
>>> subject
'math'
>>> type(student)
<class 'tuple'>

>>> my_dict = {"name": "bob", "age": 112, "occupation": "demolition", "John": "Deere"}
>>> my_dict 
{'name': 'bob', 'age': 112, 'occupation': 'demolition', 'John': 'Deere'}
>>> my_dict[1]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 1
>>> my_dict["age"]
112

>>> my_dict["key"] = "a new value"
>>> my_dict
{'name': 'bob', 'age': 112, 'occupation': 'demolition', 'John': 'Deere', 'key': 'a new value'}
>>> "key" in my_dict
True
>>> "not a key" in my_dict
False
>>> my_list = ['bing', 'bang', 'bong']
>>> my_list[2] = 'boom'
>>> my_list
['bing', 'bang', 'boom']
>>> my_dict['key'] = 'some other value'
>>> my_dict
{'name': 'bob', 'age': 112, 'occupation': 'demolition', 'John': 'Deere', 'key': 'some other value'}
>>> 

>>> def add_numbers(x, y):
...     return x + y
... 
>>> def multiply(a, b)
  File "<stdin>", line 1
    def multiply(a, b)
                      ^
SyntaxError: expected ':'
>>> def multiply(a, b):
...     return a * b
... 
>>> multiple(4, 5)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'multiple' is not defined. Did you mean: 'multiply'?
>>> multiply(4, 5)
20
>>> add_numbers(1, 2479)
2480

>>> ## using string formatting to get more fancy
>>> print(f"Michael Phelps eats {multiply(10, 1000)} per day so he maintains his weight")
Michael Phelps eats 10000 per day so he maintains his weight
>>> print(f"Michael Phelps eats {multiply(10, 1000)} calories  per day so he maintains his weight")
Michael Phelps eats 10000 calories  per day so he maintains his weight

>>> x = 12
>>> y = 13
>>> >>> def add_numbers(x, y):
... 
  File "<stdin>", line 2
    
    ^
IndentationError: expected an indented block after function definition on line 1
>>> def add_numbers(x, y):
...     print(f"Inside the function, x = {x} and y = {y}")
...     return x + y
... 
>>> print(f"outside the function, x = {x} and y = {y}")
outside the function, x = 12 and y = 13
>>> print(f"The sum of 5 and 6 is {add_numbers(5, 6)}")
Inside the function, x = 5 and y = 6
The sum of 5 and 6 is 11

NUMBER OF ARGUMENTS MATTER

ALSO BE CAREFUL ABOUT INDENTS

>>> def add(x,y):
...     return x + y
... 
>>> add(59, 1)
60
>>> add(1, 2, 3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: add() takes 2 positional arguments but 3 were given
>>>     add(1,2)
  File "<stdin>", line 1
    add(1,2)
IndentationError: unexpected indent

>>> def add(x, y, operation='add')
  File "<stdin>", line 1
    def add(x, y, operation='add')
                                  ^
SyntaxError: expected ':'
>>> def add(x, y, operation='add'):
...     if operation == 'add':
...             return x + y
...     else:
...             return x - y
... add(5, 3)
  File "<stdin>", line 6
    add(5, 3)
    ^^^
SyntaxError: invalid syntax
>>> add(5,3)
8
>>> add(5, 3, operation='add')

>>> add(5, 3, operation='foo')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: add() got an unexpected keyword argument 'operation'

FIRST SIX OPERATORS TEST OBJECT'S VALUE; firs six operators test objects value. first six operators test objects value  'is' and 'is not' test whether two objects are the same thing; 

useful for singletons such as None and False

None, True, and False are when you want to use the 'is' keyword b/c we're not comparing two different values; wanna make sure the singleton is what that variable is pointing at;

>>> 5 < 3 == True
False

>>> 
>>> 5<3
False
>>> 3<5
True

>>> def calculate_nums(x, y, operation="add"):
...     if operation == "add":
...             return x + y
...     elif operation == "subtract":
...             return x - y
... 
>>> #testing new function; default is 'add' if we do not pass in keyword argument
>>> calculate_nums(4, 3)
7
>>> calculate_nums(4, 21)
25
>>> calculate_nums(4, 21, operation="subtract")
-17

>>> 10 > 10
False
>>> 10 >= 10
True
>>> 5 != 10
True
>>> 5 == True
False
>>> if 5:
...     print("number 5 is truthy")
... 
number 5 is truthy
>>> # number 5 is truthy for an if test!

true or false can be represented by 1 or 0. true can be represented as 1 and false as 0. 1 represents true and 0 represents false. (the poison for Kuzco, Kuzco's poison...)

if, else, elif
    - elif: short for 'else if'; optional branch that'll let you add another if test
    - else: optional branch that will catch anything not previously caught by if or elif; catches anything not previously caught by if or elif;

>>> def test_numbers(number):
...     if number < 100:
...             print("This is a pretty small number")
...     elif number == 100:
...             print("Aight")
...     else:
...             print("Woah that number's biggun")
... 

>>> test_numbers(129837)
Woah that number's biggun
>>> test_numbers(12)
This is a pretty small number
>>> test_numbers(100)
Aight

>>> def fizzbuzz(number):
...     if number % 3 == 0 and number % 5 == 0:
...             print("FizzBuzz")
... 
>>> fizzbuzz(3)
>>> 
>>> fizzbuzz(5)
>>> fizzbuzz(15)
FizzBuzz
>>> fizzbuzz(30)
FizzBuzz
>>> fizzbuzz(30)
FizzBuzz
>>> def fb(number):
...     if number % 3 == 0:
...             print("Fizz")
...     if number % 5 == 0:
...             print("Buzz")
...     elif number % 3 == 0 and number % 5 == 0:
...             print("FizzBuzz")
... 
>>> fb(30)
Fizz
Buzz
>>> fb(25)
Buzz
>>> fb(21)
Fizz

using if to test for an empty list: 
    empty list is "falsey", or resolves to False 
    This is a function that prints a list of elements of a list or an error message if the list is empty. Print special message if list item is None. 

>>> def my_func(my_list):
...     if my_list:
...             for item in my_list:
...                     if item is None:
...                             print("got  none dood")
...             else:
...                     print(item)
...     else:
...             print("Got empty list")
... 
>>> my_func([1, 2, 3])
3
>>> my_func([2, None, "hello", 42])
got  none dood
42
>>> my_func([])
Got empty list

For loop, range, enumerate: 

- making a list a loping it
    >>> my_list = [0, 1, 2]
    >>> for num in my_list:
    ...     print(f"next value: {num}")
    ... 
    next value: 0
    next value: 1
    next value: 2

- looping over list of numbers. can use range() function instead; first argument is inclusive and second is inclusive
    >>> for num in range(0, 5):
    ...     print(f"next value: {num}")
    ... 
    next value: 0
    next value: 1
    next value: 2
    next value: 3
    next value: 4

- enumerate: iterates over an iterable like a list and also gives you automatic counter; returns a tuple in the form of (counter, item)

>>> my_list = ['milk', 'bread', 'eggs']    
>>> for index, item in enumerate(my_list):
...     print(f"Item {index}: {item}")
... 
Item 0: milk
Item 1: bread
Item 2: eggs

- loopng over dictionaries keys and/or values; 

>>> my_dict = {"foo": "barr", "Hello": "world"}
>>> for key in my_dict:
...     print(f"Key: {key}")
... 
Key: foo
Key: Hello
>>> for value in my_dict: 
...     print(f"Value: {value}")
... 
Value: foo
Value: Hello
>>> for value in my_dict.values():
...     print(f"Value: {value}")
... 
Value: barr
Value: world
>>> for key, value in my_dict.items():
...     print(f"Item {key} = {value}")
... 
Item foo = barr
Item Hello = world

can use return keyword to break out of a loop within a function, while optionally returning to a value
>>> my_list = [1, 2, 3, 4, 5, 6, 7]
>>> def is_num_in_list(num_to_check, list_to_search):
...     for num in list_to_search:
...             print(f"checking {num}...")
...             if num == num_to_check:
...                     return True
...     return False
... 
>>> is_num_in_list(27, my_list)
checking 1...
checking 2...
checking 3...
checking 4...
checking 5...
checking 6...
checking 7...
False
>>> is_num_in_list(4, my_list)
checking 1...
checking 2...
checking 3...
checking 4...
True

- while loops

instead of looping over a sequence, while loops continue looping while a certain condition is met (or not met) condition is checked at beginning of every iteration

>>> while counter < 3:
...     print(f"counter = {counter}")
...     counter += 1
... 
counter = 0
counter = 1
counter = 2

loop ends once counter == 3; remainder of loop is bypassed

could loop forever doing while True or while False; should make sure you have solid break connections, or progran will loop forever

>>> while True:
...     print(f"counter = {counter}")
...     if counter == 3:
...             break
...     counter += 1
... 
counter = 0
counter = 1
counter = 2
counter = 3

- nested loops
    break keyword only gets you our of whichever loop you're breaking;
    only way to exit all loops is with multiple break statements

>>> names = ["Bob", "Bill", "Jim"]
>>> target_letter = 'l'
>>> found = False
>>> for name in names:
...     for char in name:
...             if char == target_letter:
...                     found = True
...                     break
...     if found:
...             print(f"Found {name} with letter: {target_letter}")
...             break
... 
Found Bill with letter: l

>>> for x in range (0, 5):
...     for y in range(0, 5):
...             print(f"x = {x}, y = {y}")
...             if y == 2:
...                     break
... 
x = 0, y = 0
x = 0, y = 1
x = 0, y = 2
x = 1, y = 0
x = 1, y = 1
x = 1, y = 2
x = 2, y = 0
x = 2, y = 1
x = 2, y = 2
x = 3, y = 0
x = 3, y = 1
x = 3, y = 2
x = 4, y = 0
x = 4, y = 1
x = 4, y = 2