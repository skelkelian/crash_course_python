def sum_divisors(n):
    sum = 0
    if n == 0:
        return sum
    for possible_divisor in range(1, n-1):
        if n % possible_divisor == 0:
            print("this is the possible divisor, ", possible_divisor)
            sum += possible_divisor
    return sum
print(sum_divisors(0))

print(sum_divisors(3)) # Should sum of 1

print(sum_divisors(36)) # Should sum of 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102)) # Should be sum of 2+3+6+17+34+51
# 114