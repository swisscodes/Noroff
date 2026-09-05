#range(start_index, end_index)
for i in range(3):
    print("The value of i is:", i)

# ==========================================
# MODERN PYTHON GUIDE: DEEP DIVE INTO range()
# ==========================================

# 1. Full Syntax: range(start, stop, step)
# Note: 'stop' is always EXCLUSIVE (it does not include the stop value)
print("\n--- Custom Range Parameters ---")
print("range(5, 25, 5):", list(range(5, 25, 5)))

# 2. Negative Step (Counting Downwards)
print("range(10, 0, -2):", list(range(10, 0, -2)))

# 3. Memory Efficiency (Lazy Evaluation)
# In Python 3, range() does NOT generate all numbers in RAM at once.
# A range of 10 billion numbers consumes the exact same tiny memory footprint!
import sys
small_range = range(10)
huge_range = range(10_000_000_000)
print(f"Memory for 10 items: {sys.getsizeof(small_range)} bytes")
print(f"Memory for 10 billion items: {sys.getsizeof(huge_range)} bytes")

# 4. Instant O(1) Membership Check
# Python's range object calculates arithmetic membership mathematically,
# meaning checking 'x in range(...)' is instantaneous regardless of size:
print(f"Is 9_999_998 in huge_range? {9_999_998 in huge_range}")