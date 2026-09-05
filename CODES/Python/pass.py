x = 'b'
if (x == 'a'): # type: ignore
    print( "x is 'a'" )
elif(x == 'b'):
    print( "x is 'b'" )
    pass # TODO: Do something useful here!
else:
    print( "x does not have 'a' or 'b'" )

# ==========================================
# MODERN PYTHON GUIDE: 'pass', ELLIPSIS, & STUBS
# ==========================================

# 1. 'pass' as a Syntactic Placeholder
# Python requires indentation under blocks (functions, classes, if/loops).
# 'pass' literally does nothing; it satisfies Python's syntax parser.
class TemporaryPlaceholder:
    pass

# 2. Modern Alternative: The Ellipsis (...)
# In modern Python, '...' (Ellipsis) is frequently used in function/type stubs:
def fetch_user_data(user_id: int) -> dict:
    ...  # Modern shorthand for pass, commonly seen in interfaces and protocols

# 3. Explicit Errors for Incomplete Code
# 'pass' silently succeeds. If you want to make sure unfinished code isn't
# accidentally called in production, raise NotImplementedError:
def calculate_advanced_metrics():
    # Calling this will alert the developer immediately:
    # raise NotImplementedError("Metrics engine has not been implemented yet!")
    pass

print("Executed pass and ellipsis placeholders cleanly.")

