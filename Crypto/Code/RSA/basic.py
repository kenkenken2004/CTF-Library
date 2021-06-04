from sympy import randprime
from Crypto.Code.math_lib import gcd

def gen_key(bits):
    while True:
        p = randprime((1 << (bits - 1)) + 1, 1 << bits)
        q = randprime((1 << (bits - 1)) + 1, 1 << bits)
        if p != q and gcd(p - 1, q - 1) == 2:
            n = p * q
            e = 65537
            d = pow(e, -1, (p - 1) * (q - 1) // 2)
            return n, e, d


def encrypt(m, e, n):
    return pow(m, e, n)


def decrypt(c, d, n):
    return pow(c, d, n)


def recover(e, n, numtype, num):
    if numtype == "p":
        p = num
        q = n // num
        return pow(e, -1, (p - 1) * (q - 1))
    elif numtype == "l":
        return pow(e, -1, num)
    else:
        print("No such numtype.")
        return
