__author__ = 'independence'
str0 = 'abcdefghijklmnopqrstuvwxyz'
dict1 = {}
for i in range(26):
    dict1[i+1] = str0[i]
str00 = input()
str1 = str00 + ' '
m = 0
for i in range(26):
    for n in range(len(str1)):
        if str1[n] == dict1[i + 1]:
            m = m + 1
        n = n + 1
    if m > 0:
        print(dict1[i + 1], m)
    m = 0
