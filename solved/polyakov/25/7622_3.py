import fnmatch

mask = "3?12?14*5"

div = 1917

upper_limit = 10**10

first_div = None
for i in range(30120145, upper_limit):
    if i % div == 0:
        first_div = i
        break

for i in range(first_div, upper_limit, div):
    if fnmatch.fnmatch(str(i), mask):
        print(i, i // div)
