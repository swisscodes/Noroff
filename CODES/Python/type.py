x = 100
# print the type of our variable to console
print( type(x) )
# determine if our variable is a particular type
print( isinstance(x, str) )
print( isinstance(x, int) ) # type: ignore

# ==========================================
# MODERN PYTHON GUIDE: TYPE INSPECTION BEST PRACTICES
# ==========================================

# 1. type() vs isinstance() (The Inheritance Difference)
# 'type(obj) is T' checks for the EXACT class only.
# 'isinstance(obj, T)' also correctly recognizes subclasses!
# (For instance, bool is a subclass of int: isinstance(True, int) is True, but type(True) is bool)
print("\n--- type() vs isinstance() ---")
flag = True
print(f"type(True) is int:       {type(flag) is int}")
print(f"isinstance(True, int):   {isinstance(flag, int)}")

# 2. Checking Multiple Types at Once
# Pass a tuple of candidate types to isinstance():
val: object = 45.6
if isinstance(val, (int, float)):
    print(f"\n{val} is a numeric type (int or float)!")

# 3. Modern Type Dispatch with match / case (Python 3.10+)
def describe_data(data: object) -> str:
    match data:
        case int() | float():
            return f"Numeric value: {data}"
        case str():
            return f"Text sequence of length {len(data)}"
        case list() | tuple():
            return f"Container with {len(data)} items"
        case _:
            return "Unknown type"

print(describe_data("Hello Modern Python"))
print(describe_data([1, 2, 3, 4]))