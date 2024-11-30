from math import factorial as f

text = "Себе на уме городничий, и чин дорог ему, а не бес."
# text = "У дорог кину лес. Кину ни к селу ни к городу."

text = text.lower().replace(" ", "").replace(",","").replace(".", "")

frequency = {}

for letter in text:
    if letter in frequency:
        frequency[letter] += 1
    else:
        frequency[letter] = 1

print(frequency)

Xk = []

for key, value in frequency.items():
    if value % 2 == 1:
        # нечетное кол-во
        if value > 1:
            # убираем 1 символ, остальные идут в часть палиндрома
            Xk.append((value - 1) // 2)
    else:
        Xk.append(value // 2)

print(Xk)

p = 1

for x in Xk:
    p *= f(x)

s = sum(Xk)

print("sum:", s)
print("p:", p)

result = f(s) / p

print("result:", result)
