pi = "3.14159265" # string
print( float(pi) )
# Convert the string to a float first, then cast that float to an int
print( int(float(pi)) )
mylist = [123,'hello world', []] # type: ignore
print( tuple(mylist) ) # type: ignore

# ==========================================
# MODERN PYTHON GUIDE: SAFE TYPECASTING & CONVERSIONS
# ==========================================

# 1. Safe Casting with Exception Handling
# Direct int("abc") throws ValueError. Always protect user input:
def safe_cast_int(val: str, default: int = 0) -> int:
    try:
        return int(val)
    except (ValueError, TypeError):
        return default

print("\n--- Safe Casting ---")
print(f"Safe cast '120': {safe_cast_int('120')}")
print(f"Safe cast 'invalid': {safe_cast_int('invalid', default=-1)}")

# 2. Truthy & Falsy Values (bool casting)
# Python evaluates empty collections and zeros as False:
print("\n--- Truthy / Falsy in Python ---")
falsy_values = ["", [], {}, 0, 0.0, None, set()]
for item in falsy_values:
    print(f"bool({repr(item)}): {bool(item)}")

# 3. Deduplicating Lists with set() Casting
duplicates = [1, 2, 2, 3, 4, 4, 4, 5]
unique_items = list(set(duplicates))
print(f"\nDeduplicated via set(): {unique_items}")