import sys
__author__ = 'Independence'


def simple_t2ts(x, upper_class, xdict, treedict):
    if upper_class in xdict[x]:
        return upper_class
    else:
        for element in treedict[upper_class]:
            return simple_t2ts(x, element, xdict, treedict)

inp = sys.stdin.read()
inp = inp.split('\n')
n = int(inp[0])
m = int(inp[n + 1])
methods = dict()
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
for x in range(n + 2, n + m + 2):
    meth = inp[x].split(" ")
    if meth[1] not in methods:
        methods[meth[1]] = list()
    methods[meth[1]].append(meth[0])
question = inp[n + m + 2].split(" ")
if question[1] not in methods:
    print(None)
else:
    print(simple_t2ts(question[1], question[0], methods, parents))
