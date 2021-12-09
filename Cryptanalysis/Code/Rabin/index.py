import basic


def key_gen(bits):
    return basic.key_gen(bits)


def encrypt(plain, n, b):
    return basic.encrypt(plain, n, b)


def decrypt(cipher, p, q, b):
    return basic.decrypt(cipher, p, q, b)

