user_name = " Alice Smith "

cleaned_name = user_name.strip()  # Remove leading and trailing whitespace
print(f"Hello, {cleaned_name}!")

upper_name = cleaned_name.upper()  # Convert to uppercase
print(f"Uppercase: {upper_name}")


main_phrase = "powerful"
new_phrase = main_phrase.replace(main_phrase,"amazing")
print(new_phrase)

print(len(cleaned_name))  # Length of the cleaned name

print(f"Hello, {cleaned_name}! Your name has {len(cleaned_name)} characters.")

print(f"{cleaned_name + " " + upper_name[0:3]}")
print(f"{cleaned_name} {upper_name[0:3]}")

# ==========================================
# MODERN PYTHON GUIDE: STRING CLEANING & NORMALIZATION
# ==========================================

# 1. Modern Prefix/Suffix Removal (Python 3.9+)
# Unlike .strip("Mr. "), which removes any of the characters M, r, ., or space,
# .removeprefix() removes the EXACT prefix sequence safely:
prefixed_user = "Mr. Alice Smith"
cleaned_prefix = prefixed_user.removeprefix("Mr. ")
print(f"\nCleaned prefix: '{cleaned_prefix}'")

file_with_ext = "data_report.csv"
base_file = file_with_ext.removesuffix(".csv")
print(f"Base filename: '{base_file}'")

# 2. Modern Caseless Matching: casefold()
# .casefold() is more aggressive than .lower() and handles unicode/international characters:
email_input = "Alice.Smith@EXAMPLE.COM"
stored_email = "alice.smith@example.com"
print("Case-insensitive match:", email_input.casefold() == stored_email.casefold())

# 3. Fluent Method Chaining
raw_text = "   \t Python Developer \n  "
sanitized = raw_text.strip().title()
print(f"Sanitized: '{sanitized}'")