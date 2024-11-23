import re



# Define the mask and the divisor

mask = "3?12?14*5"

divisor = 1917

upper_limit = 10**10



# Convert the mask into a regular expression

mask_regex = mask.replace("?", r"\d").replace("*", r"\d*") + r"$"



# Compile the regex pattern for better performance

pattern = re.compile(mask_regex)



# Find numbers matching the mask and divisible by the divisor

results = []
first_divider = None

for number in range(300_000_000, upper_limit + 1):
    if number % divisor == 0:
        first_divider = number
        break

for number in range(first_divider, upper_limit + 1, divisor):

    if pattern.match(str(number)):
        if number % divisor == 0:
            results.append((number, number // divisor))




# Display results

import pandas as pd

results_df = pd.DataFrame(results, columns=["Number", "Quotient"])

import ace_tools_open as tools; tools.display_dataframe_to_user(name="Numbers Matching Mask and Divisible by 1917", dataframe=results_df)