product_name = "Laptop"
price = 1234.5678
quantity = 15
print(f"{product_name:>15}")

long_description = "A high-performance computing device with a sleek design."

#Format Specifier: {long_description:.20}
print(f"{long_description:.20}")  # Limit to 20 characters

#slicing
print(f"{long_description[0:20]}")  # Limit to 20 characters using slicing

# The Real Advantage: Combining Truncation with Padding
# The format specifier shines when you need to construct clean, 
# aligned CLI tables or log outputs where fields must fit an exact column width whether they are too short or too long:

print(f"{"NOK":>6}{price:>10.2f}")  # Right-align the price with 2 decimal places

print(f"{quantity:>5}")  # Left-align the quantity
"""
This is not an official comment, 
but Python ignores it because it is not 
assigned to any variable.
"""
