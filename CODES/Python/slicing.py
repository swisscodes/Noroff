# string[start_index : end_index]
s = "hello world again"
string1 = s[0:5]
string2 = s[6:11]
string3 = s[12:17]
print( string1 )
print( string2 )
print( string3 )

g = "hello world again"
g = "why not"
print(g)
path = r"C:\\Program Files\My Games\The Game\saved games\lost"
print( path )

# ==========================================
# MODERN PYTHON GUIDE: STRING SLICING MASTERY
# ==========================================

# 1. Omitting Indices (Shorthand)
text = "PythonProgramming"
print("\n--- Omitted Indices ---")
print("First 6 characters (text[:6]):", text[:6])   # 'Python'
print("From index 6 to end (text[6:]):", text[6:])   # 'Programming'

# 2. Negative Indices in Slices
print("\n--- Negative Slicing ---")
print("Last 7 characters (text[-7:]):", text[-7:])
print("Everything except last 7 (text[:-7]):", text[:-7])

# 3. Step in Slicing: [start:stop:step]
print("\n--- Step & Reversal ---")
alphabet = "abcdefghijklmnop"
print("Every 2nd char (alphabet[::2]):", alphabet[::2])
print("Reversed string (alphabet[::-1]):", alphabet[::-1])

# 4. Reusable 'slice' Objects
# Instead of hardcoding numbers in multiple places:
FIRST_FIVE = slice(0, 5)
print("Using slice object:", text[FIRST_FIVE])