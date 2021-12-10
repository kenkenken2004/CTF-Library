from .basic import recover
from ..MathLib.basic import gcd


def getkey(e, n1, n2):
    p = gcd(n1, n2)
    if p == 1:
        print("These are co-prime, therefore it is hard to solve it.")
        return -1
    else:
        return recover(e, n1, 'p', p)

