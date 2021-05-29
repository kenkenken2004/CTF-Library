from math import *


def fermat_factor(n):
    x = floor(sqrt(n)) + 1
    y = floor(sqrt(x * x - n))
    while True:
        w = x * x - n - y * y
        if w == 0:
            return x + y
        elif w > 0:
            y += 1
        else:
            x += 1
