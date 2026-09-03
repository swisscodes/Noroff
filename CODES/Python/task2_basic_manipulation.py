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