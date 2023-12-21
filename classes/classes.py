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
print(Pokemon.start())

# returns this error. can't call a method n a class
# Traceback (most recent call last):
#  File "/Users/timothycole/python-workshop-frontend-masters/classes/classes.py", line 26, in <module>
#    print(Pokemon.start())
#          ^^^^^^^^^^^^^^^
# TypeError: Pokemon.start() missing 1 required positional argument: 'self'