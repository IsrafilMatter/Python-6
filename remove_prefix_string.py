# Program to remove prefix from string without using removeprefix()
# Author: Israfil Palabay
# Date: March 28, 2025

def remove_start(s, prefix):
    # Check if the string `s` starts with the given `prefix`
    if s.startswith(prefix): 
        return s [len(prefix):] # If true, remove the prefix by slicing the string from index `len(prefix)` onward
    else:
        return s # If false, return the original string unchanged
    
print(remove_start("Hello World", "Hello ")) # Print Results