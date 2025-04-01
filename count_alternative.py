# Program description: Replicates count() functionality by counting occurrences of substring
# Author: Israfil Palabay
# Date: April 1, 2025

def custom_count(text, sub):
    count = 0
    start = 0
    while True:
        start = text.find(sub, start)
        if start == -1:
            break
        count += 1
        start += 1
    return count

test_string = "hello hello hello"
substring = "hello"
result = custom_count(test_string, substring)

print(f"String: '{test_string}'")
print(f"Count of '{substring}': {result}") 
