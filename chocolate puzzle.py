
# Chocolate puzzle
# A teacher decided to motivate all her students for their grades by
# giving them chocolates.
# On the first day she gave a certain number of chocolates and on the
# next day she gave twice the no of chocolates she gave on previous
# day and she doubled the no of chocolates every day.
# find how many chcolates she bought ? given last day, say N

# sample input (last day)
# 5
# sample output
# 62
# explanation
# on first day = 2
# on second day = 2*2 = 4
# on third day = 4*2 = 8
# on fourth day = 8*2 = 16
# on last day = 16*2 = 32
# sum of all the chocolates = 62 (2+4+8+16+32)


# time complexity: O(1)
# space complexity: O(1)
# Geometric progression formula
from math import pow
# n = int(input())
n = 5
r = 2
a = 2
print(2**(n+1)-2)   # 2**(n-1) + 2**(n-2) + 2**(n-3) + 2**(n-4) + 2**(n-5)

print(int(a*((r**n)-1)/(r-1)))   # 2*(1-2**n)
print(int(a*(pow(r, n)-1)//(r-1)))   # 2*(1-2**n)
print((1+((n/2)**((n/2)+1)))*2)
