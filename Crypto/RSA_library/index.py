import basic
import common_factor
import fermat
import low_public_exponent_attack
import low_factor

# basic.py
# Generate a key pair
def gen_key(bits):
    basic.gen_key(bits)


# Encrypt with given public key
def encrypt(m, e, n):
    basic.encrypt(m, e, n)


# Decrypt with given private key
def decrypt(c, d, n):
    basic.decrypt(c, d, n)


# Generate private exponent "d" from given public key and other param
# You can input "p"=one of N's factors, and "l"=(p-1)*(q-1) or it as "numtype"
def recover(e, n, numtype, num):
    basic.recover(e, n, numtype, num)


# Generate the private exponent from two public modules with the same factor.
def common_factor(e, n1, n2):
    return common_factor.getkey(e, n1, n2)


# Generate the private exponent from the public module with factors that they have especially close value.
def fermat_method(e, n):
    return basic.recover(e, n, 'p', fermat.fermat_factor(n))


# Decrypt the cipher text from the public exponent whose value is especially small.
# This can not figure out what the private exponent is.
def low_E_attack(c, e, n):
    return low_public_exponent_attack.decrypt(e, n, c)


# Get the private exponent from the public module which has a especially small factor.
def low_factor_attack(e,n):
    return low_factor.getkey(e,n)


