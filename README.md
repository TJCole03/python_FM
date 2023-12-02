# python_FM

- variables and data types: 
    - dont name your variables things like int, str, list, etc... 
    -helpful REPL meethods, help() type() and dir()
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