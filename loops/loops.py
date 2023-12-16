colors = ["red", "green", "blue", "orange"]
for color in colors: 
    print(f"Color is: {color}")

# If you need to get a handle on an index and print out both the element 
# and position of an elemnt
# no need to declare a variable to keep track of 'i', and then increment and then print
# PYTHON HAS A SHORTCUT CALLED ENUMERATE; 
# ENUMERATE: PASS IT IN A LIST, RETURN A TUPLE, PASS IT IN A LIST RETURN A TUPLE. PASS IT IN A LST, RETURN A TUPLE. 

print(list(enumerate(colors))) 
#[(0, 'red'), (1, 'green'), (2, 'blue'), (3, 'orange')]
for index, color in enumerate(colors):
    print(f"{index} color at: {color}") 

# 0 color at: red
# 1 color at: green
# 2 color at: blue
# 3 color at: orange

# loops don't have the same scoping as functions
print("outside the loop", color) #when we're outside the loop, this cariable color still exists
#value of the variable is the last value in the list

chewy = list(range(31))
print(chewy) # PRINTS A LIST
for num in chewy:
    print(num) # JUST PRINTS THE NUMBERS

#IF WE WANT TO LOOP OVER A DICTIONARY 
# WE MUST BE MINDFUL THAT BY DEFUALT DICTIONARIES RETRUN  ONLY KESY
# NEED TO EXPLICITYL ASK FOR BOTH KEYS AND VALUES

hex_colors = {
     "Red": "#FF0000",
     "Green": "#008000",
     "Blue": "#0000FF",
}

for foo in hex_colors:
    print(foo)
    #only returns the keys
    # Red
    # Green
    # Blue
print(hex_colors.items())
#returns: dict_items([('Red', '#FF0000'), ('Green', '#008000'), ('Blue', '#0000FF')])
for key, value in hex_colors.items():
    print(key)
    print("---")
    print(value)
# Red
# ---
# #FF0000
# Green
# ---
# #008000
# Blue
# ---

counter = 0
max = 21
while counter < max:
    print(f"count: {counter}")
    counter = counter + 2

# count: 0
# count: 2
# count: 4
# count: 6
# count: 8
# count: 10
# count: 12
# count: 14
# count: 16
# count: 18
# count: 20

names = ["Stacy", "Darcy", "Macy", "Marcy"]

def return_target(target="Stacy"):
    for name in names:
        if name == target:
            return name
        
print(return_target())
print(return_target(target="Darcy"))
        