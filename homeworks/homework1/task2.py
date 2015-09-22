__author__ = 'independence'
a=str(input())
c=str
if a == 'утюг':
    b = int(input())
    if 11 <= b%100 <= 14:
        c = 'утюгов'
    elif b%10 == 1:
        c = a
    elif 2 <= b%10 <=4:
        c = 'утюга'
    else:
        c = 'утюгов'
    print(b,c)
elif a == 'ложка':
    b = int(input())
    if 11 <= b%100 <= 14:
        c = 'ложек'
    elif b%10 == 1:
        c = a
    elif 2 <= b%10 <=4:
        c = 'ложки'
    else:
        c = 'ложек'
    print(b,c)
else: print('€ так не играю')
