def while_countdown(n: int):
    while n > 0:
        print(n)
        n -= 1
    print("Countdown finished!")

while_countdown(5)

"""
Infinity loop happens when we have a recursive function or a loop that doesnt have proper exit condition
for example the while loop above if we havent decremented n, there will be no way our program will understand
when or how to stop the loop, and it will keep running forever. this is called infinity loop.
"""

# ==========================================
# MODERN PYTHON GUIDE: COUNTDOWNS & RECURSION
# ==========================================

# 1. The Pythonic Way: Using range() with negative step
# In modern Python, counting down is usually cleaner with a for-loop:
def for_countdown(start: int) -> None:
    print("\n--- Pythonic Countdown using range(start, 0, -1) ---")
    for sec in range(start, 0, -1):
        print(f"T-minus {sec}...")
    print("Blastoff! 🚀")

for_countdown(3)

# 2. Safe Recursion with a Base Case
# Every recursive function MUST have a base case to avoid RecursionError (stack overflow)
def recursive_countdown(n: int) -> None:
    if n <= 0:  # BASE CASE: Stop condition
        print("Reached 0! Safe exit.")
        return
    print(f"Recursive tick: {n}")
    recursive_countdown(n - 1)  # RECURSIVE STEP: Moving towards base case

print("\n--- Safe Recursive Countdown ---")
recursive_countdown(3)