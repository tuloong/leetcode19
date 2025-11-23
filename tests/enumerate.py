s = "Python"

print(f"The string is: '{s}'")
print("-" * 20)

# Loop through the string using enumerate
for right, ch in enumerate(s):
    print(f"Index: {right}, Character: '{ch}'")

# A more common use case: building a dictionary of character positions
char_indices = {}
for right, ch in enumerate(s):
    char_indices[ch] = right

print("\nResulting dictionary:", char_indices)
