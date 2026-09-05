x = ['a','b','c','d']
y = [100,200,300,400]
for (item) in zip(x,y):
   item_x = item[0]
   item_y = item[1]
   print( f"{item}: Item {item_x} has the value NOR{item_y}" )


#Similar to enumerate, we can also use tuple unpacking in a for loop to access each item easily:
items = []
products = ["cheese", "chocolate", "pie", "pants"]
prices = [29.99, 15.50, 17.99, 199.99]
sales = [2, 10, 0, 200]
for (p1, p2, s) in zip(products,prices,sales):
   items.append({"product":p1, "price":p2, "sale":s}) # type: ignore
   print( f"{p1} sold for a profit of {p2 * s}" )
   print(items ) # type: ignore

# ==========================================
# MODERN PYTHON GUIDE: zip() BEST PRACTICES
# ==========================================

# 1. Instant Dictionary Creation from Two Lists
# One of the most common, powerful idioms in modern Python:
keys: list[str] = ["id", "username", "email"]
values: list[object] = [101, "codemaster", "code@example.com"]
user_profile: dict[str, object] = dict(zip(keys, values))
print(f"\nBuilt dict with dict(zip(...)):\n{user_profile}")

# 2. Modern Safety: 'strict=True' (Introduced in Python 3.10)
# By default, zip() silently stops at the shortest list.
# With strict=True, it raises a ValueError if sequences have different lengths:
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30]  # Mismatched length!

try:
    for name, age in zip(names, ages, strict=True):
        print(name, age)
except ValueError as err:
    print(f"\nCaught mismatched length with strict=True: {err}")

# 3. Handling Uneven Lists with itertools.zip_longest
import itertools
print("\n--- itertools.zip_longest with fillvalue ---")
for name, age in itertools.zip_longest(names, ages, fillvalue="Unknown"):
    print(f"  • {name}: {age}")

# 4. Unzipping Data with zip(*...)
coordinates = [(1, 10), (2, 20), (3, 30)]
x_coords, y_coords = zip(*coordinates)
print(f"\nUnzipped X: {x_coords}, Unzipped Y: {y_coords}")