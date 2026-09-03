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