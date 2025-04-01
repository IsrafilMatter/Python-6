# Program description: Replicates index() functionality by finding first occurrence of substring
# Author: Israfil Palabay
# Date: April 1, 2025

def custom_index(text, sub):
    for i in range(len(text) - len(sub) + 1):
        if text[i:i+len(sub)] == sub:
            return i
    raise ValueError("Substring not found")

test_string = "Hello World"
substring = "World"
try:
    result = custom_index(test_string, substring)
    print(f"String: '{test_string}'")
    print(f"Index of '{substring}': {result}")
except ValueError as e:
    print(e) 