x = 0
while x < 5:
    print("Not there yet, x=" + str(x))
    x=x+1
print("x=" + str(x))

def attempts(n):
    x = 1
    while x <= n:
        print("Attempt " + str(x))
        x += 1
    print("Done")
attempts(5)

# REMEMBER TO INITIALIZE YOUR VARIABLES

x = 1
sum = 0
while x < 10:
    sum += x
    x += 1

product = 1
x = 1
while x < 10:
    product *= x
    # product = product * x
    x += 1
print(sum, product)

def count_down(current):
    while (current > 0):
        print(current)
        current -= 1
    print("Zero!")
count_down(3)

# MAKE SURE LOOP IS NOT INFINITE

def infinite_loop_stop(x):
    if x != 0:
        while x % 2 == 0:
            x /= 2
    print(x)
infinite_loop_stop(8)

def print_prime_factors(number):
    # Start with two, which is the first prime
    factor = 2
    # Keep going until the factor is larger than the number
    while factor <= number:
        # Check if factor is a divisor of number
        if number % factor == 0:
            # If it is, print it and divide the original number
            print(factor)
            number = number / factor
        else:
            # If it's not, increment the factor by one
            factor = factor + 1
    return "Done"
print_prime_factors(100)
# Should print 2,2,5,5

def is_power_of_two(n):
    # Check if the number can be divided by two without a remainder
    if n != 0:
        while n % 2 == 0:
            n = n / 2
    # If after dividing by two the number is 1, it's a power of two
    if n == 1:
        return True
    return False
print(is_power_of_two(0)) # Should be False
print(is_power_of_two(1)) # Should be True
print(is_power_of_two(8)) # Should be True
print(is_power_of_two(9)) # Should be False

def sum_divisors(n):
    sum = 0
    if n == 0:
        return sum
    for possible_divisor in range(1, n-1):
        if n % possible_divisor == 0:
            sum += possible_divisor
    return sum
print(sum_divisors(0))
# 0
print(sum_divisors(3)) # Should sum of 1
# 1
print(sum_divisors(36)) # Should sum of 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102)) # Should be sum of 2+3+6+17+34+51
# 114

def multiplication_table(number):
    # Initialize the starting point of the multiplication table
    multiplier = 1
    # Only want to loop through 5
    while multiplier <= 5:
        result = number * multiplier
        # What is the additional condition to exit out of the loop?
        if result > 25 :
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))
        # Increment the variable for the loop
        multiplier += 1
multiplication_table(3)
# Should print: 3x1=3 3x2=6 3x3=9 3x4=12 3x5=15
multiplication_table(5)
# Should print: 5x1=5 5x2=10 5x3=15 5x4=20 5x5=25
multiplication_table(8)
# Should print: 8x1=8 8x2=16 8x3=24

for x in range(5):
    print(x)

values = [20, 45, 53, 66, 78]
sum = 0
number_of_values = 0
for value in values:
    sum += value
    number_of_values += 1
print("The sum is " + str(sum) + " and the average is " + str(sum/number_of_values))

product = 1
for n in range(1,10):
    product = product * n
print(product)

def factorial(n):
    result = 1
    for i in range(1,n+1):
        result = result * i
    return result
print(factorial(4)) # should return 24
print(factorial(5)) # should return 120

# WHY DO SOME OF THESE RETURN NOTHING?

def to_celsius(x):
    return (x - 32) * 5 / 9
for x in range(0,101,10):
    print(x, to_celsius(x))

for left in range(7):
    for right in range(left, 7):
        print("[" + str(left) + "|" + str(right) + "]", end = " ")
        # THE END PUT A SPACE BETWEEN EACH RESPONSE
        # SO IT WOULD NOT BE ON SEPARATE LINES
    print() # PUTS THE RESPONSE IN ORDER BASED OFF COLUMN NUMBER

teams = ['Dragons', 'Wolves', 'Pandas', 'Unicorns']
for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print(home_team + " vs " + away_team)

# DO NOT USE NESTED FOR LOOPS FOR SUPER LONG LISTS

for x in [25]:
    print(x)

def greet_friends(friends):
    for friend in friends:
        print("Hi " + friend)
greet_friends(['Taylor', 'Luke', 'Alissa', 'Jacob'])
# greet_friends('Barry') will print b a r r y
# separate, to fix that put it in a list

# def validate_users(users):
#     for user in users:
#         if is_valid(user):
#             print(user + " is valid")
#         else:
#             print(user + " is invalid")
# validate_users(["purplecat"])

for x in range(1,11):
    print(x**3)

for x in range(0, 100, 7):
    print(x)

# def retry(operation, attempts):
#     for n in range(attempts):
#         if operation():
#             print("Attempt " + str(n) + " succeeded")
#             break
#         else:
#             print("Attempt " + str(n) + " failed")
# retry(create_user, 3)
# retry(stop_service, 5)

def factorial(n):
    result = 1
    for x in range(1,n+1):
        result = result * x
    return result
for n in range(10):
    print(n, factorial(n))

def factorial(n):
    print("Factorial called with " + str(n))
    if n < 2:
        print("Returning 1")
        return 1
    result = n * factorial(n-1)
    print("Returning " + str(result) + " for factorial of " + str(n))
    return result
factorial(4)

def sum_positive_numbers(n):
    # The base case is n being smaller than 1
    if n < 1:
        return n
    # The recursive case is adding this number to
    # the sum of the numbers smaller than this one.
    return n + sum_positive_numbers(n-1)
print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15

# STRUCTURE FOR RECURSIVE FUNCTION
# def recursive_function(parameters):
#     if base_case_condition(parameters):
#         return base_case_value
#     recursive_function(modified_parameters)

def is_power_of(number, base):
    # Base case: when number is smaller than base.
    if number < base:
        # If number is equal to 1, it's a power (base**0).
        return number == 1

    # Recursive case: keep dividing number by base.
    return is_power_of(number/base, base)
print(is_power_of(8,2)) # Should be True
print(is_power_of(64,4)) # Should be True
print(is_power_of(70,10)) # Should be False

number = 1
while number <= 7:
    print(number, end=" ")
    number = number + 1

def show_letters(word):
    for x in word:
        print(x)
show_letters("Hello")
# Should print one line per letter

def digits(n):
    count = 0
    if n == 0:
        return 1
    while (int(n / 10) != 0):
        count += 1
        n = int(n / 10)
    return count + 1
print(digits(25))   # Should print 2
print(digits(144))  # Should print 3
print(digits(1000)) # Should print 4
print(digits(0))    # Should print 1

def multiplication_table(start, stop):
    for x in range(start, stop + 1):
        for y in range(start, stop + 1):
            print(str(x*y), end=" ")
        print()
multiplication_table(1, 3)
# Should print the multiplication table shown above

def counter(start, stop):
    x = start
    if start > stop:
        return_string = "Counting down: "
        while x >= stop:
            return_string += str(x)
            if x != stop:
                return_string += ","
            x = x - 1
    else:
        return_string = "Counting up: "
        while x <= stop:
            return_string += str(x)
            if x != stop:
                return_string += ","
            x = x + 1
    return return_string
print(counter(1, 10)) # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
print(counter(2, 1)) # Should be "Counting down: 2,1"
print(counter(5, 5)) # Should be "Counting up: 5"

def even_numbers(maximum):
    return_string = ""
    for x in range(2, maximum + 1, 2):
        return_string += str(x) + " "
    return return_string.strip()

print(even_numbers(6))  # Should be 2 4 6
print(even_numbers(10)) # Should be 2 4 6 8 10
print(even_numbers(1))  # No numbers displayed
print(even_numbers(3))  # Should be 2
print(even_numbers(0))  # No numbers displayed

