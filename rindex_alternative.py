# Program description: Replicates rindex() functionality by finding last occurrence of substring
# Author: Israfil Palabay
# Date: April 1, 2025

def custom_rindex(text, sub): # For each possible starting position from end to beginning
    for i in range(len(text) - len(sub), -1, -1): # Check if substring matches starting from this position
        if text[i:i+len(sub)] == sub: # If match found, return the position
            return i
    raise ValueError("Substring not found") # If no match found, raise ValueError

test_string = "Hello World World"
substring = "World"
try: # Print Results
    result = custom_rindex(test_string, substring)
    print(f"String: '{test_string}'")
    print(f"Last index of '{substring}': {result}")
except ValueError as e:
    print(e) 