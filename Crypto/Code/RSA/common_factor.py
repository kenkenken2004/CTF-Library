from basic import recover
from math_lib import gcd


def getkey(e, n1, n2):
    p = gcd(n1, n2)
    if p == 1:
        print("There is not any common factor.")
        return -1
    else:
        return recover(e, n1, 'p', p)
