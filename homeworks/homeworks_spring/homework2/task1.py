import sys
__author__ = 'Independence'


inp = sys.stdin.read()
inp = inp.split('\n')
n = int(inp[0])
parents = dict()
for i in range(1, n + 1):
    branch = inp[i].split(" ")
    for x in branch:
        if x == branch[0]:
            parents[branch[0]] = list()
        elif x == ":":
            continue
        else:
            parents[branch[0]].append(x)
for elem in parents:
    for parent in parents[elem]:
        for x in parents[parent]:
            if x not in parents[elem]:
                parents[elem].append(x)
q = int(inp[n + 1])
for x in range(n + 2, n + q + 2):
    question = inp[x].split(" ")
    if question[0] == question[1]:
        print("Yes")
    elif question[0] in parents[question[1]]:
        print("Yes")
    else:
        print("No")
