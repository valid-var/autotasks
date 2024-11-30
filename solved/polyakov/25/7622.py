import re

"""
(Демо-2025) Назовём маской числа последовательность цифр, в которой также могут встречаться следующие символы:
— символ «?» означает ровно одну произвольную цифру;
— символ «*» означает любую последовательность цифр произвольной длины; в том числе «*» может задавать и пустую последовательность.
Например, маске 123*4?5 соответствуют числа 123405 и 12300425.
Среди натуральных чисел, не превышающих 1010, найдите числа, удовлетворяющих маске 3?12?14*5 и делящиеся на 1917 без остатка. 
Запишите в ответе найденные числа в порядке возрастания, справа от каждого числа запишите частное от его деления на 1917. 
"""

# Define the mask and the divisor

mask = "3?12?14*5"

divisor = 1917

upper_limit = 10**10

# Convert the mask into a regular expression

mask_regex = mask.replace("?", r"\d").replace("*", r"\d*") + r"$"

print(mask_regex)

# Compile the regex pattern for better performance

pattern = re.compile(mask_regex)

# Find numbers matching the mask and divisible by the divisor

results = []
first_divider = None

for number in range(300_000_000, upper_limit + 1):
    if number % divisor == 0:
        first_divider = number
        break

print(first_divider)

for number in range(first_divider, upper_limit + 1, divisor):

    if pattern.match(str(number)):
        results.append((number, number // divisor))


print(results)