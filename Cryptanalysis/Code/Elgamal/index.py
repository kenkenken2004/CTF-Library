import basic


def key_gen(bits):
    return basic.key_gen(bits)


def encrypt(plain, p, g, h):
    return basic.encrypt(plain, p, g, h)


def decrypt(cipher1, cipher2, p, x):
    return basic.decrypt(cipher1, cipher2, p, x)



