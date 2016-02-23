import sys
__author__ = 'Independence'


inp = sys.stdin.read()
inp = inp.split('\n')

n = int(inp[0])
m = int(inp[2])
ex = inp[m+3]
output = str()
rules = dict()
stack = inp[1].split(" ")
for i in range(3, m+3):
    x = inp[i].split(" ")
    if x[0] not in rules:
        rules[x[0]] = {x[1]: x[2]}
    else:
        rules[x[0]][x[1]] = x[2]
while n > 0:
    x = rules[stack[n-1]]
    if ex not in x:
        stack.pop(n-1)
        n -= 1
    elif x[ex] != "_":
        ex = x[ex]
        stack.pop(n-1)
        n -= 1
    else:
        break
for elem in stack:
    output = output + str(elem) + " "
print(output)