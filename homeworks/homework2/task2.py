__author__ = 'Independence'


def combinations(n, k):
    if n < 0 or k < 0:
        print('Error in combinations, you will die')
    elif k > n:
        return 0
    elif k == n or k == 0:
        return 1
    else:
        return combinations(n-1, k-1) + combinations(n-1, k)
inp = str(input())
inp = inp.split(' ')
print(combinations(int(inp[0]), int(inp[1])))
