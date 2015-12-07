__author__ = 'Independence'


import re
import sys

data = sys.stdin.read().split("\n")
for i in range(len(data)):
    x = re.findall("(\w*) = ", data[i])
    if len(x) > 0:
        print(str(i + 1) + " " + x[0])