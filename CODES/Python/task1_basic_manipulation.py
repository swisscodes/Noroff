main_phrase = "Python is a powerful language!"

word_python = main_phrase[0:6]

print(word_python)
print(f"f stringed {word_python}")

word_powerful = main_phrase[12:20]
print(f"f stringed {word_powerful}")

language = main_phrase[21:29]
print(f"f stringed {language}")


print(f"The {word_python} programming language is very {word_powerful}.")

# ==========================================
# MODERN PYTHON GUIDE: DYNAMIC STRING MANIPULATION
# ==========================================

# 1. Dynamic Search (Avoid fragile hardcoded slice indices)
# Instead of guessing indices [12:20], search dynamically with .find():
search_target = "powerful"
start_pos = main_phrase.find(search_target)
end_pos = start_pos + len(search_target)
extracted_dynamic = main_phrase[start_pos:end_pos]
print(f"\nDynamically extracted '{extracted_dynamic}' at [{start_pos}:{end_pos}]")

# 2. Modern Prefix & Suffix Checking
print("\n--- StartsWith and EndsWith ---")
print("Starts with 'Python'?", main_phrase.startswith("Python"))
print("Ends with '!'?", main_phrase.endswith("!"))

# 3. Dynamic Word Splitting (Tokenization)
# Modern code splits by whitespace and strips punctuation cleanly:
words = [w.strip("!.,") for w in main_phrase.split()]
print(f"Extracted clean words list: {words}")