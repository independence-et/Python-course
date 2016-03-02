import sys
__author__ = 'Independence'

inp = sys.stdin.read()
inp = inp.split('\n')
n = int(inp[0])
m = int(inp[n + 1])
errors = list()
parents = dict()
redundant_errors = list()


def simple_t4ts(error, errors_list, errors_tree):
    if error in errors_list:
        return True
    else:
        for element in errors_tree[error]:
            if simple_t4ts(element, errors_list, errors_tree) == True:
                return True

for i in range(1, n + 1):
    branch = inp[i].split(" ")
    for x in branch:
        if x == branch[0]:
            parents[branch[0]] = list()
        elif x == ":":
            continue
        else:
            parents[branch[0]].append(x)
for i in range(n + 2, m + n + 2):
    errors.append(inp[i])
for i in range(m):
    if simple_t4ts(errors[m - i - 1], errors[0:m - i - 1], parents) == True \
            and errors[m - i - 1] not in redundant_errors:
        redundant_errors.append(errors[m - i - 1])
list.reverse(redundant_errors)
for r_errors in redundant_errors:
    print(r_errors)
