import os
# 1. Get the Current Working Directory (CWD)
# This tells you exactly where your Python script is currently executing.
current_dir = os.getcwd()
print(f"Current Directory: {current_dir}")
# 2. Create a new directory
# We'll create a folder named 'test_folder' in the current directory.
folder_name = "test_folder"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print(f"Created directory: '{folder_name}'")
else:
    print(f"Directory '{folder_name}' already exists.")
# 3. Join paths safely using os.path.join
# This ensures the correct slashes are used regardless of the operating system.
file_path = os.path.join(current_dir, folder_name, "sample.txt")
print(f"Safe file path generated: {file_path}")
# 4. List contents of a directory
# This shows all files and folders in the specified path.
print(f"Contents of current directory: {os.listdir(current_dir)}")
# 5. Clean up: Remove the directory we just created
# os.rmdir() only works on empty directories.
os.rmdir(folder_name)
print(f"Removed directory: '{folder_name}'")