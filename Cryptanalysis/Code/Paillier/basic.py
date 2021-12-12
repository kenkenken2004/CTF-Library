from sympy import randprime
from random import randrange as rand
from ..MathLib.basic import *


def key_gen(bits):
    p = randprime((1 << (bits // 2 - 1)) + 1, 1 << (bits // 2))
    q = randprime((1 << (bits // 2 - 1)) + 1, 1 << (bits // 2))
    n = p * q
    k = rand(0, n)
    g = (1 + k * n) % (n * n)
    # pubkey:n,g  privatekey:p,q
    return p, q, n, g


def encrypt(m, n, g):
    mod = n * n
    r = rand(0, mod)
    c = pow(g, m, mod) * pow(r, n, mod) % mod
    return c


def decrypt(c, p, q, n, g):
    l = lcm(p - 1, q - 1)
    return 0
