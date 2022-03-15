import math


def is_prime(n):
    j = math.sqrt(n)
    j = math.ceil(j)
    j = int(j)
    l = []
    if n <= 1:
        return False
    if n ==2:
        return True
    for x in range(2, j+1):
        l.append(x)
    print(l)
    for x in range(0,len(l)):
        if n % l[x] == 0:
            return False
    return True



print(is_prime(2))