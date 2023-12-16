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

#list comprehension
list_comp = [x ** 2 for x in range (10) if x % 2 == 0]
print("list comp:", list_comp)

# generator expression
gen_exp = (x ** 2 for x in range(10) if x % 2 == 0)

print("gen exp:", gen_exp)

for num in gen_exp:
    print("num:", num)

# list comp: [0, 4, 16, 36, 64]
# gen exp: <generator object <genexpr> at 0x10613e0c0>
# num: 0
# num: 4
# num: 16
# num: 36
# num: 64

#GENERATORS ARE A ONCE AND DONE TYPE OF DEAL