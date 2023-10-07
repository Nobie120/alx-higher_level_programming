#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return None
    divs = []
    for i in my_list:
        if (i % 2) == 0:
            divs.append(True)
        else:
            divs.append(False)
    return divs
