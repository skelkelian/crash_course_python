divisors=[1, 2, 3, 5]

def sum_divisors(n):
    sum = 0
    if n == 0:
        return sum
    for divisor in divisors:
        print("this is the divisor, ", divisor)
        if n % divisor == 0:
            sum += divisor
    return sum

print("the sum of the first one is, ", sum_divisors(0))
# 0
assert(sum_divisors(0)==0)
print(sum_divisors(3)) # Should sum of 1
# 1
assert(sum_divisors(3)==1)