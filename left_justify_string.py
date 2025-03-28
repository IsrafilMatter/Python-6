# Program to left justify string with spaces without using ljust()
# Author: Israfil Palabay
# Date: March 28, 2025

def align_left(s, width):
    # If `s` is shorter than `width`, pad it with spaces on the right
    return s + ' ' * (width - len(s)) if len(s) < width else s  

print(align_left("Hello", 10))  # Print Results
