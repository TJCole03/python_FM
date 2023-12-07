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