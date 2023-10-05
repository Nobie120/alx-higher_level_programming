#!/usr/bin/python3
def magic_calculation(a, b):
    import magic_calculation_102 as fn
    if a < b:
        c = fn.add(a, b)
        for i in range(4, 6):
            c = fn.add(c, i)
        return c
    else:
        return fn.sub(a, b)
    return 0
