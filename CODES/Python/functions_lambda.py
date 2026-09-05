add_numbers = lambda a,b : a + b #type:ignore


numbers = [2,3,6,7]
def double_number(number):#type:ignore
    return 2 * number#type:ignore
n_traditional = map(double_number, numbers)#type:ignore
n_lambda = map(lambda n: 2*n, numbers)  # here is the lambda    lambda n: 2*n
print( f"Traditional method: {list(n_traditional)}" )#type:ignore
print( f"Lambda function: {list(n_lambda)}" )




products: list[dict[str, str | int]] = [
    {"name": "Laptop", "price": 1200, "quantity": 10},
    {"name": "Mouse", "price": 25, "quantity": 150},
    {"name": "Keyboard", "price": 75, "quantity": 70},
    {"name": "Monitor", "price": 300, "quantity": 30},
]
print("Original products list:")
for p in products:
    print(p)
print("-" * 30)
# Sort products by price (ascending) using a lambda function as the key
# The lambda function takes a 'product' dictionary and returns its 'price'
sorted_by_price = sorted(products, key=lambda product: product['price'])#type:ignore
print("Products sorted by price:")
for p in sorted_by_price:#type:ignore
    print(p)#type:ignore
print("-" * 30)
# Sort products by quantity (descending) using a lambda function
sorted_by_quantity_desc = sorted(products, key=lambda product: product['quantity'], reverse=True)#type:ignore
print("Products sorted by quantity (descending):")
for p in sorted_by_quantity_desc:#type:ignore
    print(p)#type:ignore
print("-" * 30)
# Sort products by name (alphabetically)
sorted_by_name = sorted(products, key=lambda product: product['name'])#type:ignore
print("Products sorted by name:")
for p in sorted_by_name:#type:ignore
    print(p)#type:ignore
    print(p)#type:ignore

# ==========================================
# MODERN PYTHON GUIDE: LAMBDAS, OPERATOR & COMPREHENSIONS
# ==========================================

# 1. PEP 8 Guideline on Lambdas
# Avoid assigning a lambda directly to an identifier (e.g., `f = lambda x: ...`).
# Use standard `def f(x): ...` instead. It provides proper tracebacks and docstrings.
# Lambdas shine exclusively as throwaway inline arguments.

# 2. Faster & Cleaner Sorting with 'operator.itemgetter'
# Standard library 'operator' is implemented in C and runs faster than lambda:
import operator

# Instead of key=lambda x: x['price'], use operator.itemgetter:
fast_sorted = sorted(products, key=operator.itemgetter('price'))
print("\nSorted using operator.itemgetter('price'):")
for p in fast_sorted:
    print(f"  {p['name']}: ${p['price']}")

# 3. Modern Preference: Comprehensions over map() and filter()
# In modern Python, list comprehensions are preferred over map/filter with lambdas:
# Instead of: list(map(lambda n: n * 2, numbers))
doubled_comprehension = [n * 2 for n in numbers]
# Instead of: list(filter(lambda n: n > 3, numbers))
filtered_comprehension = [n for n in numbers if n > 3]

print(f"\nDoubled via comprehension: {doubled_comprehension}")
print(f"Filtered (>3) via comprehension: {filtered_comprehension}")