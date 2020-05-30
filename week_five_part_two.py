class Piglet:
    """Represents a piglet that can say its name"""
    name = "piggy"
    def speak(self):
        """Outputs a message including name of the piglet"""
        print("Oink! I'm {}! Oink!".format(self.name))
    years = 0
    def pig_years(self):
        """Converts the current age to equivalent pig years."""
        return self.years * 18
help(Piglet) # ALWAYS USE THE CLASS NAME IF YOU ARE CALLING HELP
hamlet = Piglet()
hamlet.name = "Hamlet"
hamlet.years = 2
hamlet.speak()
print(hamlet.pig_years())

petunia = Piglet()
petunia.name = "Petunia"
petunia.years = 4
petunia.speak()
print(petunia.pig_years())



class Dog:
    years = 0
    def dog_years(self):
        return self.years * 7
fido=Dog()
fido.years=3
print("Fido is " + str(fido.dog_years()) + " years old!")



class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor
    def __str__(self):
        # this method allows us to print a user friendly
        # message when print(jonagold) is called
        # define str method when creating objects you want to print
        return "This apple is {} and its flavor is {}".format(self.color, self.flavor)

jonagold = Apple("red", "sweet")
print(jonagold.color)
print(jonagold.flavor)
print(jonagold)


class Person:
    def __init__(self, name):
        self.name = name
    def greeting(self):
        """Outputs a message with the name of the person"""
        # Should return "hi, my name is " followed by the name of the Person.
        return "hi, my name is " + self.name
# Create a new instance with a name of your choice
human = Person("Alex")
# Call the greeting method
print(human.greeting())
# Call the help method
help(Person)

def to_seconds(hours, minutes, seconds):
    """Returns the amount of seconds in the given hours, minutes and seconds."""
    # created a docstring using triple quotes which prints
    # whatever is in the triple quotes when user calls help
    return hours * 3600 + minutes * 60 + seconds

help(to_seconds)


# NO QUESTIONS FOR KERI
