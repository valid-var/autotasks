from itertools import product

k = 0
items = []

for item in product("0123456789ABCDE", repeat=5):
    item2 = [int(x, base=15) for x in item]

    if item[0] == "0":
        continue

    if (item2[0] % 2 == 0 and item2[1] % 3 == 0 and item2[2] % 2 == 0 and item2[3] % 3 == 0 and item2[4] % 2 == 0
        or item2[0] % 3 == 0 and item2[1] % 2 == 0 and item2[2] % 3 == 0 and item2[3] % 2 == 0 and item2[4] % 3 == 0):
        k += 1

print(k)