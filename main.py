import random
from Cryptanalysis.Code.Modern_Cipher.Merkle_Hellman.main import *


def test():
    m = random.randint(1434223, 53123514252)
    w, q, r, b = key_gen(100, lambda x: x * 2)
    c = encrypt(m, b)
    d = decrypt(c, w, q, r)
    print(m)
    print(c)
    print(d)


