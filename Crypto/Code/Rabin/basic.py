from sympy import randprime
from random import randrange as rand


def key_gen(bits):
    p = 0
    q = 0
    while p % 4 != 3 or q % 4 != 3:
        p = randprime((1 << (bits - 1)) + 1, 1 << bits)
        q = randprime((1 << (bits - 1)) + 1, 1 << bits)
    n = p * q
    b = rand(0,n)
    return p, q, n, b


def encrypt(plain, n, b):
    return (plain * (plain + b)) % n


def decrypt(cipher, p, q, n, b):
    return