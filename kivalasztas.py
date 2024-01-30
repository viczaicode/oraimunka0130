import math


def kivalasztas():
    prim = False
    n = 9999
    while prim == False:
        n = n + 1
        i = 2
        while i <= math.sqrt(n) and n % i != 0:
            i = i + 1
        prim = i > math.sqrt(n)
    print(n)
