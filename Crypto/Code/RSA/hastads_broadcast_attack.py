from Crypto.Code.math_lib import *


def exec(e, c_list, n_list):
    if max(len(c_list), len(n_list)) < e:
        print("information is not enough and can't solve.")
        return -1
    x, n = crt(c_list, n_list)
    return root(x, e)


