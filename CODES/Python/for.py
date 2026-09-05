for (number) in [1,2,3,4,5,6]:
    print(f"{number} * {number} = {number * number}")

for (number) in range(1, 11):
    print(f"{number}")

# ==========================================
# MODERN PYTHON GUIDE: FOR LOOPS & ITERATION
# ==========================================

# 1. PEP 8 Clean Loop Syntax
# No parentheses needed around the loop variable:
# Good: `for number in ...:`  (Avoid: `for (number) in ...:`)

# 2. range() with Custom Step
print("\n--- Counting by Twos (Step argument) ---")
for even_num in range(2, 11, 2):
    print(f"Even: {even_num}", end=" ")
print()

# 3. The 'for ... else' Construct
# 'else' executes if the loop finishes WITHOUT encountering a 'break'
print("\n--- For ... Else Search Pattern ---")
search_item = 7
numbers = [1, 3, 5, 7, 9]

for val in numbers:
    if val == search_item:
        print(f"Found {search_item} in sequence!")
        break
else:
    print(f"{search_item} was not in the list.")

# 4. Modern Alternative: Comprehensions for Data Transformation
# Instead of initializing an empty list and running a for loop with .append():
squares = [x ** 2 for x in range(1, 7)]
print(f"\nCalculated squares using list comprehension: {squares}")