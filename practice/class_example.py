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
print(vegan_gold)

print(f"{vegan_gold.variety} has been proven to grow in drought and is another formidable {vegan_gold.planttype}")

print(f"My vegan gold is a {type(vegan_gold)} and my most overgrown crop is a {type(most_overgrown_crop)}")

# My vegan gold is a <class '__main__.Soybeans'> and my most overgrown crop is a <class '__main__.Crop'>

print(f"Is my most overgrown crop a crop?? {isinstance(most_overgrown_crop, Crop)}")
# Is my most overgrown crop a crop?? True

print(f"is my wheat a Crop?? {isinstance(Wheat, Crop)}")
# is my wheat a Crop?? False. NOT an instance of Crop

print(f"is my Soybeans a Crop?? {isinstance(Soybeans, Crop)}")
# is my soybeans a Crop?? False. NOT an instance of Crop

print(f"is my wheat a C")
