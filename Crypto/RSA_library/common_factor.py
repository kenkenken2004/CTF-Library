from basic import recover
from math import gcd


def getkey(e, n, n2):
    p = gcd(n, n2)
    if p == 1:
        print("There is not any common factor.")
    else:
        return recover(e, n, 'p', p)
