# print(dir(""))
# returns a list of valid attributes of the object

# help("")
# help returns the syntax of a bunch of methods of
# the object and provides an explanation of what
# each one does and its parameters (type q to quit)




class Apple:
    pass # pass shows body is empty

class Apple:
    color = ""
    flavor = ""

jonagold = Apple()
# created a new instance of the Apple class
# and assigned to variable called 'jonagold'
jonagold.color = "red"
# sets the attribute "color" of jonagold instance to red
jonagold.flavor = "sweet"
# sets the attribute "flavor" of jonagold instance to sweet
print(jonagold.color)
print(jonagold.flavor)
print(jonagold.flavor.upper())

golden = Apple()
# golden is an instance of the Apple class
golden.color = "yellow"
golden.flavor = "soft"

# jonagold and golden are both instances of the Apple
# class they both have the same attributes (color, flavor)
# however, those attributes have different values




class Flower:
    color = ""
rose = Flower()
rose.color = "red"
violet = Flower()
violet.color = "blue"
last_line = "this pun is for you"
print("Roses are {},".format(rose.color))
print("violets are {},".format(violet.color))
print(last_line)




class Person:
    apples = 0
    ideas = 0

johanna = Person()
johanna.apples = 1
johanna.ideas = 1

martin = Person()
martin.apples = 2
martin.ideas = 1

def exchange_apples(you, me):
    save_johanna_apples =  johanna.apples
    save_martin_apples = martin.apples
    # created new variables to save their respective apple counts
    johanna.apples = save_martin_apples
    martin.apples = save_johanna_apples
    # set martin's apples equal to johanna's save
    # and johanna's apples to martin's save

def exchange_ideas(you, me):
    save_johanna_ideas = johanna.ideas
    save_martin_ideas = martin.ideas
    you.ideas += save_martin_ideas
    me.ideas += save_johanna_ideas
    return you.ideas, me.ideas

exchange_apples(johanna, martin)
print("Johanna has {} apples and Martin has {} apples".format(johanna.apples, martin.apples))
exchange_ideas(johanna, martin)
print("Johanna has {} ideas and Martin has {} ideas".format(johanna.ideas, martin.ideas))




class Furniture:
    color = ""
    material = ""

table = Furniture()
table.color = "brown"
table.material = "wood"

couch = Furniture()
couch.color = "red"
couch.material = "leather"

def describe_furniture(piece):
    return ("This piece of furniture is made of {} {}".format(piece.color, piece.material))

print(describe_furniture(table))
# Should be "This piece of furniture is made of brown wood"
print(describe_furniture(couch))
# Should be "This piece of furniture is made of red leather"



# QUESTIONS FOR KERI

# QUESTION ONE:
# AT CITY_CLASS_QUESTION, COULD YOU EXPLAIN WHAT
# IS GOING ON IN MAX_ELEVATION_CITY FUNCTION?
