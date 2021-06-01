import basic


# Generate the key pair with given bit-length and recurrence formula function which will generate a superincreasing
# list.
# Function's example: lambda a: a*2
def key_gen(bits, function):
    return basic.key_gen(bits, function)


# Encrypt the plaintext with given public key list.
def encrypt(plain, b_list):
    return basic.encrypt(plain, b_list)


# Decrypt the ciphertext with given private key number and list.
def decrypt(cipher, w_list, q, r):
    return basic.decrypt(cipher, w_list, q, r)


def example():
    m = 26589269837643675647765454352365343536425263536563265326265425
    function = lambda n: 2345636542365343 * n
    w_list, q, r, b_list = key_gen(len(bin(m)) - 2, function)
    c = encrypt(m, b_list)
    m_2 = decrypt(c, w_list, q, r)
    print(c)
    print(m_2)
    print(m == m_2)

