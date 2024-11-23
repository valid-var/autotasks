

results = []

for number in range(800_000, 10_000_000):
    min_div = None
    max_div = None
    for i in range(2, number // 2):
        if number % i == 0:
            min_div = i
            break
    if min_div is None or min_div == number // 2:
        max_div = None
        continue
    for i in range(number // 2, 1, -1):
        if number % i == 0:
            max_div = i
            break
    M = max_div + min_div
    if M % 10 == 4:
        results.append([number, M])
        if len(results) == 5:
            break
print(results)