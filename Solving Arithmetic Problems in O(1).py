# # Sum of a natural number
# # n = int(input())
# n = 10
# # Sum of a natural number formula is n*(n+1)/2

# print(n*(n+1)//2)

# find sum of multiples of 3 and 5 below 1000
# sum = 0

# time complaxity: O(n)
# for i in range(1000):
#     if i % 3 == 0 or i % 5 == 0:
#         sum += i
# print(sum)


# # time_complexity: O(1)
# N = 1000

# n1 = (N-1)//3
# n2 = (N-1)//5
# n3 = (N-1)//15

# s1 = 3*(n1*(n1+1))//2
# s2 = 5*(n2*(n2+1))//2
# s3 = 15*(n3*(n3+1))//2

# sum = s1 + s2 - s3
# print(sum)

# sum of two natural numbers in list
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 13

# time complexity: O(n^2)
# for i in range(len(l)):
#     for j in range(i+1, len(l)):
#         if l[i] + l[j] == target:
#             print(l[i], l[j])
#             break   # break the inner loop

# # time complexity: O(n)
# for i in range(len(l)):
#     a = target - l[i]
#     if a in l[i+1:]:
#         print(l[i], a)
#         break

# time complexity: O(n)
for i in range(len(l)):
    if l[i] + l[i+1] == target:
        print(l[i], l[i+1])
        break
