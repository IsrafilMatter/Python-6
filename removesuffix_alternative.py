# Program description: Replicates removesuffix() functionality by removing specified suffix
# Author: Israfil Palabay
# Date: March 31, 2025

def custom_removesuffix(text, suffix): # Function to remove a specified suffix from a string
    if text.endswith(suffix): # Check if the string ends with the given suffix
        return text[:-len(suffix)]# Remove the suffix by slicing the string
    return text # Return the original string if the suffix is not found

# Print Results