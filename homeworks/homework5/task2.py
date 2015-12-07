__author__ = 'Independence'


import re
import sys

data = sys.stdin.read()
results = []
for symbol in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9):
    results += re.findall(("\d*" + str(symbol) + "{3,11}" + "\d*"), data)
for result in results:
    print(result)