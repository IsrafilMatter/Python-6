# Program description: Replicates islower() functionality by checking if all characters are lowercase
# Author: Israfil Palabay
# Date: March 31, 2025

def custom_islower(text): # Function to check if all alphabetic characters in a string are lowercase
     return all('a' <= c <= 'z' for c in text if c.isalpha()) # Verify that all letters in the string are lowercase
 
# Iterate through test cases and print results
test_strings = ["hello world", "Hello World", "123", "hello123"]
for s in test_strings:
    result = custom_islower(s)
    print(f"'{s}' is lowercase: {result}") 