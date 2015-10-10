__author__ = 'Independence'


def euclid(n, m):
    if n % m == 0:
        return m
    return euclid(m, n % m)


def rpfilter(a, *args):
    result = str()
    a = int(a)
    for arg in args:
        arg = int(arg)
        if euclid(a, arg) == 1:
            result = result + " " + str(arg)
    return result[1:]

inp = str(input())
inp = inp.split(' ')
if len(rpfilter(inp[0], *inp[1:])) == 0:
    print(None)
else:
    print(rpfilter(inp[0], *inp[1:]))
