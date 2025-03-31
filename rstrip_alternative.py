# Program description: Replicates rstrip() functionality by removing trailing spaces
# Author: Israfil Palabay
# Date: March 31, 2025

def custom_rstrip(text):
    while text and text[-1] == ' ': # Repeat while the string is not empty and the last character is a space
        text = text[:-1] # Remove the last character

# Print Results
test_string = "Hello World   "
result = custom_rstrip(test_string)

print(f"Original: '{test_string}'")  # Show the original string
print(f"After rstrip: '{result}'")   # Show the modified string