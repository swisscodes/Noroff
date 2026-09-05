students = ["Alice", "Bob", "Charlie", "David", "Eve"]

for student in students:
    print(f"Hello, {student}!")


for student in range(len(students)):
    print("range starts here")
    print(f"Hello, {students[student]}!")

items = ["apple", "banana", "cherry"]
prices = [1.50, 0.75, 2.00]

# Find the maximum character length across all items
the_length = max(len(item) for item in items)

for item, price in zip(items, prices):
    if(len(item) > the_length):
        the_length = len(item)
    print(f"The price of {item:<{the_length}} is ${price:.2f}.")

# ==========================================
# MODERN PYTHON GUIDE: PYTHONIC ITERATION
# ==========================================

# 1. Why to Avoid `range(len(...))` (The Pythonic Alternative)
# `range(len(...))` is an anti-pattern carried over from C/Java.
# In modern Python, if you need index AND item, use `enumerate()`:
print("\n--- Pythonic Index & Value with enumerate() ---")
for idx, student in enumerate(students, start=1):
    print(f"Student #{idx}: {student}")

# 2. Clean CLI Column Formatting with zip and f-strings
print("\n--- Clean Table Output ---")
col_width = max(len(item) for item in items)
for item, price in zip(items, prices):
    # Formats column to max width, left-aligned, price with 2 decimals
    print(f"{item.capitalize():<{col_width}} | ${price:>6.2f}")