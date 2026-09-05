people = { "Alice" : 25, "Bob" : 33 } # assignment
# accessing value using a key
print( people["Alice"] )
# changing a value
people["Bob"] = 34
print( people["Bob"] )

# ==========================================
# MODERN PYTHON DICTIONARY GUIDE & BEST PRACTICES
# ==========================================

# 1. PEP 8 Spacing & Modern Formatting
# In modern Python, avoid extra spaces inside brackets/colons:
people_modern = {"Alice": 25, "Bob": 34}

# 2. Modern Output using f-strings (introduced in Python 3.6+)
print(f"\n--- Modern Output ---")
print(f"Alice's age: {people_modern['Alice']}")

# 3. Safe Access with .get()
# Direct access (people["Charlie"]) crashes with a KeyError if the key doesn't exist.
# .get() returns None (or a custom default) instead of crashing:
charlie_age = people_modern.get("Charlie", "Not found")
print(f"Charlie's age (safe access): {charlie_age}")

# 4. Adding New Key-Value Pairs
people_modern["Charlie"] = 28
print(f"Added Charlie: {people_modern}")

# 5. Checking if a Key Exists ('in' keyword)
if "Alice" in people_modern:
    print(f"Alice is in the directory!")

# 6. Removing Items Safely with .pop()
# .pop() removes the key and returns its value
removed_age = people_modern.pop("Bob", None)
print(f"Removed Bob (age {removed_age}). Remaining: {people_modern}")

# 7. Modern Iteration with .items(), .keys(), .values()
print("\nIterating over key-value pairs:")
for name, age in people_modern.items():
    print(f"  • {name} is {age} years old")

# 8. Modern Dictionary Merging (Python 3.9+ '|' union operator)
new_members = {"Diana": 22, "Evan": 31}
team = people_modern | new_members
print(f"\nMerged team using '|' operator:\n{team}")

# 9. Dictionary Comprehension (creating dictionaries cleanly)
# Example: Filter people who are 25 or older
older_people = {name: age for name, age in team.items() if age >= 25}
print(f"\nPeople 25 and older (Dict Comprehension):\n{older_people}")