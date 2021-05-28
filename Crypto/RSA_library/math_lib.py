def root(b, r):
    x = 1
    v = 0
    do = True
    while do:
        if (v + x) ** r == b:
            return v + x
        elif (v + x) ** r < b:
            v += x
            x *= 2
        else:
            x = x // 2
        if x == 0:
            do = False
    return -1

