import basic


def key_gen(bits):
    return basic.key_gen(bits)


def encrypt(plain, p, g, h):
    return basic.encrypt(plain, p, g, h)


def decrypt(cipher1, cipher2, p, x):
    return basic.decrypt(cipher1, cipher2, p, x)


m = 39128581952325263237237231
p, g, h, x = key_gen(1024)
c1, c2 = encrypt(m, p, g, h)
print(decrypt(c1, c2, p, x))
