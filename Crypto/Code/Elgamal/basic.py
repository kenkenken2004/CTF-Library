from sympy import randprime
from random import randrange as rand


def key_gen(bits):
    q = randprime((1 << (bits - 1)) + 1, 1 << bits)
    g = rand(2, q)
    x = rand(2, q)
    h = pow(g, x, q)
    return q, g, h, x


def encrypt(plain, q, g, h):
    r = rand(0, q)
    c1 = pow(g, r, q)
    c2 = plain * pow(h, r, q) % q
    return c1, c2


def decrypt(cipher1, cipher2, q, x):
    return cipher2 * pow(pow(cipher1, x, q), -1, q) % q

