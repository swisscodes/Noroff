"""Python `os` Module: Best Practices, Common Functions, and Production Standards.

This module provides a comprehensive, hands-on reference for working with the
operating system using Python's standard `os` module. It covers common functions,
file and directory operations, environment variables, system information, and
important anti-patterns to avoid.
"""

from datetime import datetime
import os
from pathlib import Path
import shutil
import subprocess
import sys


# ==============================================================================
# BEST PRACTICE #0: CRITICAL NAMING RULE — NEVER NAME YOUR FILE `os.py`
# ==============================================================================
# ANTI-PATTERN:
#   Saving your script as `os.py`.
#
# WHY THIS IS DANGEROUS (Shadowing):
#   When a script contains `import os`, Python checks the current working
#   directory first. If a file named `os.py` exists in your folder, Python
#   imports YOUR file instead of the built-in standard library module.
#   This causes `AttributeError: module 'os' has no attribute 'getcwd'` or
#   breaks external packages that rely on `os`.
#
# RULE:
#   Never name your scripts after standard library modules (e.g., `os.py`,
#   `random.py`, `json.py`, `sys.py`, `time.py`). Use descriptive names
#   such as `os_demo.py` or `os1.py`.


# ==============================================================================
# BEST PRACTICE #1: Current Working Directory & Safe Directory Changes
# ==============================================================================
# - os.getcwd(): Returns the absolute path of the Current Working Directory.
# - os.chdir(path): Changes the current process working directory.
#
# BEST PRACTICE:
# Always record the initial directory or use try...finally / context handlers
# if you must change directories, so your program returns to a known state.
# Even better: avoid changing cwd globally; use absolute paths instead!


def demo_current_working_directory() -> None:
    """Demonstrates inspecting and safely handling the working directory."""
    original_cwd = os.getcwd()
    print(f"[CWD] Current Working Directory: {original_cwd}")

    # Inspect file system metadata
    print(f"[OS] OS Name ('posix' for Linux/macOS, 'nt' for Windows): {os.name}")
    print(f"[OS] Path Separator for this system: {repr(os.sep)}")


# ==============================================================================
# BEST PRACTICE #2: Creating and Removing Directories
# ==============================================================================
# ANTI-PATTERN:
#   os.mkdir("nested/sub/folder")  -> Crashes if "nested" doesn't exist!
#   os.mkdir("folder")             -> Crashes if "folder" already exists!
#
# RECOMMENDED:
#   Use `os.makedirs(path, exist_ok=True)`.
#   - Creates intermediate parent directories automatically (like mkdir -p).
#   - Does NOT raise FileExistsError if the folder already exists.


def demo_directory_creation_and_removal() -> None:
    """Demonstrates resilient directory creation and clean removal."""
    base_dir = os.path.join(os.getcwd(), "demo_temp_sandbox")
    nested_dir = os.path.join(base_dir, "nested", "level2")

    # 1. Safe creation with exist_ok=True
    os.makedirs(nested_dir, exist_ok=True)
    print(f"✓ Created nested directories safely: {nested_dir}")

    # 2. Check existence
    if os.path.exists(nested_dir):
        print(f"✓ Verified existence using os.path.exists(): True")

    # 3. Removing directories:
    # - os.rmdir(path): Removes a single EMPTY directory.
    # - shutil.rmtree(path): Recursively removes a directory and all contents.
    shutil.rmtree(base_dir)
    print(f"✓ Cleaned up directory tree using shutil.rmtree('{base_dir}')")


# ==============================================================================
# BEST PRACTICE #3: Listing Directory Contents (`os.listdir` vs `os.scandir`)
# ==============================================================================
# - os.listdir(path): Returns a simple list of names (strings).
#   Drawback: To check if an item is a file or directory, you must make an
#   extra system call (os.path.isfile(os.path.join(path, name))).
#
# - os.scandir(path): [RECOMMENDED] Returns an iterator of `DirEntry` objects.
#   Advantage: Caches file attributes (size, is_dir, is_file, stat) on modern
#   OSes without extra syscalls, making it 2x-20x faster on large folders!


def demo_listing_directories() -> None:
    """Demonstrates os.listdir() vs the faster, modern os.scandir()."""
    cwd = os.getcwd()

    # Basic listing (names only)
    items = os.listdir(cwd)
    python_files = [f for f in items if f.endswith(".py")]
    print(f"[os.listdir] Found {len(python_files)} Python files in {cwd}")

    # High-performance listing with os.scandir()
    print("\n[os.scandir] Inspecting first 5 entries with DirEntry attributes:")
    with os.scandir(cwd) as entries:
        count = 0
        for entry in entries:
            if count >= 5:
                break
            entry_type = "DIR " if entry.is_dir() else "FILE"
            file_size = entry.stat().st_size if entry.is_file() else 0
            print(f"  [{entry_type}] {entry.name:<25} ({file_size} bytes)")
            count += 1


# ==============================================================================
# BEST PRACTICE #4: Traversing Directory Trees with `os.walk()`
# ==============================================================================
# `os.walk(top, topdown=True)` yields a 3-tuple: (current_root, dir_names, file_names).
# It recursively walks through an entire directory hierarchy.


def demo_os_walk() -> None:
    """Demonstrates recursive tree traversal with os.walk()."""
    target_dir = os.getcwd()
    total_py_files = 0
    total_size = 0

    print(f"[os.walk] Traversing directory tree from: {target_dir}")
    for root, dirs, files in os.walk(target_dir):
        # Ignore hidden directories like .git or __pycache__
        dirs[:] = [d for d in dirs if not d.startswith(".")]

        for filename in files:
            if filename.endswith(".py"):
                filepath = os.path.join(root, filename)
                try:
                    total_size += os.path.getsize(filepath)
                    total_py_files += 1
                except OSError:
                    continue

    print(f"✓ Found {total_py_files} total .py files ({total_size / 1024:.2f} KB)")


# ==============================================================================
# BEST PRACTICE #5: Path Manipulation with `os.path`
# ==============================================================================
# ANTI-PATTERN:
#   path = folder + "/" + filename   # Fails on Windows or with wrong slashes!
#
# RECOMMENDED:
#   Use `os.path.join()` or `pathlib.Path` for cross-platform compatibility.


def demo_os_path_utilities() -> None:
    """Demonstrates the most essential os.path helper functions."""
    sample_file = os.path.abspath(__file__)

    # 1. Safe Joining
    combined = os.path.join("home", "user", "documents", "data.csv")
    print(f"[os.path.join] Safe joined path: {combined}")

    # 2. Splitting path into directory and file
    dirname, basename = os.path.split(sample_file)
    print(f"[os.path.split] Directory: {dirname}")
    print(f"[os.path.split] Basename:  {basename}")

    # 3. Splitting filename and extension
    name_only, extension = os.path.splitext(basename)
    print(f"[os.path.splitext] Filename without ext: {name_only} | Extension: {extension}")

    # 4. Checking existence and types
    print(f"[os.path.exists] Exists?    {os.path.exists(sample_file)}")
    print(f"[os.path.isfile] Is file?   {os.path.isfile(sample_file)}")
    print(f"[os.path.isdir]  Is folder? {os.path.isdir(sample_file)}")

    # 5. File size and modification time
    size_in_bytes = os.path.getsize(sample_file)
    mtime = os.path.getmtime(sample_file)
    formatted_date = datetime.fromtimestamp(mtime).strftime("%Y-%m-%d %H:%M:%S")
    print(f"[os.path.getsize] Size: {size_in_bytes} bytes")
    print(f"[os.path.getmtime] Last modified: {formatted_date}")


# ==============================================================================
# BEST PRACTICE #6: File Operations (Renaming, Replacing, Removing)
# ==============================================================================
# - os.remove(file) / os.unlink(file): Deletes a file.
# - os.rename(src, dst): Renames a file. (Fails on Windows if dst exists!)
# - os.replace(src, dst): [RECOMMENDED] Atomically renames and overwrites dst
#   consistently across both POSIX (Linux/macOS) and Windows.


def demo_file_lifecycle() -> None:
    """Demonstrates creating, safely renaming/replacing, and deleting files."""
    temp_file_a = "temp_step1.txt"
    temp_file_b = "temp_step2.txt"

    # Create temporary file
    with open(temp_file_a, "w", encoding="utf-8") as f:
        f.write("Temporary content for OS demonstration.\n")
    print(f"✓ Created '{temp_file_a}'")

    # Atomic replace / rename
    os.replace(temp_file_a, temp_file_b)
    print(f"✓ Atomically renamed '{temp_file_a}' to '{temp_file_b}' using os.replace()")

    # Delete safely
    if os.path.exists(temp_file_b):
        os.remove(temp_file_b)
        print(f"✓ Removed '{temp_file_b}' using os.remove()")


# ==============================================================================
# BEST PRACTICE #7: Environment Variables (`os.environ` & `os.getenv`)
# ==============================================================================
# ANTI-PATTERN:
#   api_key = os.environ["API_KEY"]  -> Crashes with KeyError if variable missing!
#
# RECOMMENDED:
#   Use `os.getenv("KEY", default_value)` or `os.environ.get("KEY", default_value)`.


def demo_environment_variables() -> None:
    """Demonstrates safe access and modification of environment variables."""
    # 1. Read existing standard environment variables
    user = os.getenv("USER") or os.getenv("USERNAME", "Unknown User")
    home = os.getenv("HOME") or os.getenv("USERPROFILE", "Unknown Home")
    print(f"[os.getenv] Current User: {user}")
    print(f"[os.getenv] User Home:    {home}")

    # 2. Reading with default fallback
    custom_setting = os.getenv("APP_MODE", "development")
    print(f"[os.getenv] APP_MODE (with fallback): {custom_setting}")

    # 3. Setting an environment variable for the current process
    os.environ["DEMO_VARIABLE"] = "active_session_value"
    print(f"[os.environ] Set DEMO_VARIABLE: {os.environ.get('DEMO_VARIABLE')}")

    # 4. Clean up environment variable
    if "DEMO_VARIABLE" in os.environ:
        del os.environ["DEMO_VARIABLE"]
        print("✓ Successfully cleaned up DEMO_VARIABLE from os.environ.")


# ==============================================================================
# BEST PRACTICE #8: Process & System Information
# ==============================================================================
# Get system metadata, process IDs, and core counts.


def demo_system_and_process_info() -> None:
    """Demonstrates retrieving process ID, CPU count, and terminal info."""
    pid = os.getpid()
    parent_pid = os.getppid() if hasattr(os, "getppid") else "N/A"
    cpus = os.cpu_count()

    print(f"[Process] Process ID (PID):        {pid}")
    print(f"[Process] Parent Process ID (PPID): {parent_pid}")
    print(f"[Hardware] Logical CPU cores:      {cpus}")


# ==============================================================================
# BEST PRACTICE #9: Modern Alternative to `os.system()` -> Use `subprocess`
# ==============================================================================
# ANTI-PATTERN:
#   os.system("ls " + user_input)  # SECURITY RISK! Susceptible to command injection!
#   Also: os.system() does not capture output cleanly in Python variables.
#
# RECOMMENDED:
#   Use `subprocess.run(["command", "arg1", ...], check=True, capture_output=True)`


def demo_running_commands_safely() -> None:
    """Demonstrates running external commands safely via subprocess."""
    print("[Anti-Pattern] `os.system()` is legacy and insecure for user input.")
    print("[Recommended]  Use `subprocess.run()` with argument lists:")

    # Safe command execution:
    result = subprocess.run(
        [sys.executable, "--version"],
        capture_output=True,
        text=True,
        check=True
    )
    print(f"  ✓ Python interpreter version output: {result.stdout.strip()}")


# ==============================================================================
# BEST PRACTICE #10: Summary of `os.path` vs Modern `pathlib.Path`
# ==============================================================================
# Python 3.4+ introduced `pathlib`, which provides an object-oriented syntax:
#
# | Task                | Legacy `os` / `os.path`          | Modern `pathlib.Path`       |
# |---------------------|----------------------------------|-----------------------------|
# | Join paths          | os.path.join(a, b)               | a / b                       |
# | Get file name       | os.path.basename(path)           | path.name                   |
# | Get parent dir      | os.path.dirname(path)            | path.parent                 |
# | Check exists        | os.path.exists(path)             | path.exists()               |
# | Make directory      | os.makedirs(path, exist_ok=True) | path.mkdir(parents=True, ..)|
# | Read text file      | with open(path) as f: f.read()   | path.read_text()            |


def demo_pathlib_comparison() -> None:
    """Compares os.path with pathlib for modern Python development."""
    current_file = Path(__file__).resolve()

    print(f"[pathlib] Path object:  {current_file}")
    print(f"[pathlib] File name:    {current_file.name}")
    print(f"[pathlib] File stem:    {current_file.stem}")
    print(f"[pathlib] Suffix:       {current_file.suffix}")
    print(f"[pathlib] Parent dir:   {current_file.parent}")
    print(f"[pathlib] File exists:  {current_file.exists()}")


# ==============================================================================
# SCRIPT EXECUTION ENTRY POINT
# ==============================================================================
if __name__ == "__main__":
    print("=" * 70)
    print("PYTHON `os` MODULE: BEST PRACTICES & COMMON METHODS GUIDE")
    print("=" * 70)

    demo_current_working_directory()
    print("-" * 70)

    demo_directory_creation_and_removal()
    print("-" * 70)

    demo_listing_directories()
    print("-" * 70)

    demo_os_walk()
    print("-" * 70)

    demo_os_path_utilities()
    print("-" * 70)

    demo_file_lifecycle()
    print("-" * 70)

    demo_environment_variables()
    print("-" * 70)

    demo_system_and_process_info()
    print("-" * 70)

    demo_running_commands_safely()
    print("-" * 70)

    demo_pathlib_comparison()

    print("=" * 70)
    print("✓ All demonstrations completed successfully!")
    print("=" * 70)
