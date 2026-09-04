x = -10
result = None
# traditional method
if (x < 0): 
   result = "Negative"
else:
   result = "Non-negative"
print(result)
# ternary expression method
result = "Negative" if (x < 0) else "Non-negative"
print(result)