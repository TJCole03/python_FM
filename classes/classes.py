class Pokemon: 
    battle = True

    def start(self):
        if self.battle:
            print("Pokemon is ready for battle!")
        else:
            print("Oh no! No more pokemon!")
mudkip = Pokemon()
mudkip.battle = False
print(f"Mudkip is battling! {mudkip.battle}")
print(mudkip.start())

# Mudkip is battling! True
# Pokemon is ready for battle!
# None

torchic = Pokemon()
torchic.start()
print(f'Torchic used Ember! {torchic.battle}')
# Torchic used Ember! True

# SELF REFERS TO AN INSTANCE

#TRYING TO CALL INSTANCE METHOD ON A CLASS
# print(Pokemon.start())

# returns this error. can't call a method n a class
# Traceback (most recent call last):
#  File "/Users/timothycole/python-workshop-frontend-masters/classes/classes.py", line 26, in <module>
#    print(Pokemon.start())
#          ^^^^^^^^^^^^^^^
# TypeError: Pokemon.start() missing 1 required positional argument: 'self'

class Dog:
    barks = True
    number_of_legs = 4

    @classmethod
    def get_number_of_legs(cls):
        return cls.number_of_legs
    def start(self):
        if self.barks:
            print("Doggo woke up! Woof Woof!")
        else:
            print("Doggo is still asleep")

my_dog = Dog()
print(f"my Dog has {Dog.get_number_of_legs()} legs")
# overriding this in our instance
my_dog.number_of_legs = 3
# accessing new instance variable
print(f"Tripod has {my_dog.number_of_legs} legs")
# calling class method on instance
print(f"my dog has {my_dog.get_number_of_legs()} legs")
# my dog has 4 legs

print(type(42)) #<class 'int'>
print(isinstance(42, int)) # True 
print(isinstance('hi', int)) # False
print(isinstance('hi', str))# True

print(isinstance(mudkip, Pokemon)) # True

# MAGIC METHODS 
# have two unerscoreson either side 
# __init()__

# class Car: 
#     runs = True

#     def __init__(self, make, model):
#         self.make = make
#         self.model = model

#     def start(self):
#         if self.runs:
#             print(f"Your {self.make} {self.model} is started. Vroom!")
#         else:
#             print(f"Your {self.make} {self.model} is broken")
# my_car = Car("Ford", "Focus")
# my_car.start()

#__str__ and __repr__
# both functions return strings representing objects
# both functions return a string representation of an object
# __str__ returns end-uder output that is more readable
# __repr__ returns PYthon code necessary to rebuild the object
# __str__() maps to the built-in function str() and __repr__() maps to the built-in function repr().

import datetime
now = datetime.datetime.now()
print(str(now)) # 2023-12-21 06:45:56.259582
print(repr(now)) # datetime.datetime(2023, 12, 21, 6, 45, 56, 259582)

class Car: 
    runs = True

    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __str__(self):
        return f"<<Car object: {self.make} {self.model}>>"

    def __repr__(self):
        return f"Car('{self.make})', '{self.model}')"
    
my_car = Car("Ford", "Focus")
print(f"This object is a {str(my_car)}")
print(f"To reproduce it, type: {repr(my_car)}")
# This object is a <<Car object: Ford Focus>>
# To reproduce it, type: Car('Ford)', 'Focus')

# converting a list of number-strings insto a list of integers
my_ints = [int(str_num) for str_num in ["1", "2", "3"]]
print(my_ints)
[1, 2, 3]