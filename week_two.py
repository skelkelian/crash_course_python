print(7+8)
print("hello " + "world")

# print("hi" + 8)
# can't add a string and
# an integer because they
# are two different dataypes

print(type("a"))
print(type(2))
print(type(2.5))

length = 10
width = 2
area_rectangle = length * width
print(area_rectangle)

base = 5
height = 3
area_triangle = (base*height)/2
print(area_triangle)

# print = 2
# print(print)
# can't do this because python
# doesn't allow you to use
# keywords/functions as variable names

Serop = 3
serop = 1
sErop = 4
serOp = 6
# these are all different variables
# because python is case sensitive

print(5+4.3)
# works because of implicit conversion

radius = 3
pi = 3.14159
area_circle = radius**2 * pi
print("the area of the circle is: " + str(area_circle))
# this works because we explicitly
# converted the area to a string so
# we could print the sentence and the value

total_size_of_files = 2048 + 4357 + 97658 + 125 + 8
files = 5
average = total_size_of_files / files
print("The average size is: " + str(average))

bill = 47.28
tip = bill * .15
total = bill + tip
share = total/2
print("Each person needs to pay: " + str(share))

word1 = "How "
word2 = "do "
word3 = "you "
word4 = "like "
word5 = "Python "
word6 = "so "
word7 = "far?"

print(word1 + word2 + word3 + word4 + word5 + word6 + word7)

def greeting(name):
    print("Welcome, " + name)
greeting("rop")
greeting("robert")
greeting("samvel")

def greeting_work(name, department):
    print("Welcome, " + name + ". You are part of " + department)
greeting_work("serop", "Tech Support")

def print_seconds(hours, minutes, seconds):
    print(hours*3600 + minutes*60 + seconds)
print_seconds(1,2,3)

def area_triangle(base, height):
    return base*height/2
area_a = area_triangle(5,4)
area_b = area_triangle(6,2)
sum = area_a + area_b
print("The sum of both areas is: " + str(sum))

def get_seconds(hours, minutes, seconds):
    return 3600*hours + 60*minutes + seconds
amount_a = get_seconds(2, 30, 0)
amount_b = get_seconds(0, 45, 15)
result = amount_a + amount_b
print(result)

def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = (seconds - hours * 3600 - minutes * 60)
    return hours, minutes, remaining_seconds
hours, minutes, seconds = convert_seconds(5645)
print(hours, minutes, seconds)
print("There are " + str(hours) + " hours, " + str(minutes) + " minutes and " + str(seconds) + " seconds.")
# if you want to set a variable when you call a function
# like we did above, you must call return or else the
# value of the results will be none

def lucky_number(name):
    lucky_number = len(name) * 3
    print("Hello " + name + ". Your lucky number is " + str(lucky_number))
lucky_number("Serop")

def month_days(month, days):
    print(month + " has " + str(days) + " days.")
month_days("June", 30)
month_days("July", 31)

def convert_distance(miles):
    km = miles * 1.6  # approximately 1.6 km in 1 mile
my_trip_miles = 55
my_trip_km = my_trip_miles * 1.6
print("The distance in kilometers is " + str(my_trip_km))
print("The round-trip in kilometers is " + str(2 * my_trip_km))

def order_numbers(number1, number2):
    if number2 > number1:
        return number1, number2
    else:
        return number2, number1
smaller, bigger = order_numbers(100, 99)
print(smaller, bigger)

print(10>1)
print('e'>'i')
# goes in alphabetical order 'a'
# being least,'z' being greatest
print('cat' > 'Cat')
# In Python uppercase letters are alphabetically
# sorted before lowercase letters
print(1!=2)
print(1==2)
# print(1 < '1') because you can't compare str and int
print(1!='1')
# will give you an answer because computer
# knows int and str are not the same
print("Yellow">"Cyan" and 1>2) # both must be true
print(1==1 or 2>1) # only one must be true
print(not 42 == 30) # inverts value of expression

def is_even_number(number):
    if number % 2 == 0:
        # "%" is modulo, it returns
        # the remainder of number % 2
        print("True")
    print("False")
is_even_number(5)

def is_positive(number):
    if number>0:
        return True
        # why did we do return here
        # instead of print? We never
        # called it after, we just
        # wanted to print it.
print(is_positive(4))
print(is_positive(-1))

def username_check(username):
    if len(username)<=3:
        print("Username must be over 3 characters")
    elif len(username)>=15:
        print("Username must be under 15 characters")
    else:
        print("Valid username")
username_check('skelkelian')
username_check("ae")
username_check("qwertyuiopasdfgh")

def calculate_storage(filesize):
    block_size = 4096
    # Use floor division to calculate how many blocks are fully occupied
    full_blocks = filesize // 4096
    # Use the modulo operator to check whether there's any remainder
    partial_block_remainder = filesize % 4096
    # Depending on whether there's a remainder or not, return
    # the total number of bytes required to allocate enough blocks
    # to store your data.
    if partial_block_remainder > 0:
        return full_blocks * block_size + 4096
    return full_blocks * block_size

print(calculate_storage(1))    # Should be 4096
print(calculate_storage(4096)) # Should be 4096
print(calculate_storage(4097)) # Should be 8192
print(calculate_storage(6000)) # Should be 8192

def color_translator(color):
    if color == "red":
        hex_color = "#ff0000"
    elif color == "green":
        hex_color = "#00ff00"
    elif color == "blue":
        hex_color = "#0000ff"
    else:
        hex_color = "unknown"
    return hex_color

print(color_translator("blue")) # Should be #0000ff
print(color_translator("yellow")) # Should be unknown
print(color_translator("red")) # Should be #ff0000
print(color_translator("black")) # Should be unknown
print(color_translator("green")) # Should be #00ff00
print(color_translator("")) # Should be unknown

def exam_grade(score):
    if score > 95:
        grade = "Top Score"
    elif score >= 60:
        grade = "Pass"
    else:
        grade = "Fail"
    return grade

print(exam_grade(65)) # Should be Pass
print(exam_grade(55)) # Should be Fail
print(exam_grade(60)) # Should be Pass
print(exam_grade(95)) # Should be Pass
print(exam_grade(100)) # Should be Top Score
print(exam_grade(0)) # Should be Fail

def format_name(first_name, last_name):
    if first_name != '' and last_name !='':
        return ("Name: " + first_name + ", " + last_name)
    elif first_name != '' or last_name !='':
        return ("Name: " + first_name + last_name)
    else:
        return ''

#     my code
# def format_name(first_name, last_name):
#   if first_name != '' and last_name !='':
#      return ("Name: " + first_name + ", " + last_name)
#   elif first_name != '' or last_name !='':
#      return ("Name: " + first_name + last_name)
#   else:
#      return ''
#
# print(format_name("Ernest", "Hemingway"))
# # Should return the string "Name: Hemingway, Ernest"
#
# print(format_name("", "Madonna"))
# # Should return the string "Name: Madonna"
#
# print(format_name("Voltaire", ""))
# # Should return the string "Name: Voltaire"
#
# print(format_name("", ""))
# # Should return an empty string

# WHY DID I GET A BUNCH OF WEIRD STUFF AND NONE?
print(format_name("Ernest", "Hemingway"))
# Should return the string "Name: Hemingway, Ernest"
print(format_name("", "Madonna"))
# Should return the string "Name: Madonna"
print(format_name("Voltaire", ""))
# Should return the string "Name: Voltaire"
print(format_name("", ""))
# Should return an empty string

def longest_word(word1, word2, word3):
    if len(word1) >= len(word2) and len(word1) >= len(word3):
        word = word1
    elif len(word2) >= len(word1) and len(word2) >= len(word3):
        word = word2
    else:
        word = word3
    return(word)
print(longest_word("chair", "couch", "table"))
print(longest_word("bed", "bath", "beyond"))
print(longest_word("laptop", "notebook", "desktop"))

def fractional_part(numerator, denominator):
    if denominator != 0:
        return (numerator % denominator) / denominator
    return 0
print(fractional_part(5, 5)) # Should be 0
print(fractional_part(5, 4)) # Should be 0.25
print(fractional_part(5, 3)) # Should be 0.66...
print(fractional_part(5, 2)) # Should be 0.5
print(fractional_part(5, 0)) # Should be 0
print(fractional_part(0, 5)) # Should be 0
# my code
# if denominator == 0:
#     return 0
#   else:
#     print((numerator / denominator) - (numerator // denominator))