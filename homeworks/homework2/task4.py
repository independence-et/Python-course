__author__ = 'Independence'


def euclid(n, m):
    if n % m == 0:
        return m
    return euclid(m, n % m)


def rpfilter(a, *args):
    result = list()
    for arg in args:
        if euclid(a, arg) == 1:
            result.append(arg)
    return result

inp = input().split(' ')
inp = [int(i) for i in inp]
if len(rpfilter(*inp)) == 0:
    print(None)
else:
    print(*rpfilter(*inp))
