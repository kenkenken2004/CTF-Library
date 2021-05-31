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

