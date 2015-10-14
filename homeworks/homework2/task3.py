__author__ = 'Independence'


def euclid(n, m):
    if n % m == 0:
        return m
    return euclid(m, n % m)

inp = str(input())
inp = inp.split(' ')
print(euclid(int(inp[0]), int(inp[1])))
