from random import randint
from math import gcd


def key_gen(bits, function):
    w_list = []
    w = 65537
    sum_w = 0
    for a in range(bits):
        w = function(w)
        w_list.append(w)
        if sum_w >= w:
            print("Error: Invalid superincreasing function.")
            return -1
        sum_w += w
    q = randint(sum_w + 1, (sum_w + 1) ** 2)
    r = q
    while gcd(q, r) != 1:
        r = randint(1, q - 1)

    b_list = [((r * x) % q) for x in w_list]
    return w_list, q, r, b_list


def encrypt(plain, b_list):
    m = bin(plain)[2:]
    if not (len(m) == len(b_list)):
        print("Error: Invalid Key.")
        return -1
    c = 0
    for a, b in zip(m, b_list):
        c += a * b
    return c


def decrypt(cipher, w_list, q, r):
    c = cipher * pow(r, -1, q) % q
    m = ""
    t = w_list.copy().reverse()
    for a in t:
        if a <= c:
            m = "1" + m
            c -= a
        else:
            m = "0" + m
    m = int(m, 2)
    return m
