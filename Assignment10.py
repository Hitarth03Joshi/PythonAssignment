# 10. Solve in Fewest Steps
# Given a string consisting of letters and digits, write a Python program to separate and sort letters
# and digits individually and then concatenate them, letters first and digits after, with each group
# sorted individually.
# Your solution should be concise yet clear.
# Example:
# • Input: "B4A1D3"
# • Output: "ABD134"

def separate_and_sort(s):
    letters = sorted([c for c in s if c.isalpha()])
    digits = sorted([c for c in s if c.isdigit()])
    return ''.join(letters + digits)

# Example
print(separate_and_sort("B4A1D3"))  # Output: ABD134
