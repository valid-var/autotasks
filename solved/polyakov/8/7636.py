from itertools import product

ps = product("0123456789AB", repeat=5)
result = []
for p in ps:
    if (p[0] == "0"):
        continue
    if list(p).count("7") != 1:
        continue
    more_that_eight = 0
    for s in p:
        if s > '8': more_that_eight += 1
    if more_that_eight > 3:
        continue
    result.append(p)

print(len(result))