counter = 0
while(counter < 5):
    print ( "The value of counter is:", counter+1 )
    counter += 1
print( "While loop complete. Our final value is:", counter )

# ==========================================
# MODERN PYTHON GUIDE: WHILE LOOPS & CONTROL FLOW
# ==========================================

# 1. 'break' and 'continue' Controls
print("\n--- Break and Continue ---")
n = 0
while n < 10:
    n += 1
    if n % 2 == 0:
        continue  # Skip even numbers
    if n > 7:
        break     # Stop loop when n exceeds 7
    print(f"Odd number <= 7: {n}")

# 2. The 'while ... else' Construct
# The 'else' block executes ONLY if the while loop completes without hitting a 'break'
print("\n--- While ... Else Pattern ---")
target = 4
num = 1
while num < 5:
    if num == target:
        print(f"Target {target} found at step {num}!")
        break
    num += 1
else:
    print("Target was not found in the search space.")

# 3. Modern Walrus Operator (:=) in While Loops (Python 3.8+)
# The walrus operator assigns and evaluates in an expression simultaneously
print("\n--- Walrus Operator (:=) ---")
commands = ["start", "process", "stop", "extra"]
cmd_iter = iter(commands)

# Read command and check condition in one clean line:
while (cmd := next(cmd_iter, None)) and cmd != "stop":
    print(f"Executing command: {cmd}")