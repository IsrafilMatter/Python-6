# Program to check string ending without using endswith()
# Author: Israfil Palabay
# Date: March 28, 2025

def ends_with(s, suffix):
    # Check if `suffix` is longer than `s`, in which case `s` cannot end with `suffix`
    if len(suffix) > len(s):
        return False
    
    # Compare the last `len(suffix)` characters of `s` with `suffix`
    return s[-len(suffix):] == suffix  

print(ends_with("Hello World", "World"))  # Print Results