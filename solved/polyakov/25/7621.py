

results = []

for number in range(800_000, 10_000_000):
    min_div = None
    max_div = None

    for i in range(2, int(number ** 0.5)+1):
        if number % i == 0:
            min_div = i
            break

    if min_div is None:
        max_div = None
        continue

    max_div = number // min_div

    M = max_div + min_div

    if M % 10 == 4:
        results.append([number, M])

        if len(results) == 5:
            break

print(results)