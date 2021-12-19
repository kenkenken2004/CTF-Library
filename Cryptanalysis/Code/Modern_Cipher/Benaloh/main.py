from sympy import randprime, factorint
from math import gcd
from random import randrange
from ...MathLib.basic import *


def key_gen(r, primebits):
    assert r % 2 == 1
    p = randprime(2 ** (primebits - 1), 2 ** primebits)
    while (p - 1) % r != 0 or gcd(r, (p - 1) // r) != 1:
        p = randprime(2 ** (primebits - 1), 2 ** primebits)
    q = randprime(2 ** (primebits - 1), 2 ** primebits)
    while gcd(r, q - 1) != 1:
        q = randprime(2 ** (primebits - 1), 2 ** primebits)
    n = p * q
    phi = (p - 1) * (q - 1)
    p = list(factorint(r).keys())
    tf = True
    y = 0
    while tf:
        tf = False
        y = randrange(2, n)
        for _ in p:
            tf = tf or pow(y, phi // _, n) == 1
    x = pow(y, phi // r, n)
    return y, n, phi, x


def encrypt(m, y, n, r):
    assert m < r
    u = randrange(0, n)
    return (pow(y, m, n) * pow(u, r)) % n


def decrypt(c, n, phi, x, r):
    assert c < n and gcd(c, n) == 1
    a = pow(c, phi // r, n)
    m = baby_giant(x, a, n) % r
    assert m != -1
    return m
