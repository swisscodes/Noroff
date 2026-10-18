# Relative Path
f = open("alice.txt", "r")  # Open file in read mode
print(f"Filename: {f.name}")  # Print the name of the file
print(f"File contents: {f.read()}")  # Read entire file contents
f.close()  # IMPORTANT: Always close the file to release system resources
# Absolute Path
f = open(r"C:\Program Files\py-alice\alice.txt", "r")
print(f"Filename: {f.name}")
f.close()