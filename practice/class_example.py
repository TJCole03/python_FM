class Crop:

    # usa_originated = True

    def __init__(self, crop_name, family, seed_type, plant_type, variety):
        self.name = crop_name
        self.family = family
        self.seedtype = seed_type
        self.planttype = plant_type
        self.variety = variety

#Instance of Crop
most_overgrown_crop = Crop('Corn', 'Poaceae', 'monocot', 'determinate', 'Signature XR')
# print(most_overgrown_crop)
# most_overgrown_crop.usa_originated = False

# print(f"Can we please begin growing less {most_overgrown_crop.name}????")

# intance variables
# print(f"You need to stop growing so much {most_overgrown_crop.name}!! These {most_overgrown_crop.seedtype} are oversaturating the market! And your seeds {most_overgrown_crop.usa_originated}ly represented to come from the US!")

# class variables
# print(f"Is it {Crop.usa_originated} most seeds are from Canada?")
# print(f"Is it {most_overgrown_crop.usa_originated} most seeds are from Canada?")

#INHERITANCE

class Soybeans(Crop):

    usa_originated = False
    roundup_ready = True

class Wheat(Crop):

    usa_originated = True
    winter_grown = True

    def __init__(self, crop_name, family, seed_type, plant_type, variety):
        super().__init__(crop_name, family, seed_type, plant_type, variety)

# instance of Soybeans which inherits from Crop 
vegan_gold = Soybeans('Soybeans', 'Fabaceae', 'dicot', 'hybrid','AG005XF1')
print(f"{vegan_gold.variety} has been proven to grow in drought and is another formidable {vegan_gold.planttype}")

new_crop = Crop('Sorghum', 'Poaceae', 'Monocot', 'Hybrid', 'S. Bicolor')
print(f"I grow {new_crop.name} in the {new_crop.family} family")

print(f"My vegan gold is a {type(vegan_gold)} and my most overgrown crop is a {type(most_overgrown_crop)}")
# My vegan gold is a <class '__main__.Soybeans'> and my most overgrown crop is a <class '__main__.Crop'>

print(f"My vegan gold is a {type(vegan_gold)} and my NEW CROP is a {type(new_crop)}")
#My vegan gold is a <class '__main__.Soybeans'> and my NEW CROP is a <class '__main__.Crop'>

print(f"Is my most overgrown crop a crop?? {isinstance(most_overgrown_crop, Crop)}")
# Is my most overgrown crop a crop?? True

print(f"is my wheat a Crop?? {isinstance(Wheat, Crop)}")
# is my wheat a Crop?? False. NOT an instance of Crop

print(f"is my Soybeans a Crop?? {isinstance(Soybeans, Crop)}")
# is my soybeans a Crop?? False. NOT an instance of Crop

# a = 1 / 0
# print(a)

# 2 + "3"
# my_dict = {"hello": "world"}
# my_dict["foo"]
# my_dict.append("foo")

# try: 
#     new_dict = {"hey": "dude"}
#     print(new_dict['foo'])
# except KeyError:
#      print("oops! the key doesn't exist :(")
# ... oops! the key doesn't exist :(

# try: 
#     new_dict = {"hey": "dude"}
#     print(new_dict['foo'])
# except KeyError as key_error:
#      print(f"oops! the key {key_error} doesn't exist :(")
# oops! the key 'foo' doesn't exist :(


#EXCEPTIONS

try:
     int("a")
except ValueError:
     print("Oops, couldn't convert that value into an int!")

print("1-End of program reached")
# Oops, couldn't convert that value into an int!
# 1-End of program reached

try:
     int("a")
except ValueError as error:
     print(f"Something went wrong. Message: {error}")

print("2-End of program reached")
# Something went wrong. Message: invalid literal for int() with base 10: 'a'
# 2-End of program reached


class MyException(Exception):
    def __init__(self, message):
            new_message = f"!!!ERROR!!! {message}"
            super().__init__(new_message)
raise MyException("Someting went wrong")

