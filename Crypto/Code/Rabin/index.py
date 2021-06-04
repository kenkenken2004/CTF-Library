import basic


def key_gen(bits):
    return basic.key_gen(bits)


def encrypt(plain, n, b):
    return basic.encrypt(plain, n, b)


def decrypt(cipher, p, q, b):
    return basic.decrypt(cipher, p, q, b)


p, q, n, b = key_gen(1024)
m = 21835734525324315264623626432
c = encrypt(m, n, b)

d1, d2, d3, d4 = decrypt(c, p, q, b)
print(p, q, n, b)
print(d1)
print(d2)
print(d3)
print(d4)
