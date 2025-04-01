# Program description: Replicates startswith() functionality by checking if string starts with specified prefix
# Author: Israfil Palabay
# Date: March 31, 2025

def custom_startswith(text, prefix): # Function to check if a string starts with a given prefix
     return text[:len(prefix)] == prefix # Compare the start of the string with the prefix
 
# Iterate through test cases and print results
test_string = "Hello World"
prefixes = ["Hello", "World", "He"]
for prefix in prefixes:
    result = custom_startswith(test_string, prefix)
    print(f"'{test_string}' starts with '{prefix}': {result}") 