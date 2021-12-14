from sympy import randprime, factorint
from ...MathLib.basic import *
from math import floor, sqrt
from wieners_attack import wieners_attack


def gen_key(bits):
    while True:
        p = randprime((1 << (bits // 2 - 1)) + 1, 1 << (bits // 2))
        q = randprime((1 << (bits // 2 - 1)) + 1, 1 << (bits // 2))
        if p != q and gcd(p - 1, q - 1) == 2:
            n = p * q
            e = 65537
            d = pow(e, -1, (p - 1) * (q - 1) // 2)
            return n, e, d


def encrypt(m, e, n):
    return pow(m, e, n)


def decrypt(c, d, n):
    return pow(c, d, n)


def naive_attack(e, n):
    p = 2
    while p ** 2 <= n:
        if n % p == 0:
            return p
        p += 1

    if p > n:
        print("n is a prime number.")
    else:
        q = n // p
        return pow(e, -1, (p - 1) * (q - 1))


def common_factor_attack(e, n1, n2):
    p = gcd(n1, n2)
    if p == 1:
        print("These are co-prime, therefore it is hard to solve it.")
        return -1
    else:
        q = n1 // p
        return pow(e, -1, (p - 1) * (q - 1))


def common_modulus_attack(c_list, e_list, n):
    cur_e = e_list[0]
    cur_c = c_list[0]
    for a in range(1, len(e_list)):
        g = gcd(cur_e, e_list[a])
        k1, k2 = extgcd(cur_e, e_list[a])
        cur_c = pow(cur_c, k1, n) * pow(c_list[a], k2, n) % n
        cur_e = g

    return root(cur_c, cur_e)


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


def hastads_broadcast_attack(e, c_list, n_list):
    if max(len(c_list), len(n_list)) < e:
        print("information is not enough and can't solve.")
        return -1
    x, n = crt(c_list, n_list)
    return root(x, e)


def low_public_exponent_attack(e, n, c):
    a = c
    while True:
        ret = root(c, e)
        if ret != -1:
            return ret
        a += n


def multi_factor_attack(e, n):
    factor = list(factorint(n).keys())
    l = 1
    for a in factor:
        l *= a - 1
    return pow(e, -1, n)


