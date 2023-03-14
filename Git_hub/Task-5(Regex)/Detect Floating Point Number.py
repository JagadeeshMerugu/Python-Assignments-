import re
pattern = r'^[+-.]\d+\.\d+|\d+\.\d+$|[+-]\.\d+'
n = int(input())
for i in range(n):
    target = input()
    if re.fullmatch(pattern,target):
        print('True')
    else:
        print('False')
