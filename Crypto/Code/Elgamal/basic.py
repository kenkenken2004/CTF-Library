from sympy import randprime
from random import randrange as rand


def key_gen(bits):
    p = randprime((1 << (bits - 1)) + 1, 1 << bits)
    g = rand(2, p)
    x = rand(0, p)
    h = pow(g, x, p)
    return p, g, h, x


def encrypt(plain, p, g, h):
    r = rand(0, p)
    c1 = pow(g, r, p)
    c2 = plain * pow(h, r, p) % p
    return c1, c2


def decrypt(cipher1, cipher2, p, x):
    return cipher2 * pow(pow(cipher1, x, p), -1, p) % p

