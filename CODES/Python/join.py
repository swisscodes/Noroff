countries = ["norway","sweden","united states","canada"]
# join using comma (,)
commas = ",".join(countries) 
print("commas:", commas )
# join using newlines
newlines = "\n".join(countries)
print( "newlines\n", newlines, sep="" ) # by default, print injects a space between arguments, 
#so the output will have a space before the first country. thats why we added sep="" to remove the space.

#Option 2: Use an f-string (Best Practice)
#Combine everything into a single string argument so print never injects a separator:

print(f"newlines\n{newlines}")

# ==========================================
# MODERN PYTHON GUIDE: STRING JOINING BEST PRACTICES
# ==========================================

# 1. Joining Non-String Data (Numbers, Objects)
# .join() requires all items to be strings. Pass a generator expression to convert them:
numbers = [10, 20, 30, 40, 50]
formatted_nums = " -> ".join(str(n) for n in numbers)
print(f"\nFormatted numbers: {formatted_nums}")

# 2. Performance: Why .join() is the Gold Standard
# In Python, strings are immutable. Using `text += word` inside a loop creates a new string
# in memory on every iteration (O(N^2) time complexity).
# `.join()` preallocates the exact memory needed once (O(N) time complexity).

# 3. Capitalizing While Joining
capitalized_countries = ", ".join(c.title() for c in countries)
print(f"Capitalized: {capitalized_countries}")