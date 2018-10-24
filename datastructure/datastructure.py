import os
import re

list = ["a", "b", "c", "d"]

list.append(33)

print list

list.pop(0)

print list
print list.index('c')

print os.getcwd()

print dir(os)

print re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')