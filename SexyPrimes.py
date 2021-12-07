# Given a range of the form [L, R].The task is to print all the sexy prime pairs in the range.
# Examples:
# Input : L =6, R = 59
# Output : (7, 13) (11, 17) (13, 19)
# (17, 23) (23, 29) (31, 37) (37, 43)
# (41, 47) (47, 53) (53, 59)

# Input : L = 1, R = 19
# Output : (5, 11) (7, 13) (11, 17) (13, 19)


def primelist(n):
    primes = [True] * (n+1)
    primes[0], primes[1] = False, False
    for i in range(2, int(n**0.5)+1):
        if primes[i]:
            for j in range(i*i, n+1, i):
                primes[j] = False
    return primes


L = 6
R = 59
primes = primelist(R)

for i in range(L, len(primes)):
    if i+L < len(primes) and primes[i] and primes[i+L]:
        print([i, i+L])
