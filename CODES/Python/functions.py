# def function_name(optional_parameters):
#     # start of code block within indentation

def print_hello_world():
    print("hello world")
    #end of method

print_hello_world()

def add_two_things(thing1, thing2): # type: ignore
    combination = thing1 + thing2 # type: ignore
    print(combination) # type: ignore
add_two_things(10,20)
add_two_things('hello ','world')
add_two_things([123],[456])

#print(thing1) error thing one is not defined outside of the function

# Default arguments / optional parameters
def repeat_text(text, iterations=3):# type: ignore
    for i in range(iterations): # type:ignore
        print(text) #type: ignore
repeat_text("apple",1)
repeat_text("pear")

def odd_or_even(number): # type:ignore
    if (number % 2 == 0):
        return "even"
    else:
        return "odd"
result = odd_or_even(10)
print( f"{10} is {result}" )

def division_remainder(x, y=1):#type:ignore
    division = x // y #type:ignore
    remainder = x % y #type:ignore
    return (division, remainder) #type:ignore

# ==========================================
# MODERN PYTHON GUIDE: PROFESSIONAL FUNCTION DESIGN
# ==========================================

# 1. Modern Type Hinting & Docstrings
def calculate_area(width: float, height: float) -> float:
    """Calculate the area of a rectangle.
    
    Args:
        width: The width of the rectangle.
        height: The height of the rectangle.
        
    Returns:
        The computed area as a float.
    """
    return width * height

print(f"\nArea (5.5 x 4.0): {calculate_area(5.5, 4.0)}")

# 2. Flexible Arguments: *args and **kwargs
def log_event(event_type: str, *tags: str, **metadata: object) -> None:
    """Demonstrates packing variable positional (*args) and keyword (**kwargs) arguments."""
    print(f"\nEvent: [{event_type}]")
    if tags:
        print(f"  Tags: {', '.join(tags)}")
    if metadata:
        print(f"  Metadata: {metadata}")

log_event("LOGIN_SUCCESS", "auth", "security", user_id=101, ip="192.168.1.1")

# 3. Keyword-Only Arguments ('*' barrier)
# Everything after '*' MUST be passed by name, preventing confusing call sites:
def connect_server(host: str, port: int, *, timeout: int = 30, secure: bool = True) -> str:
    return f"Connecting to {host}:{port} (timeout={timeout}s, ssl={secure})"

# connect_server("localhost", 8080, 10, False)  # Syntax error! Must name timeout & secure
print(connect_server("localhost", 8080, timeout=15, secure=True))