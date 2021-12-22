from random import *
from math import gcd


def key_gen(n=100, d=2):
    w = []
    a = randrange(2 ** (d * n - n - 1), 2 ** (d * n - n))
    sum_w = a
    for i in range(1, n):
        a = randrange(max(2 ** (d * n - n + i - 1), sum_w + 1), 2 ** (d * n - n + i))
        w.append(a)
        if sum_w >= a:
            print("Error: Invalid superincreasing function.")
            return -1
        sum_w += a
    q = randrange(max(2 ** (d * n - 1), sum_w), 2 ** (d * n))
    r = q
    while gcd(q, r) != 1:
        r = randrange(2, q)
    b = [((r * x) % q) for x in w]
    return w, q, r, b


def encrypt(m, b):
    m = bin(m)[2:]
    m = "0" * (len(b) - len(m)) + m
    c = 0
    for a, b in zip(m, b):
        c += (ord(a) - ord("0")) * b
    return c


def decrypt(c, w, q, r):
    c = (c * pow(r, -1, q)) % q
    m = ""
    t = w.copy()
    t.reverse()
    for a in t:
        if a <= c:
            m = "1" + m
            c -= a
        else:
            m = "0" + m
    m = int(m, 2)
    return m
