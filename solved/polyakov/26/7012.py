file = open("7012.txt").read()
fileline = file.split('\n')
N, M = map(int, fileline[0].split())
A = fileline[1:-1] if fileline[-1] == "" else fileline[1:]

D_CHEAP = {}
D_EXP = {}
for line in A:
    price, status = map(int, line.split())

    if price > M:
        D = D_EXP
    else:
        D = D_CHEAP

    if price not in D:
        D[price] = {}
    if status == 1:
        D[price]["sold"] = D[price].get("sold", 0) + 1
    elif status == 0:
        D[price]["left"] = D[price].get("left", 0) + 1

exp_sorted = sorted(D_EXP.items(), key=lambda item: -item[1]["sold"])

cheap_sorted = sorted(D_CHEAP.items(), key=lambda item: -item[1]["sold"])

print(
    exp_sorted[0][0] * exp_sorted[0][1]["sold"] + cheap_sorted[0][0] * cheap_sorted[0][1]["sold"],
    exp_sorted[0][1]["left"] + cheap_sorted[0][1]["left"]
)

exp_price, exp_data = exp_sorted[0]
exp_revenue = exp_price * exp_data["sold"]
exp_left = exp_data["left"]

cheap_price, cheap_data = cheap_sorted[0]
cheap_revenue = cheap_price * cheap_data["sold"]
cheap_left = cheap_data["left"]

print(
    exp_revenue + cheap_revenue, exp_left + cheap_left
)

MAX_SOLD = 0
MAX_PRICE = None
for price, data in D_EXP.items():
    if data['sold'] > MAX_SOLD:
        MAX_SOLD = data['sold']
        MAX_PRICE = price

MAX_SOLD_CHEAP = 0
MAX_PRICE_CHEAP = None
for price, data in D_CHEAP.items():
    if data['sold'] > MAX_SOLD_CHEAP:
        MAX_SOLD_CHEAP = data['sold']
        MAX_PRICE_CHEAP = price

print(
    MAX_SOLD*MAX_PRICE + MAX_SOLD_CHEAP*MAX_PRICE_CHEAP,
    D_EXP[MAX_PRICE]["left"] + D_CHEAP[MAX_PRICE_CHEAP]["left"]
)
