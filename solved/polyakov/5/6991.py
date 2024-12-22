
for n in range(1,100):
    r = bin(n)[2:]
    count_1 = r.count("1")
    if count_1 % 2 == 1:
        r += "10"
    else:
        r += "01"
    r_int = int(r, 2)
    if r_int > 89:
        print(r_int)
        print(n)
        break
