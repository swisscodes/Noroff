user_age = 10
if(user_age >= 18):
    print("Access granted.")
elif(user_age < 18 and user_age>=13):
    print("Access limited: You are a teenager.")
else:
    print("Access denied: You are a child.")