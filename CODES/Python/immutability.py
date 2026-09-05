s = "hello world"
# accessing a single character
print( s[0] )
# attempting to change character
s[0] = 'w' # type: ignore  // i know its error but i want to see it in action

# ==========================================
# MODERN PYTHON GUIDE: IMMUTABILITY & HOW TO "MODIFY" STRINGS
# ==========================================

# 1. Why Strings are Immutable
# In Python, str, int, float, and tuple are immutable (cannot be modified in-place).
# This provides safety, thread-safety, and allows strings to be dictionary keys.

# 2. How to Safely "Modify" a String (Create a New One)
# Method A: Slicing and Concatenation
original = "hello world"
modified_slice = "w" + original[1:]
print(f"\nModified via slicing: '{modified_slice}'")

# Method B: .replace()
modified_replace = original.replace("h", "w", 1)
print(f"Modified via replace: '{modified_replace}'")

# Method C: Converting to a mutable list of characters, changing it, and joining back
chars = list(original)
chars[0] = "w"
modified_list = "".join(chars)
print(f"Modified via list conversion: '{modified_list}'")

# 3. Inspecting Object Identity with id()
# Notice how 'original' and 'modified_slice' have different memory addresses:
print(f"Original id: {id(original)}, Modified id: {id(modified_slice)}")