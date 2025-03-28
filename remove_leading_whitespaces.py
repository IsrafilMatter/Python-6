# Program to remove leading whitespace characters without using lstrip()
# Author: Israfil Palabay
# Date: March 28, 2025

def strip_left(s):
    index = 0 # Iterate while there are spaces
    while index < len(s) and s[index].isspace(): index += 1 # Move index forward
    return s[index:] # Return the substring from the first non-space character

print(strip_left("     Hello")) # Print Results