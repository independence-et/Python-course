__author__ = 'independence'
a=str(input())
c=str
if a == '����':
    b = int(input())
    if 11 <= b%100 <= 14:
        c = '������'
    elif b%10 == 1:
        c = a
    elif 2 <= b%10 <=4:
        c = '�����'
    else:
        c = '������'
    print(b,c)
elif a == '�����':
    b = int(input())
    if 11 <= b%100 <= 14:
        c = '�����'
    elif b%10 == 1:
        c = a
    elif 2 <= b%10 <=4:
        c = '�����'
    else:
        c = '�����'
    print(b,c)
else: print('� ��� �� �����')
