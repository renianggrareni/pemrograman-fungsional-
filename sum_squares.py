from functools import reduce
numbers = [1, 2, 3]

def squared(n):
   return n**2

def get_sum(acc, n):
   return acc + n

squared = list(map(squared, numbers))
sum = reduce(get_sum, squared)

print(sum)
