from ..MathLib.basic import *


def common_modulus_attack(c_list, e_list, n):
    cur_e = e_list[0]
    cur_c = c_list[0]
    for a in range(1, len(e_list)):
        g = gcd(cur_e, e_list[a])
        k1, k2 = extgcd(cur_e, e_list[a])
        cur_c = pow(cur_c, k1, n) * pow(c_list[a], k2, n) % n
        cur_e = g

    return root(cur_c, cur_e)
