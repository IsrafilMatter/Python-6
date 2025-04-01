# Program description: Replicates rjust() functionality by adding spaces at the beginning
# Author: Israfil Palabay
# Date: April 1, 2025

def custom_rjust(text, width): # Function to right-justify a string by adding leading spaces
    return ' ' * (width - len(text)) + text # Calculate the number of spaces needed and prepend them to the text

# Print results
test_string = "Hello"
width = 10
result = custom_rjust(test_string, width)

print(f"Original: '{test_string}'")  # Show the original string
print(f"After rjust({width}): '{result}'")  # Show the right-justified string