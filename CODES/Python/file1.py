"""Python File Handling & Writing: Best Practices and Modern Standards.

This module demonstrates the recommended, production-ready ways to write,
append, read, and manage files in Python, contrasting outdated habits with
modern Python (3.10+) standards.
"""

from pathlib import Path
import json


# ==============================================================================
# BEST PRACTICE #1: Always Use Context Managers (`with` statement)
# ==============================================================================
# ANTI-PATTERN:
#   f = open("example.txt", "w")
#   f.write("hello")
#   f.close()
# Problem: If an exception happens before f.close(), the file descriptor stays
# open, causing memory/file leaks and potential data corruption.
#
# RECOMMENDED:
# The `with` statement guarantees the file is automatically and safely closed,
# even if an unexpected error or crash occurs.


def demo_basic_write() -> None:
    """Demonstrates writing to a text file using a context manager."""
    file_path = "sample_output.txt"

    # 'w' mode: opens file for writing.
    # Note: 'w' will CREATE the file if it doesn't exist, or OVERWRITE/TRUNCATE it if it does.
    # Always specify encoding="utf-8" to avoid OS-dependent encoding bugs (e.g. Windows cp1252).
    with open(file_path, mode="w", encoding="utf-8") as f:
        f.write("Line 1: Hello from Python!\n")
        f.write("Line 2: Writing files the right way.\n")

    print(f"✓ Successfully wrote to '{file_path}' using standard context manager.")


# ==============================================================================
# BEST PRACTICE #2: Understand File Modes ('w', 'a', 'x', 'r')
# ==============================================================================
# - 'w' : Write (overwrites everything; creates file if missing)
# - 'a' : Append (adds content to the END of the file without deleting existing text)
# - 'x' : Exclusive creation (creates a new file; RAISES FileExistsError if it already exists)
# - 'r' : Read (default mode; raises FileNotFoundError if missing)
# - 'b' : Binary mode (append 'b' to any mode, e.g. 'wb', 'rb' for images, audio, bytes)


def demo_append_mode() -> None:
    """Demonstrates appending content to an existing file without deleting it."""
    file_path = "sample_output.txt"

    # 'a' mode: opens for appending at the end of the file
    with open(file_path, mode="a", encoding="utf-8") as f:
        f.write("Line 3: This line was appended later!\n")

    print(f"✓ Successfully appended new line to '{file_path}'.")


def demo_exclusive_creation() -> None:
    """Demonstrates safe creation to prevent accidental overwrites."""
    file_path = "unique_record.txt"

    # If the file already exists, 'x' mode raises FileExistsError
    try:
        with open(file_path, mode="x", encoding="utf-8") as f:
            f.write("Initial safe record created.\n")
        print(f"✓ Created new file '{file_path}' in exclusive mode.")
    except FileExistsError:
        print(f"ℹ File '{file_path}' already exists; skipped overwrite.")


# ==============================================================================
# BEST PRACTICE #3: Different Ways to Write Content
# ==============================================================================
def demo_writing_techniques() -> None:
    """Demonstrates write(), writelines(), and print(file=...)."""
    file_path = "techniques_demo.txt"

    lines = [
        "First item\n",
        "Second item\n",
        "Third item\n"
    ]

    with open(file_path, mode="w", encoding="utf-8") as f:
        # Technique A: .write() for single strings
        f.write("--- Header ---\n")

        # Technique B: .writelines() for a list/iterable of strings
        # Note: writelines() does NOT add newlines automatically; each string must end with \n
        f.writelines(lines)

        # Technique C: print(..., file=f)
        # Convenient because print() automatically adds newlines by default!
        print("Fourth item (via print)", file=f)
        print("Fifth item (via print)", file=f)

    print(f"✓ Demonstrated writing techniques in '{file_path}'.")


# ==============================================================================
# BEST PRACTICE #4: The Modern Python Standard — `pathlib.Path`
# ==============================================================================
# Why pathlib is preferred over os.path / raw strings:
# 1. Fully cross-platform: handles Windows (\\) and Unix (/) paths automatically.
# 2. Object-oriented and expressive methods (.exists(), .mkdir(), .read_text(), .write_text()).
# 3. Path building using the '/' division operator.


def demo_pathlib_operations() -> None:
    """Demonstrates the modern, recommended pathlib module."""
    # Define directory and file path relative to current script's folder
    current_dir = Path(__file__).resolve().parent
    output_dir = current_dir / "output_data"
    target_file = output_dir / "pathlib_example.txt"

    # Best Practice: Ensure parent directory exists before writing
    output_dir.mkdir(parents=True, exist_ok=True)

    # 1. Quick write (convenience method: automatically opens, writes, and closes)
    target_file.write_text("Written quickly with Path.write_text()!\n", encoding="utf-8")

    # 2. Pathlib with context manager for larger or streaming data
    with target_file.open(mode="a", encoding="utf-8") as f:
        f.write("Appended using target_file.open().\n")

    # 3. Quick read
    content = target_file.read_text(encoding="utf-8")
    print(f"✓ pathlib demonstrated. Content read back:\n{content.strip()}")


# ==============================================================================
# BEST PRACTICE #5: Writing Structured Data (JSON)
# ==============================================================================
# For dictionaries, lists, configurations, or complex data, use the `json` module.


def demo_json_write() -> None:
    """Demonstrates writing structured data cleanly as formatted JSON."""
    data = {
        "course": "Noroff Python Programming",
        "topic": "File Handling",
        "best_practices": [
            "Always use 'with open(...)'",
            "Always specify encoding='utf-8'",
            "Use pathlib for file paths",
            "Handle potential IO exceptions"
        ],
        "is_active": True,
        "version": 1.0
    }

    json_file = Path("course_info.json")

    with json_file.open(mode="w", encoding="utf-8") as f:
        # indent=4 creates human-readable, pretty-printed JSON
        json.dump(data, f, indent=4, ensure_ascii=False)

    print(f"✓ Wrote structured JSON configuration to '{json_file.name}'.")


# ==============================================================================
# BEST PRACTICE #6: Robust Error Handling (try...except)
# ==============================================================================
# File operations interact with the operating system and can fail due to:
# - FileNotFoundError: Reading a file that doesn't exist.
# - PermissionError: No write permissions for that folder/file.
# - IsADirectoryError: Trying to write to a path that is actually a directory.
# - OSError: Catch-all for OS-level input/output issues.


def demo_safe_file_reading(filepath: str | Path) -> None:
    """Demonstrates resilient file access with proper error handling."""
    path = Path(filepath)

    try:
        with path.open(mode="r", encoding="utf-8") as f:
            print(f"Reading '{path.name}':\n{f.read()}")
    except FileNotFoundError:
        print(f"⚠ Error: The file '{path}' does not exist.")
    except PermissionError:
        print(f"⚠ Error: Permission denied when accessing '{path}'.")
    except OSError as error:
        print(f"⚠ OS error encountered: {error}")


# ==============================================================================
# SCRIPT EXECUTION ENTRY POINT
# ==============================================================================
if __name__ == "__main__":
    print("=" * 60)
    print("PYTHON FILE WRITING & BEST PRACTICES DEMONSTRATION")
    print("=" * 60)

    # 1. Basic write
    demo_basic_write()

    # 2. Append mode
    demo_append_mode()

    # 3. Exclusive creation
    demo_exclusive_creation()

    # 4. Write techniques
    demo_writing_techniques()

    # 5. Modern pathlib
    demo_pathlib_operations()

    # 6. JSON structured data
    demo_json_write()

    # 7. Safe read with error handling (testing a non-existent file gracefully)
    print("\n--- Testing Error Handling with missing file ---")
    demo_safe_file_reading("alice.txt")

    print("\n" + "=" * 60)
    print("All file writing demonstrations completed successfully!")
    print("=" * 60)