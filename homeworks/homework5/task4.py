__author__ = 'Independence'


import re
import sys

data = sys.stdin.read().split("\n")
for i in range(len(data)):
    x = re.match(" *(\w+[.\w*]*[, \w+[.\w*]*]*) = ", data[i])
    if x is not None:
        x = x.groups()[0].split(", ")
        st = str(i + 1)
        for word in x:
            st = st + " " + word
        print(st)