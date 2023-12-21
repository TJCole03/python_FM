my_string = "Hello World!"
print(my_string[6:12]) # from index 7 to 12
# returns 'world'
#lopsided slicing
print(my_string[:12])
#'Hello World'
print(my_string[6:])
#'World'
print(my_string[:])
#'Hello World'
print(my_string[-1])
# '!'

# shift command D


my_list = ['h', 'e', 'l', 'l', 'o', '!']
print('my_list', len(my_list))
print('4:6', (my_list[4:6]))
print('4:', (my_list[4:]))
print('-2', (my_list[-2:]))

# my_list 6
# 4:6 2
# 4: 2
# -2 1

new_list = [num for num in range(0,100) if num % 2 != 0]
print('new_list', new_list)
slizzy = [num for num in range(0,100) if num % 2 == 0]
print('slizzy', slizzy[29:71])
# returns slizzy [58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]
print('slizzy', slizzy[30:70])
# returns slizzy [60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]

dog = [num for num in range(0,100)]
print('dog', dog[30:70:2])
# dog [30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68]

backwards_slice = dog[::-1]
print('backwards_slice', backwards_slice)
# backwards_slice [99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 
# 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 
# 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 
# 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 
# 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 
# 1, 0]

#ZIP
import random
names = ['bob', 'jack', 'dick', 'willie']
scores = [random.randint(0,10) for name in names]
print(scores)
for name, score in zip(names, scores):
    print(f"{name} got a score of {score}")

# [4, 2, 4, 4]
# bob got a score of 4
# jack got a score of 2
# dick got a score of 4
# willie got a score of 4

# CONVERTING BETWEEN NUMBERS AND STRINGS

my_string = str(100)
print(my_string)
print(type(my_string))
my_int = int(my_string)
print(my_int)
print(type(my_int))

# 100
# <class 'str'>
# 100
# <class 'int'>

# use float() to convert strings into floating point numbers 
pie = float('3.14156765')
print(pie)
# returns 3.14156765

# can use int() for converting floats as well

print(int(3.1415))
# returns 3

# CONVERTING BETWEEN LISTS AND STRINGS

newer_list = list('sup baby')
print(newer_list)
print(str(newer_list))
# returns ['s', 'u', 'p', ' ', 'b', 'a', 'b', 'y']
# ['s', 'u', 'p', ' ', 'b', 'a', 'b', 'y'] 
# which is not what we want
# need to join the elements of the list
print(''.join(newer_list))
print(','.join(newer_list))
print('-'.join(newer_list))

# sup baby
# s,u,p, ,b,a,b,y
# s-u-p- -b-a-b-y

# SPLIT() METHOD FOR CONVERTING STRING INTO LIST

newer_string = "Pizza Hut went downhill. Domino's reigns supreme."
split_string = newer_string.split(',')
print(split_string)
# returns ["Pizza Hut went downhill. Domino's reigns supreme."]