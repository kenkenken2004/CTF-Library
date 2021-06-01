from math_lib import *


def decrypt(e, n, c):
    a = c
    while True:
        ret = root(c, e)
        if ret != -1:
            return ret
        a += n
