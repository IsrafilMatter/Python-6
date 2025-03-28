# Program to capitalize first letter of each word without using title()
# Author: Israfil Palabay
# Date: March 28, 2025

def title_case(s):
    # Split the string into words, capitalize the first letter of each word,
    # and make the rest of the letters lowercase
    return ' '.join(
        word[0].upper() + word[1:].lower()  # Capitalize first letter, lowercase rest
        for word in s.split()  # Split string into words
    )

print(title_case("hello world PYTHON"))  # Print results