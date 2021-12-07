def isSquare(n):
    # if (n == 0):
    #     return True
    # if (n < 0):
    #     return False
    sr = (n**0.5)
    return ((sr - int(sr)) == 0)


n = int(input())
for i in range(n):
    isSquareNumber = isSquare(int(input()))
    print("NO" if isSquareNumber else "YES")
