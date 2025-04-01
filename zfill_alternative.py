# Program description: Replicates zfill() functionality by adding zeros at the beginning
# Author: Israfil Palabay
# Date: March 31, 2025

def custom_zfill(text, width): # Function to pad a string with leading zeros to match a given width
    return '0' * (width - len(text)) + text # Calculate the number of zeros needed and prepend them to the text

test_string = "42"
width = 5
result = custom_zfill(test_string, width)

# Print results
print(f"Original: '{test_string}'")  # Show the original string
print(f"After zfill({width}): '{result}'")  # Show the zero-filled string