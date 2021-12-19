from math import sqrt, ceil


# Get the greatest common divisor of m,n
def gcd(m, n):
    while n:
        m, n = n, m % n
    return m


# Get the least common multiple of m,n
def lcm(m, n):
    return m * n // gcd(m, n)


# Get the x,y,g which will be a*x+b*y=gcd(a,b)
def extgcd(a, b):
    x, y, u, v = 1, 0, 0, 1
    while b:
        k = a // b
        x -= k * u
        y -= k * v
        x, u = u, x
        y, v = v, y
        a, b = b, a % b
    return x, y


def root(b, r):
    x = 1
    v = 0
    do = True
    while do:
        if (v + x) ** r == b:
            return v + x
        elif (v + x) ** r < b:
            v += x
            x *= 2
        else:
            x = x // 2
        if x == 0:
            do = False
    return -1


def crt(r, n):
    n_mul = 1
    for m in n:
        n_mul *= m
    result = 0
    for (a, n) in zip(r, n):
        m = n_mul // n
        r, s = extgcd(n, m)
        d = gcd(n, m)
        if d != 1:
            print("Input not pairwise co-prime")
        result += a * s * m

    return result % n_mul, n_mul


def baby_giant(X, Y, M):
    D = {1: 0}
    sq = int(M ** .5) + 1
    # Baby-step
    Z = 1
    for i in range(sq):
        Z = Z * X % M
        D[Z] = i + 1
    if Y in D:
        return D[Y]
    # Giant-step
    R = pow(Z, M - 2, M)  # R = X^(-sq)
    for i in range(1, sq + 1):
        Y = Y * R % M
        if Y in D:
            return D[Y] + i * sq
    return -1
