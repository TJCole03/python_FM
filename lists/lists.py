import random

names = ["Nina", "Max", "Rose", "Jimmy", "Stephen", "Todd"]
my_list = [] # empty list
for name in names:
    my_list.append(len(name))
print("Before:", my_list)
# [4, 3, 4, 5]
# list comprehensions let us do the same tings in one line

my_odd_list = [name for name in names if len(name) % 2 != 0]
my_even_list = [name for name in names if len(name) % 2 == 0]

print("After odds:", my_odd_list)
print("After evens:", my_even_list)

names_string = "TJ, Mellanie, Luna, Lotus"
print(names_string.split(
    ","
))
#['TJ', ' Mellanie', ' Luna', ' Lotus']
print(names_string)
names_list = names_string.split(",")
print(names_list)

woowoo = " <=> ".join(names_list)
print(woowoo)

my_nums = range(10)
print([num * 2 for num in my_nums]) #[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
print(", ".join([str(num * 2) for num in my_nums])) # 0, 2, 4, 6, 8, 10, 12, 14, 16, 18

print("____________________________")

#list comprehensions
list_comp = [x ** 2 for x in range (10) if x % 2 == 0]
print("list comp:", list_comp)

superman = [num for num in range(0,20) if num % 2 == 0]
batman = [num for num in range(0,100) if num % 5 == 0]
print('superman', superman)
print('batman', batman)

my_dict = {num:random.randint(0,25) for num in superman}
print('MY_DICT', my_dict)

my_set = {num for num in my_dict.values()} #will contain the values the dictionary has
print('MY_SET', my_set)

# superman [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]
# batman [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
# MY_DICT {0: 18, 2: 22, 4: 18, 6: 19, 8: 12, 10: 3, 12: 23, 14: 20, 16: 7, 18: 25, 20: 5, 22: 0, 24: 24, 26: 4, 28: 4, 30: 21, 32: 11, 34: 15, 36: 9, 38: 11, 40: 14, 42: 7, 44: 3, 46: 17, 48: 13, 50: 1, 52: 6, 54: 24, 56: 19, 58: 5, 60: 19, 62: 21, 64: 8, 66: 19, 68: 17, 70: 24, 72: 0, 74: 5, 76: 13, 78: 15, 80: 14, 82: 0, 84: 7, 86: 11, 88: 3, 90: 18, 92: 17, 94: 23, 96: 6, 98: 21}
# MY_SET {0, 1, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 17, 18, 19, 20, 21, 22, 23, 24, 25}

# generator expression
gen_exp = (x ** 2 for x in range(10) if x % 2 == 0)

print("GEN EXP:", gen_exp)

for num in gen_exp:
    print("NUM:", num)

# list comp: [0, 4, 16, 36, 64]
# gen exp: <generator object <genexpr> at 0x10613e0c0>
# num: 0
# num: 4
# num: 16
# num: 36
# num: 64

#GENERATORS ARE A ONCE AND DONE TYPE OF DEAL