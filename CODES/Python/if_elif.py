age = 25
has_license = True
is_tired = False
speed = 75
# Example with 'and': Both conditions must be True
if age >= 18 and has_license:
    print("Eligible to drive.")
else:
    print("Not eligible to drive.")
# Example with 'or': At least one condition must be True
if is_tired or speed > 60:
    print("Consider resting or reducing speed.")
else:
    print("Driving safely.")

# ==========================================
# MODERN PYTHON GUIDE: LOGICAL OPERATORS & BEST PRACTICES
# ==========================================

# 1. Clean Boolean Checking (Avoid comparing directly to True/False)
# Good: `if has_license:`  |  Avoid: `if has_license == True:`
is_registered = True
if is_registered:
    print("\nUser is registered.")

# 2. Modern Condition Aggregation using all() and any()
# Check if ALL requirements are met:
driving_checks = [age >= 18, has_license, not is_tired]
if all(driving_checks):
    print("All driving safety criteria passed!")

# Check if ANY warning condition is triggered:
warning_conditions = [is_tired, speed > 70, age < 16]
if any(warning_conditions):
    print("Warning: At least one risk factor detected.")

# 3. Guard Clauses (Early Return Pattern)
# Instead of deeply nested if-else statements in functions, return early:
def evaluate_driver(driver_age: int, licensed: bool, tired: bool) -> str:
    if driver_age < 18:
        return "Cannot drive: Underage."
    if not licensed:
        return "Cannot drive: No license."
    if tired:
        return "Cannot drive: Driver is fatigued."
    return "Cleared to drive safely."

print("Driver assessment:", evaluate_driver(22, True, False))
