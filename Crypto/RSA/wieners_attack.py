from math_lib import root


# convert the continued fraction to a rational number
def rational(cont_frac):
    array = cont_frac.copy()
    array.reverse()
    numer = 1
    denom = 0
    for a in array:
        numer, denom = denom, numer
        numer += denom * a
    return numer, denom


# rebuild the continued fraction
def cont_frac(numer, denom):
    cf = []
    while denom:
        q = numer // denom
        cf.append(q)
        numer, denom = denom, numer - denom * q
    return cf


# output convergents of the continued fraction in every depth
def convergents(cont_frac):
    ret = []
    n0, n1 = cont_frac[0], cont_frac[0] * cont_frac[1] + 1
    d0, d1 = 1, cont_frac[1]
    ret.append((n0, d0))
    ret.append((n1, d1))

    for i in range(2, len(cont_frac)):
        n2, d2 = cont_frac[i] * n1 + n0, cont_frac[i] * d1 + d0
        ret.append((n2, d2))
        n0, n1 = n1, n2
        d0, d1 = d1, d2
    return ret


def wieners_attack(e, n):
    cf = cont_frac(e, n)
    conv = convergents(cf)
    for k, d in conv:
        if not k:
            continue
        phi, rem = divmod(e * d - 1, k)
        if rem:
            continue
        s = n - phi + 1
        D = s * s - 4 * n
        if D > 0 and root(D, 2) != -1:
            return d
    return -1
