numbers = [4,5,8,9,1]
numbers.sort()
# by default sorts least to greatest
print(numbers)
# changes the original list

names = ["Carlos", "Alex", "artem", "Daniel", "Kelly"]
print(sorted(names))
# by default sorts in alphabetical order with uppercase going first
print(names)
# sorted function returns a new sorted list and doesn't change the original
print(sorted(names, key = len))
# sorts function based off length of each name


# sorted returns a new list, while sort returns the same list reorganized.