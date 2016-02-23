__author__ = 'Independence'


def sum(a, b):
    if type(a) is not int or type(b) is not int:
        raise TypeError("not int")
    elif a <= 0 or b <= 0:
        raise ValueError("not positive")
    return int(a) + int(b)
