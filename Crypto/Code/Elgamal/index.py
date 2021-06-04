import basic


def key_gen(bits):
    return basic.key_gen(bits)


def encrypt(plain, q, g, h):
    return basic.encrypt(plain, q, g, h)


def decrypt(cipher1, cipher2, q, x):
    return basic.decrypt(cipher1, cipher2, q, x)


m = 39128581952325263237237231
q, g, h, x = key_gen(1024)
c1, c2 = encrypt(m, q, g, h)
print(decrypt(c1, c2, q, x))
