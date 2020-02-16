from functools import reduce

nums = [2, 5, 3, 6, 4, 9, 8, 7, 1]

sum = reduce(lambda a, b: a + b, nums)
print(sum)

# Reduce: It will take two values at a time from the list and provides the result as per the condition
