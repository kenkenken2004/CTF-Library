from sympy import randprime
from random import randrange as rand
from ..MathLib.basic import *


def key_gen(bits):
    p = 0
    q = 0
    while p % 4 != 3:
        p = randprime((1 << (bits - 1)) + 1, 1 << bits)
    while q % 4 != 3:
        q = randprime((1 << (bits - 1)) + 1, 1 << bits)
    n = p * q
    b = 1
    while b % 2 == 1:
        b = rand(0, n)
    return p, q, n, b


def encrypt(plain, n, b):
    return (plain * (plain + b)) % n


def decrypt(cipher, p, q, b):
    xp = (pow(cipher + b*b // 4, (p + 1) // 4, p) - b//2) % p
    xq = (pow(cipher + b*b // 4, (q + 1) // 4, q) - b//2) % q
    x1 = crt([xp, xq],             [p, q])[0]
    x2 = crt([- xp - b, xq],       [p, q])[0]
    x3 = crt([xp, - xq - b],       [p, q])[0]
    x4 = crt([- xp - b, - xq - b], [p, q])[0]
    return x1, x2, x3, x4
