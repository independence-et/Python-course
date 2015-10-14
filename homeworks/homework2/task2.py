__author__ = 'Independence'


def prime(x):
    result = True
    if x <= 1:
        result = False
    elif x == 2:
        result = True
    else:
        for i in range(x // 2):
            if x % (i + 2) == 0:
                result = False
                break
    return(result)
n = int(input())
lst1 = []
for i in range(n):
    x = int(input())
    lst1.append(prime(x))
for i in range(n):
    print(lst1[i])
