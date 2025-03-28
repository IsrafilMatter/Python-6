# Program to convert string to lowercase without using lower()
# Author: Israfil Palabay
# Date: March 28, 2025

def to_lower(s):
    # Convert each character in `s` to lowercase if it is an uppercase letter (A-Z)
    return ''.join(
        chr(ord(c) + 32) if 'A' <= c <= 'Z' else c  # Convert uppercase to lowercase
        for c in s  # Iterate over each character in `s`
    )
print(to_lower("Hello WORLD"))  # Print results