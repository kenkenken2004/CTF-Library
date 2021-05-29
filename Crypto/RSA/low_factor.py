from basic import *


def trial_division(n):
    p = 2
    while p ** 2 <= n:
        if n % p == 0:
            return p
        p += 1
    return -1


def getkey(e, n):
    p = trial_division(n)
    if p == -1:
        print("n is a prime number.")
    else:
        return recover(e, n, 'p', p)
