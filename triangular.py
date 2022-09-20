def triangular(n):
   if n == 1:
     return 1
   result = [i for i in range(n, 0, -1)]
   return sum(result)

print("",triangular(5))
