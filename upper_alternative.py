# Program description: Replicates upper() functionality by converting string to uppercase
# Author: Israfil Palabay
# Date: March 31, 2025

def custom_upper(text): # Function to convert lowercase letters to uppercase
    return ''.join(chr(ord(c) - 32) if 'a' <= c <= 'z' else c for c in text) # Convert each lowercase letter to uppercase using ASCII values

# Print results