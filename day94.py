import re

n = int(input())

for _ in range(n):
    strings = input()
    try:
        print(bool(re.compile(strings)))
    except re.error:
        print('False')
