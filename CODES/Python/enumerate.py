letters = ["a","b","c","d"]
for (index,item) in enumerate(letters):
   print( f"Letter {item} is in position {index}" )

# ==========================================
# MODERN PYTHON GUIDE: enumerate() MASTERY
# ==========================================

# 1. Human-friendly 1-based indexing using 'start=1'
# In CLI tools and reports, users expect list counts starting at 1, not 0:
print("\n--- 1-based Indexing (start=1) ---")
tasks = ["Setup environment", "Write code", "Run tests", "Deploy"]
for rank, task in enumerate(tasks, start=1):
    print(f"{rank}. {task}")

# 2. Modern Clean Syntax (PEP 8)
# Avoid unnecessary parentheses around loop variables:
# Preferred: `for index, item in enumerate(...):`

# 3. Using enumerate in Dictionary Comprehension
# Quickly build a reverse lookup map (value -> position):
char_positions = {char: idx for idx, char in enumerate(letters, start=1)}
print(f"\nCharacter position lookup: {char_positions}")