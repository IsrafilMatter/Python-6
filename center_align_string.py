# Program to center align string with spaces without using center()
# Author: Israfil Palabay
# Date: March 28, 2025

def center_text(s, width):
    # Find how many extra spaces are needed
    pad = width - len(s)
    
    # If the text is shorter than the width
    if pad > 0:
        # Divide spaces: half on the left, half on the right
        left_spaces = pad // 2
        right_spaces = pad - left_spaces
        
        # Add spaces around the text
        return ' ' * left_spaces + s + ' ' * right_spaces
    else:
        # If text is already wide enough, return it as is
        return s

print(center_text("Hello", 10)) # Print Results