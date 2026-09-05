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

# ==========================================
# MODERN PYTHON GUIDE: TERNARY & CONDITIONAL EXPRESSIONS
# ==========================================

# 1. Inline Ternary inside f-strings
score = 88
print(f"\nResult: {'Passed' if score >= 50 else 'Failed'}")

# 2. Ternary Assignment for Default Fallbacks
raw_username = ""
# If raw_username is empty, fallback to "Anonymous"
username = raw_username if raw_username else "Anonymous"
print(f"Active user: {username}")

# 3. Modern Multi-branch: Chained Ternary vs Dictionary Mapping
# Chained ternary (use sparingly for readability):
status_code = 200
status_msg = "OK" if status_code == 200 else ("Not Found" if status_code == 404 else "Error")
print(f"Status ({status_code}): {status_msg}")

# Best Practice Alternative for multiple branches: Dictionary lookup with .get()
http_status = {
    200: "OK",
    201: "Created",
    400: "Bad Request",
    404: "Not Found",
    500: "Internal Server Error",
}
code = 404
print(f"Modern Lookup ({code}): {http_status.get(code, 'Unknown Status')}")