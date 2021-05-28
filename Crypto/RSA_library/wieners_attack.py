from math import gcd


def to_rational(cont_frac):
    array = cont_frac
    array.reverse()
    numer = 1
    denom = 0
    for a in array:
        numer ,denom = denom ,numer
        numer += denom*a
    return numer, denom

# rebuild the continued fraction
def to_cont_frac(numer,denom):
    array = []
