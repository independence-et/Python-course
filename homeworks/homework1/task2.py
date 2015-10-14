__author__ = 'Independence'
st = str(input())
st = st + ' '
c = 0
s = 0
l = 0
n = 1
for i in range(len(st)):
    if st[i] == ' ':
        s = s + c*n
        c = 0
        i = i + 1
        l = l + 1
        n = 1
    elif st[i] == '-':
        n = -1
        i = i + 1
    else:
        c = c * 10
        c = c + int(st[i])
        i = i + 1
m = s / l
print(m)
