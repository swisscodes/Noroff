user_age = 10
if(user_age >= 18):
    print("Access granted.")
elif(user_age < 18 and user_age>=13):
    print("Access limited: You are a teenager.")
else:
    print("Access denied: You are a child.")

# ==========================================
# MODERN PYTHON GUIDE: CONDITIONALS & PATTERN MATCHING
# ==========================================

# 1. Chained Comparisons (Pythonic Way)
# Instead of: (age < 18 and age >= 13), write: 13 <= age < 18
print("\n--- Modern Chained Comparison ---")
age = 15
if age >= 18:
    status = "Adult (Full access)"
elif 13 <= age < 18:  # Clean, readable mathematical chaining
    status = "Teenager (Limited access)"
else:
    status = "Child (Access denied)"
print(f"Age {age}: {status}")

# 2. Encapsulation with Type Hints and Guard Clauses
def check_access(age: int) -> str:
    """Determine user access level based on age."""
    if age < 0:
        return "Invalid age provided."
    if age >= 18:
        return "Access granted."
    if 13 <= age < 18:
        return "Access limited: You are a teenager."
    return "Access denied: You are a child."

print(f"Function check (age 10): {check_access(10)}")
print(f"Function check (age 21): {check_access(21)}")

# 3. Modern Structural Pattern Matching (Python 3.10+ 'match/case')
# Using guards (if condition inside case):
print("\n--- Structural Pattern Matching (match/case) ---")
test_age = 17
match test_age:
    case a if a >= 18:
        print("Match: Adult")
    case a if 13 <= a < 18:
        print("Match: Teenager")
    case _:
        print("Match: Child")