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

# ==========================================
# MODERN PYTHON GUIDE: ADVANCED F-STRINGS & FORMATTING
# ==========================================

# 1. Self-Documenting Expressions / Debugging with '=' (Python 3.8+)
# Prints the variable name AND value automatically:
print(f"\n--- Debugging Specifier ---")
print(f"{product_name=}, {price=:.2f}, {quantity=}")

# 2. Number Formatting (Thousands Separators, Percentages, Currency)
large_number = 1_000_000.75
ratio = 0.8542
print("\n--- Advanced Numeric Formats ---")
print(f"Comma separator:    {large_number:,.2f}")
print(f"Underscore separator:{large_number:_.2f}")
print(f"Percentage:         {ratio:.1%}")

# 3. Center Alignment and Fill Characters
title = "INVOICE SUMMARY"
print("\n--- Alignment & Fill ---")
print(f"{title:=^35}")
print(f"{'Item':<15} {'Qty':^7} {'Total':>10}")
print(f"{product_name:<15} {quantity:^7} {price * quantity:>10,.2f}")

