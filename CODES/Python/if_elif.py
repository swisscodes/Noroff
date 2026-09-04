age = 25
has_license = True
is_tired = False
speed = 75
# Example with 'and': Both conditions must be True
if age >= 18 and has_license:
    print("Eligible to drive.")
else:
    print("Not eligible to drive.")
# Example with 'or': At least one condition must be True
if is_tired or speed > 60:
    print("Consider resting or reducing speed.")
else:
    print("Driving safely.")
