import fnmatch

mask = "3?12?14*5"

div = 1917

upper_limit = 10**10

# 1.

result = fnmatch.fnmatch("3g123145", mask)
print(result)

# 2.
import re

re_mask = mask.replace("?", "\d").replace("*", "\d*") + "$"
pattern = re.compile(re_mask)
print(bool(pattern.match("31123145")))

first_div = None
for i in range(30120145, upper_limit):
    if i % div == 0:
        first_div = i
        break

for i in range(first_div, upper_limit, div):
    if pattern.match(str(i)):
        print(i, i // div)
