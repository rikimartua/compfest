import math


def recursion(n):
    if n == 1:
        return 1
    else:
        return 1 + recursion(math.ceil(n / 2)) + recursion(math.floor(n / 2))


entry = input()
print(recursion(int(entry)))
