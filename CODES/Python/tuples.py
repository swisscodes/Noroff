x = ()
y = (1,2,3,4)
z = ('one',1,[1],(1),None)

x = (1,"hello world") # assignment

# accessing elements
print(x[0],x[1])

# unpacking
y, z = x
print(y)
print(z)

# creating tuple from other sequence types
list_items = [1,2,3,4]
tuple_created_from_list = tuple(list_items)
tupB = (4, 5, 6)
tupC = tuple([7,8,9])

# tuple unpacking
# 1. Basic Unpacking (Variables must match element count)
a, b, c = tupC
print(f"Basic unpacking: a={a}, b={b}, c={c}")

# 2. Extended / Starred Unpacking (*rest captures remaining items as a list)
numbers = (10, 20, 30, 40, 50)
first, *middle, last = numbers
print(f"Starred unpacking: first={first}, middle={middle}, last={last}")

# 3. Variable Swapping (Pythonic swap without temp variable)
num1, num2 = 100, 200
num1, num2 = num2, num1
print(f"Swapped: num1={num1}, num2={num2}")

# 4. Ignoring Unwanted Elements using '_' (throwaway variable)
record = ("Alice", 28, "Engineer", "Oslo")
name, _, role, _ = record
print(f"Ignored fields: name={name}, role={role}")

# 5. Nested Tuple Unpacking
location = ("Bergen", (60.39, 5.32))
city, (lat, lon) = location
print(f"Nested unpack: {city} is at ({lat}, {lon})")

# ==========================================
# MODERN PYTHON GUIDE: TUPLE QUIRKS & PERFORMANCE
# ==========================================

# 1. The Single-Element Tuple Gotcha
# Writing (42) is just an integer inside parentheses!
# A trailing comma is MANDATORY to make it a tuple:
not_a_tuple = (42)
is_a_tuple = (42,)
print(f"\nType of (42):  {type(not_a_tuple).__name__}")
print(f"Type of (42,): {type(is_a_tuple).__name__}")

# 2. Immutability vs Contained Mutable Objects
# The tuple container cannot change, BUT mutable objects inside it CAN!
mutable_inside_tuple = (100, ["apple", "banana"])
# mutable_inside_tuple[0] = 200  # Raises TypeError!
mutable_inside_tuple[1].append("cherry")  # Allowed! Modifying the contained list
print(f"\nTuple containing mutated list: {mutable_inside_tuple}")

# 3. Memory & Performance: Tuple vs List
import sys
sample_list = [1, 2, 3, 4, 5]
sample_tuple = (1, 2, 3, 4, 5)
print(f"\nList memory size:  {sys.getsizeof(sample_list)} bytes")
print(f"Tuple memory size: {sys.getsizeof(sample_tuple)} bytes (Tuples are lighter & faster!)")