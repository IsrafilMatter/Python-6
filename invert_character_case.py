# Program to swap character case without using swapcase()
# Author: Israfil Palabay
# Date: March 28, 2025

def swap_case(s):
    # Convert each letter to the opposite case
    return ''.join(
        chr(ord(c) ^ 32) if c.isalpha() else c  # Flip case using XOR 32
        for c in s  # Go through each character in the string
    )

print(swap_case("Hello WORLD"))  # Print Results