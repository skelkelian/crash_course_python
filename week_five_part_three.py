class Fruit:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor
        # why do we put "self." in front of color and flavor?
        # what does that do for us

class Apple(Fruit):
    pass
# when you put fruit in parentheses after a class
# (apple), it shows an inheritance relationship

class Grape(Fruit):
    pass
# think of fruit class as parent class and
# the apple and grape class as siblings
granny_smith = Apple("green", "tart")
carnelian = Grape("purple", "sweet")
print("The color of the granny smith apple is {} and the flavor is {}".format(granny_smith.color, granny_smith.flavor))
print("The color of the carnelian grape is {} and the flavor is {}".format(carnelian.color, carnelian.flavor))



class Animal:
    sound: ""
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("{sound} I'm {name}! {sound}".format(name = self.name, sound = self.sound))
        # what does self do here and why does self
        # automatically get attached on some functions?

class Piglet(Animal):
    sound = "Oink!"
hamlet = Piglet("Hamlet") # pass the name into the Piglet class
hamlet.speak()

class Cow(Animal):
    sound = "Mooooo"
milky = Cow("Milky White")
milky.speak()

# both sibling classes can inherit from the base animal class and use
# both the attributes and the methods that the animal class provides



class Clothing: # create parent class "clothing"
    material = "" # have empty string material which we will fill later
    def __init__(self,name):
    # create the constructor of the class
    # this is where you call the name of the class
        self.name = name
    def checkmaterial(self):
    # create new method in clothing class which prints what material it is
        print("This {} is made of {}".format(self.name,self.material))

class Shirt(Clothing): # create sibling class "shirt"
    material="Cotton" # pass in what material it is

polo = Shirt("Polo")
polo.checkmaterial()



class Repository:
    def __init__(self): # why didn't we pass in anything, it's just self?
        self.packages = {}
        # always initialize mutable attributes in the constructor
        # this is because it will be the same for every sibling class and
        # we want each sibling class to have a different value if needed
    def add_package(self, package):
        self.packages[package.name] = package
    def remove_package(self, package):
        del self.packages[package]
    def total_size(self):
        result = 0
        for package in self.packages.values():
            result += package.size # but where does size come from?
        return result
# could you explain composition to me?
# maybe we can watch the composition video together?



class Clothing:
    stock={ 'name': [],'material' :[], 'amount':[]}
    def __init__(self,name):
        material = ""
        self.name = name
    def add_item(self, name, material, amount):
        Clothing.stock['name'].append(self.name)
        Clothing.stock['material'].append(self.material)
        Clothing.stock['amount'].append(amount)
    def Stock_by_Material(self, material):
        count=0
        n=0
        for item in Clothing.stock['material']:
            if item == material:
                count += Clothing.stock['amount'][n]
                n+=1
        return count
class shirt(Clothing):
    material="Cotton"
class pants(Clothing):
    material="Cotton"
polo = shirt("Polo")
sweatpants = pants("Sweatpants")
polo.add_item(polo.name, polo.material, 4)
sweatpants.add_item(sweatpants.name, sweatpants.material, 6)
current_stock = polo.Stock_by_Material("Cotton")
print(current_stock)

import random
print(random.randint(1,10)) # random number between 1-10 (includes 10)
# use name of module then . then the function provided by module (name.function)

import datetime
time = datetime.datetime.now()
print(type(time))
print(time) # full date
print(time.year) # just year
print(time + datetime.timedelta(days = 28)) # date 28 days into the future

# datetime module provides datetime class
# and the datetime class gives method "now"
# "now" method generates instance of datetime class for current time

# QUESTIONS FOR KERI

# QUESTION ONE:
# LINE 5-6

# QUESTION TWO:
# LINE 30

# QUESTION THREE:
# LINE 67-71