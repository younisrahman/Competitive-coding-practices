# # Sum of a natural number
# # n = int(input())
# n = 10
# # Sum of a natural number formula is n*(n+1)/2

# print(n*(n+1)//2)

# find sum of multiples of 3 and 5 below 1000
sum = 0

# time complaxity: O(n)
# for i in range(1000):
#     if i % 3 == 0 or i % 5 == 0:
#         sum += i
# print(sum)


# time_complexity: O(1)
N = 1000

n1 = (N-1)//3
n2 = (N-1)//5
n3 = (N-1)//15

s1 = 3*(n1*(n1+1))//2
s2 = 5*(n2*(n2+1))//2
s3 = 15*(n3*(n3+1))//2

sum = s1 + s2 - s3
print(sum)
