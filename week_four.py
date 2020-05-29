name = 'sasha'
print(name * 3)
print(len(name)) # why does this need a print function to show the length?

def double_word(word):
    return 2 * word + str(len(2 * word))

print(double_word("hello")) # Should return hellohello10
print(double_word("abc"))   # Should return abcabc6
print(double_word(""))      # Should return 0

name = "Jaylen"
print(name[0])
# python starts counting indexes at
# 0, not 1 just like it does for range
print(name[1])
# print(name[6]) will give you an index error because the string is out of range
print(name[-1])
# the negative index will start from
# the back and it goes from -1 onwards

# This checks if the first character of a message
# is the same as the last character of a message
def first_and_last(message):
    if message == "":
        return True
    elif message[0] == message[-1]:
        return True
    else:
        return False
print(first_and_last("else"))
print(first_and_last("tree"))
print(first_and_last(""))

color = "Orange"
print(color[1:4]) # this prints index characters 1-4 (like range function)
print(color[:4]) # this prints every index character until 4 (0-4)
print(color[:10])
# if you put a number that is larger than the length
# of the message, it will print the entire message
print(color[4:]) # this prints every index character from 4 onwards (4-end)
print(color[2:10])
# if you put a number that is larger than the length
# of the message, it will print the entire message

message = 'A kong string with a typo'
# message[2] = 'l' will not work because strings in python are immutable
new_message = message[0:2] + "l" + message[3:]
# explain why it is [0:2] and is not [0:1]
print(new_message)
# or
message = 'A long string without a new typo' # just changed the string

pets = "Cats & Dogs"
print(pets.index("&")) # again why do I need to specify print here?
# scans for the first location where a certain value is
# in the string in this case "&" and returns its index
print(pets.index("Dog")) # prints the where D is in this case
# print(pets.index("x"))
# if the character is not in the string it will
# give you "ValueError: substring not found"

print("Dragons" in pets) # checks if "Dragons" is in pets
print("Cats" in pets) # checks if "Cats" is in pets
# will return true if it is in pets and false if not in pets
# keep in mind it is case sensitive

def replace_domain(email, old_domain, new_domain):
    if "@" + old_domain in email:
        index = email.index("@" + old_domain)
        new_email = email[:index] + "@" + new_domain
        return new_email
    return email
    # if email did not need to be changed you just return the email as is
print(replace_domain("skelkelian88@hotmail.com", "hotmail.com", "gmail.com"))
# WHY DO I NEED TO PUT PRINT HERE?!?

emails = ["skelkelian88@gmail.com", "rompytomp@yahoo.com", "ahsqwerty@hotmail.com"]
for email in emails:
    new_email = replace_domain(email, 'yahoo.com', 'gmail.com')
    print(new_email)

print("Mountains".upper()) # all caps everything
print("Mountains".lower()) # all lowercase everything

answer = 'YEs'
if answer.lower() == 'yes':
# changes the answer to lowercase to check if it is yes
    print("User said yes")

print(" yes ".strip())
# this gets rid of whitespace (space before or after
# the first non-space character in the string)
print(" yes ".lstrip()) # gets rid of whitespace on left side
print(" yes ".rstrip()) # gets rid of whitespace on right side

print("The number of times I have said e in this string is".count("e"))
# count tells you how many times a string occurs in another string

print("Forest".endswith("rest"))
# endswith tells you if a string ends with another string (true/false)

print("Forest".isnumeric()) # false
print("Forest123".isnumeric()) # false
print("12345".isnumeric()) # true
# tells you if the string is made up of just numbers

print(int("1234"))
# int converts a string of just numbers to actual number

print(" ".join(["This", "list", "gets", "spaces", "from", ".join"]))
print("...".join(["this", "is", "a", "phrase", "joined", "by", "triple", "dots"]))
# .join creates a new string by taking the input string
# and inserting it in between each element of the list
# in the first situation, it put a space between each element in the list
# in the second situation, it put a ... in between each element in the list

print("This is an example".split())
print("This is an example".split("i"))
# split method will split a string into a list of strings
# by every whitespace you can also give it a parameter to
# split by but it splits by whitespace by default

def initials(phrase):
    words = phrase.split()
    # splits the phrase into a list of words
    result = ""
    for word in words:
        result += word[0].upper()
        # takes first letter of each word and makes it uppercase
    return result
print(initials("Universal Serial Bus")) # Should be: USB
print(initials("local area network")) # Should be: LAN
print(initials("Operating system")) # Should be: OS

name = 'Serop'
number = len(name) * 3
print("Hello {} your lucky number is {}".format(name, number))
# or
print("Your lucky number is {number}, {name}.".format(name = name, number = len(name) * 3))

def student_grade(name, grade):
    return "{} received {}% on the exam.".format(name, grade)
print(student_grade("Reed", 80))
print(student_grade("Paige", 92))
print(student_grade("Jesse", 85))

def price_with_tax(price, tax):
    with_tax = price * 1.09
    print("With tax: ${:.2f} Without tax: ${:.2f}".format(with_tax, price))
price_with_tax(6, 1.09)

def to_celsius(x):
    return (x - 32) * 5 / 9
for x in range(0, 101, 10):
    print("{:>3} F | {:>6.2f} C".format(x, to_celsius(x)))

def is_palindrome(input_string):
    # We'll create two strings, to compare them
    new_string = ""
    reverse_string = ""
    # Traverse through each letter of the input string
    for character in input_string.lower():
        # Add any non-blank letters to the
        # end of one string, and to the front
        # of the other string.
        if character != " ": # checks if the letter/character is a space
            new_string = new_string + character
            reverse_string = character + reverse_string
    # Compare the strings
    if new_string == reverse_string:
        return True
    return False
print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True

def convert_distance(miles):
    km = miles * 1.6
    result = "{} miles equals {:.1f} km".format(miles, km)
    return result
print(convert_distance(12)) # Should be: 12 miles equals 19.2 km
print(convert_distance(5.5)) # Should be: 5.5 miles equals 8.8 km
print(convert_distance(11)) # Should be: 11 miles equals 17.6 km

def nametag(first_name, last_name):
    return("{first_name} {last_name}.".format(first_name = first_name, last_name = last_name[0]))
print(nametag("Jane", "Smith"))
# Should display "Jane S."
print(nametag("Francesco", "Rinaldi"))
# Should display "Francesco R."
print(nametag("Jean-Luc", "Grand-Pierre"))
# Should display "Jean-Luc G."

def replace_ending(sentence, old, new):
    # Check if the old string is at the end of the sentence
    if sentence.endswith(old):
        # Using i as the slicing index, combine the part
        # of the sentence up to the matched string at the
        # end with the new string
        i = len(old) # gets length of old word
        new_sentence = sentence[:-i] + new
        # creates a new sentence with everything up until the
        # backwards length of i and replaces it with the new word
        return new_sentence
    # Return the original sentence if there is no match
    return sentence
print(replace_ending("It's raining cats and cats", "cats", "dogs"))
# Should display "It's raining cats and dogs"
print(replace_ending("She sells seashells by the seashore", "seashells", "donuts"))
# Should display "She sells seashells by the seashore"
print(replace_ending("The weather is nice in May", "may", "april"))
# Should display "The weather is nice in May"
print(replace_ending("The weather is nice in May", "May", "April"))
# Should display "The weather is nice in April"

c = ['cook', 'bake', 'sautee', 'cookie']
print(type(c))
print(c)
print(len(c))
print("cook" in c)
print(c[0])
# print(c[5]) gives IndexError because list index is out of range
print(c[1:3])

def get_word(sentence, n):
    # Only proceed if n is positive
    if n > 0:
        words = sentence.split()
        # Only proceed if n is not more than the number of words
        if n <= len(words):
            return(words[n-1])
    return("")
print(get_word("This is a lesson about lists", 4)) # Should print: lesson
print(get_word("This is a lesson about lists", -4)) # Nothing
print(get_word("Now we are cooking!", 1)) # Should print: Now
print(get_word("Now we are cooking!", 5)) # Nothing

fruits = ['Kiwi', 'Apple', 'Mango']
fruits.append("Melon") # adds an element to a list
fruits.insert(0, "Orange")
fruits.insert(244, "Strawberry")
# inserts an element to a list at a certain location
# if you insert at a number that is too big,
# it just puts the element at the end
fruits.remove("Apple") # removes an element from a list
# fruits.remove("Pear") if it is not there, you get ValueError
fruits.pop(1) # removes an element at the index passed
fruits[0] = "Pineapple" # modifies an element of a list
print(fruits)

fullname = ('Serop', 'G', 'Kelkelian') # tuple is immutable

def file_size(file_info):
    name, type, size= file_info
    return("{:.2f}".format(size / 1024))
print(file_size(('Class Assignment', 'docx', 17875))) # Should print 17.46
print(file_size(('Notes', 'txt', 496))) # Should print 0.48
print(file_size(('Program', 'py', 1239))) # Should print 1.21

animals = ["Lion", "Zebra", "Dolphin", "Monkey"]
characters = 0
for animal in animals:
    characters += len(animal)
print("Total characters: {} Average length: {}".format(characters, characters/len(animals)))

winners = ["Ashley", "Dylan", "Reese"]
for index, winner in enumerate(winners):
# enumerate returns a tuple for each element in the list
    print("{} - {}".format(index + 1, winner))

def full_emails(people):
    result = []
    for email, name in people:
        result.append("{} <{}>".format(name, email))
    return result
print(full_emails([("alex@example.com", "Alex Diego"), ("shay@gmail.com", "Shay Brandt")]))

multiples = [ x * 7 for x in range(1, 11)]
# for each x in range 1-10, do x * 7
print(multiples)

languages = ["Python", "Perl", "Ruby", "Go", "Java", "C"]
lengths = [len(language) for language in languages]
# for each language in languages, get the length of language
print(lengths)

z = [x for x in range(0,101) if x % 3 == 0]
# explain why the if statement doesnt have colon at end
print(z)

# list comprehensions lets you create new
# lists based on sequences or ranges

def odd_numbers(n):
    return [x for x in range(1, n+1) if x % 2 != 0]
print(odd_numbers(5))  # Should print [1, 3, 5]
print(odd_numbers(10)) # Should print [1, 3, 5, 7, 9]
print(odd_numbers(11)) # Should print [1, 3, 5, 7, 9, 11]
print(odd_numbers(1))  # Should print [1]
print(odd_numbers(-1)) # Should print []

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.

newfilenames = []
for x in range(len(filenames)):
    old_name = filenames[x]
    if old_name.endswith(".hpp"):
        new_name = old_name.replace('.hpp','.h')
    else:
        new_name = old_name;
    newfilenames.append((new_name))
print(newfilenames)
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]

def pig_latin(text):
    say = ""
    # Separate the text into words
    words = text.split()
    for word in words:
        # Create the pig latin word and add it to the list
        texts = word[1:] + word[0] + "ay "
        say += texts
    return say
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"

def octal_to_string(octal):
    result = ""
    value_letters = [(4,"r"),(2,"w"),(1,"x")]
    # Iterate over each of the digits in octal
    for x in [int(n) for n in str(octal)]:
        # Check for each of the permissions values
        for value, letter in value_letters:
            if x >= value:
                result += letter
                x -= value
            else:
                result += '-'
    return result
print(octal_to_string(755)) # Should be rwxr-xr-x
print(octal_to_string(644)) # Should be rw-r--r--
print(octal_to_string(750)) # Should be rwxr-x---
print(octal_to_string(600)) # Should be rw-------

def group_list(group, users):
    members = ", ".join(users)
    return "{}: {}".format(group, users)
print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", "")) # Should be "Users:"

def guest_list(guests):
    for guest in guests:
        print('{name} is {age} years old and works as {profession}'.format(name = guest[0], age = guest[1], profession = guest[2]))
guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])

def guest_list(guests):
    for guest in guests:
        name, age, profession = guest
        print('{} is {} years old and works as {}'.format(name, age, profession))
guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])

x = {}
print(type(x))

file_counts = {"jpg": 10, "txt": 14, "csv": 2, "py": 23}
print(file_counts)
print(file_counts["txt"])
print("jpg" in file_counts)
print("html" in file_counts)
file_counts["cfg"] = 8 # adds cfg as key and puts it at end of dictionary
file_counts["csv"] = 17 # changes the value of csv because it already exists
print(file_counts)
del file_counts["cfg"] # deletes a key and its corresponding value from dictionary
print(file_counts)

toc = {"Introduction":1, "Chapter 1":4, "Chapter 2":11, "Chapter 3":25, "Chapter 4":30}
toc["Epilogue"] = 39 # Epilogue starts on page 39
toc["Chapter 3"] = 24 # Chapter 3 now starts on page 24
print(toc) # What are the current contents of the dictionary?
print("Chapter 5" in toc) # Is there a Chapter 5?

file_counts = {"jpg": 10, "txt": 14, "csv": 2, "py": 23}
for extension in file_counts:
    print(extension)
for ext, amount in file_counts.items():
# .items() takes the keys and values (key value pairs) of a dictionary
    print("There are {} files with the .{} extension".format(amount, ext))
print(file_counts.keys())
print(file_counts.values())
for value in file_counts.values():
    print(value)

cool_beasts = {"octopuses":"tentacles", "dolphins":"fins", "rhinos":"horns"}
for animal, trait in cool_beasts.items():
    print("{} have {}".format(animal, trait))

def count_letters(text):
    result = {}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
    return result
print(count_letters("myaaaaa what"))

def email_list(domains):
    emails = []
    for names, users in domains.items():
        for user in users:
            emails.append(user+"@"+names)
    return(emails)
print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))

def groups_per_user(group_dictionary):
    user_groups = {}
    # Go through group_dictionary
    for group, users in group_dictionary.items():
        # Now go through the users in the group
        for user in users:
            if user not in user_groups:
                user_groups[user] = []
            user_groups[user].append(group)
            # what does this if statement do?
    return(user_groups)
print(groups_per_user({"local": ["admin", "userA"], "public":  ["admin", "userB"], "administrator": ["admin"] }))

def add_prices(basket):
    # Initialize the variable that will be used for the calculation
    total = 0
    # Iterate through the dictionary items
    for price in basket.values():
        # Add each price to the total calculation
        # Hint: how do you access the values of
        # dictionary items?
        total += price
    # Limit the return value to 2 decimal places
    return round(total, 2)
groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59,
             "coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}
print(add_prices(groceries)) # Should print 28.44

def format_address(address_string):
    # Declare variables
    number = ''
    name = ''
    # Separate the address string into parts
    splits = address_string.split()
    # Traverse through the address parts
    for portion in splits:
        # Determine if the address part is the
        # house number or part of the street name
        if portion.isnumeric():
            number = portion
        else:
            name += portion
            name += ' '
    # Return the formatted string
    return "house number {} on street named {}".format(number, name)
print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"
print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"
print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"

def highlight_word(sentence, word):
    # get the length of the word
    length = len(word)
    # get the location of the word in the sentence as an integer
    location = sentence.index(word)
    # print the sentence as normal until the word, insert the word
    # in caps then continue to print sentence after the word
    return(sentence[:location] + word.upper() + sentence[location+length:])
    # also instead of all that, I could have just used one line
    # return(sentence.replace(word,word.upper()))
print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))

def combine_lists(list1, list2):
    # Generate a new list containing the elements of list2
    # Followed by the elements of list1 in reverse order
    new_list = list2
    for i in reversed(range(len(list1))):
        new_list.append(list1[i])
    return new_list
Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]
print(combine_lists(Jamies_list, Drews_list))

def squares(start, end):
    return [ (x*x) for x in range(start,end + 1) ]
print(squares(2, 3)) # Should be [4, 9]
print(squares(1, 5)) # Should be [1, 4, 9, 16, 25]
print(squares(0, 10)) # Should be [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

def car_listing(car_prices):
    result = ""
    for car, price in car_prices.items():
        result += "{} costs {} dollars".format(car, price) + "\n"
    return result
print(car_listing({"Kia Soul":19000, "Lamborghini Diablo":55000, "Ford Fiesta":13000, "Toyota Prius":24000}))

def combine_guests(guests1, guests2):
    # Combine both dictionaries into one, with each key listed
    # only once, and the value from guests1 taking precedence
    new_list = Rorys_guests
    for name in guests2:
        if name in guests1:
            pass
        else:
            new_list[name] = guests2[name]
    return new_list
Rorys_guests = { "Adam":2, "Brenda":3, "David":1, "Jose":3, "Charlotte":2, "Terry":1, "Robert":4}
Taylors_guests = { "David":4, "Nancy":1, "Robert":2, "Adam":1, "Samantha":3, "Chris":5}
print(combine_guests(Rorys_guests, Taylors_guests))

def count_letters(text):
    result = {}
    # Go through each letter in the text and lowercase it
    for letter in text:
        letter = letter.lower()
        # Check if the letter needs to be counted or not
        if letter.isalpha():
            # Add the letter into the result dictionary
            if letter in result:
                result[letter] += 1
            else:
                result[letter] = 1
    return result
print(count_letters("AaBbCc"))
# Should be {'a': 2, 'b': 2, 'c': 2}
print(count_letters("Math is fun! 2+2=4"))
# Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}
print(count_letters("This is a sentence."))
# Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}

# QUESTIONS FOR KERI

# QUESTION ONE:
# WHY DO I NEED TO USE PRINT FUNCTION IF I TYPE SOMETHING LIKE
# COLOR[1:4] OR LEN(NAME)? ** (SEE LINE 3, LINE 36, LINE 55 & LINE 74)

# QUESTION TWO:
# I MISSPELLED AN ERROR IN A MESSAGE ON PURPOSE TO TRY TO FIX IT HOWEVER,
# I AMD NOT SURE WHY THE RANGE IS THE WAY IT IS ** (SEE LINE 48)

# QUESTION THREE:
# COULD YOU TELL ME WHAT I AM DOING WRONG BY CREATING A FOR
# LOOP FOR THE REPLACE MULTIPLE DOMAINS FUNCTION AND WHY IT
# WON'T PRINT THE RESULTS? ** (SEE LINE 78 - 85)

# QUESTION FOUR:
# COULD YOU EXPLAIN LINE 157? I KNOW THAT
# IS FORMATTING BUT COULD U GO IN DETAIL?

# QUESTION FIVE:
# COULD YOU EXPLAIN WHY WE DID NOT USE A COLON
# AT THE END OF THE IF STATEMENT IN LINE 289?

# QUESTION SIX:
# WHY DOES LINES 356-365 REPEAT TWICE IN COURSERA QUIZ BUT NOT HERE?

# QUESTION SEVEN:
# COULD YOU EXPLAIN THE IF STATEMENT FROM LINES 408-410?

# QUESTION EIGHT:
# COULD YOU EXPLAIN THE IF STATEMENT FROM LINES 428-430?

# QUESTION NINE:
# I DON'T UNDERSTAND HOW TO REMOVE THE REVERSED FROM THE FOR LOOP
# AND GET THE NEGATIVE VALUE FROM LISTS IN LINES 488-497

# QUESTION TEN:
# EXPLAIN LINE 520 ESPECIALLY THE GUESTS2[NAME] PART

