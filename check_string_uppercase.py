# Program to check if string is uppercase without using isupper()
# Author: Israfil Palabay
# Date: March 28, 2025

def is_all_upper(s):
    # Check if there is at least one alphabetic character in `s`
    has_letter = any(c.isalpha() for c in s)
    
    # Check if all alphabetic characters in `s` are uppercase
    all_upper = all(not c.isalpha() or 'A' <= c <= 'Z' for c in s)
    
    # Return True only if both conditions are met
    return has_letter and all_upper

print(is_all_upper("HELLO"))  # Print Results