__author__ = 'Independence'
lst = []
c = 0
str0 = input()
str1 = ''
for i in range(len(str0)):
    if str0[i] == ' ':
        lst.append(c)
        c = 0
        i = i + 1
    else:
        c = c * 10
        c = c + int(str0[i])
        i = i + 1
lst.append(c)
lst1 = lst[::2]
lst2 = lst[1:len(lst):2]
lst1.sort()
lst2.sort(reverse=True)
for i in range(len(lst1)):
    str1 = str1 + str(lst1[i]) + ' ' + str(lst2[i]) + ' '
    i = i + 1
print(str1)
