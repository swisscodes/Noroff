"""Python `sys` Module: Best Practices, Common Functions, and Production Standards.

This module provides a comprehensive, hands-on reference for interacting with the
Python runtime environment using the standard `sys` module. It covers command-line
arguments, standard I/O streams, runtime parameters, system limits, memory inspection,
module resolution, and critical anti-patterns to avoid.
"""

from contextlib import redirect_stdout
import io
import sys
import traceback


# ==============================================================================
# BEST PRACTICE #0: CRITICAL NAMING RULE — NEVER NAME YOUR FILE `sys.py`
# ==============================================================================
# ANTI-PATTERN:
#   Saving your script as `sys.py`.
#
# WHY THIS IS DANGEROUS (Shadowing):
#   When a script or standard library module executes `import sys`, Python will
#   look in the current directory first if not strictly a built-in module, or
#   worse, interfere with the interpreter's internal module table.
#   Shadowing `sys.py` will break Python initialization, toolings (linters, IDEs),
#   and external libraries.
#
# RULE:
#   Never name your script after standard library modules (e.g., `sys.py`,
#   `os.py`, `json.py`, `random.py`, `typing.py`).
#   Use descriptive names like `system_lesson.py` or `sys_demo.py`.


# ==============================================================================
# BEST PRACTICE #1: Command Line Arguments (`sys.argv`)
# ==============================================================================
# - `sys.argv` is a list of strings passed to the Python script.
# - `sys.argv[0]` is ALWAYS the script name or invocation path.
# - `sys.argv[1:]` are the positional arguments provided by the user.
#
# ANTI-PATTERN:
#   filename = sys.argv[1]   # Crashes with IndexError if user provides no arguments!
#
# RECOMMENDED:
#   - Check `len(sys.argv)` before accessing indices directly.
#   - For anything beyond simple scripts, upgrade to `argparse` (standard library)
#     or modern CLI tools like `typer` or `click`.


def demo_command_line_arguments() -> None:
    """Demonstrates safe inspection of sys.argv."""
    print(f"[sys.argv] Full argument list: {sys.argv}")
    print(f"[sys.argv[0]] Executing script: {sys.argv[0]}")

    # Safe handling of user arguments with length verification
    if len(sys.argv) > 1:
        print(f"[sys.argv[1:]] User supplied arguments: {sys.argv[1:]}")
    else:
        print("[sys.argv] No additional CLI arguments provided (try running: python system_lesson.py arg1 arg2)")


# ==============================================================================
# BEST PRACTICE #2: Program Termination & Exit Codes (`sys.exit`)
# ==============================================================================
# - `sys.exit([arg])`: Exits the Python process cleanly.
#   - `sys.exit(0)` signals SUCCESS to the operating system / CI pipeline.
#   - `sys.exit(1)` or any non-zero integer signals an ERROR or failure.
#   - `sys.exit("Error message")` prints the message to `sys.stderr` and exits with code 1.
#
# UNDER THE HOOD:
#   `sys.exit()` raises a `SystemExit` exception. This allows `try...finally`
#   blocks and context managers to clean up open files, connections, and locks!
#
# ANTI-PATTERNS:
#   - Using `exit()` or `quit()` in production code. (These are interactive shell
#     helpers from the `site` module and may not exist if Python runs with -S).
#   - Using `os._exit()` for regular exits. (`os._exit` bypasses Python's cleanup
#     handlers, `finally` blocks, and stream flushes).


def demo_exit_and_status_codes() -> None:
    """Demonstrates sys.exit behavior and how SystemExit can be caught for cleanup."""
    print("[sys.exit] Demonstrating controlled exit and status codes:")

    try:
        print("  Attempting sys.exit(0)...")
        # In a real script, this would stop execution. Here we catch SystemExit
        # so the lesson continues executing subsequent sections.
        sys.exit(0)
    except SystemExit as exc:
        print(f"  ✓ Caught SystemExit with exit code: {exc.code} (Process cleanup executed!)")


# ==============================================================================
# BEST PRACTICE #3: Standard Streams (`sys.stdin`, `sys.stdout`, `sys.stderr`)
# ==============================================================================
# Python provides 3 standard file-like streams:
# - `sys.stdin`:  Standard input stream (for reading user/piped input).
# - `sys.stdout`: Standard output stream (where `print()` writes by default).
# - `sys.stderr`: Standard error stream (for error messages and diagnostic logs).
#
# BEST PRACTICES:
#   - Direct diagnostic/error messages to `sys.stderr` so they don't corrupt
#     clean data pipelines when piped into other programs (e.g., `python app.py | jq`).
#   - Use `sys.stdout.flush()` when printing progress without newlines to ensure
#     data is immediately rendered to the terminal buffer.


def demo_standard_streams() -> None:
    """Demonstrates direct writing, flushing, and separating stdout from stderr."""
    # 1. Writing directly to stdout (unlike print(), write() does not append a newline)
    sys.stdout.write("[sys.stdout] Direct write to standard output.\n")

    # 2. Writing diagnostic/error messages to stderr
    sys.stderr.write("[sys.stderr] Diagnostic / error message sent to standard error.\n")

    # Or using the built-in print function with file=sys.stderr:
    print("[sys.stderr] Convenient error logging via print(..., file=sys.stderr)", file=sys.stderr)

    # 3. Stream flushing (essential for real-time logs or progress indicators)
    sys.stdout.write("[sys.stdout] Buffering test... ")
    sys.stdout.flush()  # Forces the buffer to empty immediately to the console
    sys.stdout.write("Done!\n")

    # 4. Stream redirection in memory (safe capturing for unit tests)
    captured_buffer = io.StringIO()
    with redirect_stdout(captured_buffer):
        print("Captured output inside redirect_stdout context manager.")

    print(f"[Captured Output] Result: {captured_buffer.getvalue().strip()}")


# ==============================================================================
# BEST PRACTICE #4: Module Search Paths (`sys.path`)
# ==============================================================================
# - `sys.path` is a list of directory strings where Python looks for modules.
# - Index 0 (`sys.path[0]`) is the directory of the currently running script.
#
# ANTI-PATTERN:
#   Hardcoding arbitrary absolute paths with `sys.path.append("/path/to/my/project")`.
#   This makes code brittle, machine-dependent, and hard to test.
#
# RECOMMENDED:
#   - Use proper package layout with `pyproject.toml` and install in editable mode:
#     `pip install -e .`
#   - Use environment variable `PYTHONPATH` for development setups.
#   - If dynamic path insertion is unavoidable, calculate relative to `__file__`:
#     `sys.path.insert(0, str(Path(__file__).resolve().parent.parent))`


def demo_module_search_paths() -> None:
    """Demonstrates inspecting and understanding sys.path."""
    print(f"[sys.path[0]] Current script directory: {sys.path[0]}")
    print("[sys.path] First 4 search locations Python checks when importing:")
    for idx, path_entry in enumerate(sys.path[:4]):
        display_path = path_entry if path_entry else "'' (current working directory)"
        print(f"  {idx}: {display_path}")


# ==============================================================================
# BEST PRACTICE #5: Interpreter, Runtime Version & Platform Information
# ==============================================================================
# - `sys.version_info`: A structured named tuple containing (major, minor, micro, ...).
# - `sys.version`: A human-readable version string.
# - `sys.platform`: Operating system platform identifier ('linux', 'darwin', 'win32').
# - `sys.executable`: Absolute path to the running Python binary.
#
# ANTI-PATTERN:
#   if "3.10" in sys.version:   # Brittle string comparison!
#
# RECOMMENDED:
#   Use tuple comparison:
#   if sys.version_info >= (3, 10): ...


def demo_runtime_and_platform_info() -> None:
    """Demonstrates inspecting Python interpreter version and host platform."""
    # 1. Reliable version checking
    v = sys.version_info
    print(f"[sys.version_info] Running Python {v.major}.{v.minor}.{v.micro} (Release: {v.releaselevel})")

    # Enforcing minimum version check:
    MIN_VERSION = (3, 8)
    if sys.version_info < MIN_VERSION:
        raise RuntimeError(f"This application requires Python {MIN_VERSION[0]}.{MIN_VERSION[1]}+")
    print(f"  ✓ Python version meets requirement (>={MIN_VERSION[0]}.{MIN_VERSION[1]})")

    # 2. Platform identification
    print(f"[sys.platform] OS Platform identifier: {sys.platform}")
    if sys.platform == "linux":
        print("  -> Running on Linux")
    elif sys.platform == "darwin":
        print("  -> Running on macOS")
    elif sys.platform == "win32":
        print("  -> Running on Windows")

    # 3. Interpreter binary path (Crucial when spawning subprocesses!)
    print(f"[sys.executable] Python Interpreter Path: {sys.executable}")
    # BEST PRACTICE for subprocesses:
    # Use subprocess.run([sys.executable, "another_script.py"]) instead of "python"!
    # This guarantees the subprocess uses the EXACT SAME virtualenv/interpreter!


# ==============================================================================
# BEST PRACTICE #6: Memory Inspection with `sys.getsizeof()`
# ==============================================================================
# - `sys.getsizeof(object)`: Returns the memory footprint of an object in bytes.
#
# IMPORTANT CAVEAT (Shallow vs Deep Size):
#   `sys.getsizeof()` measures only the direct memory allocated for that object.
#   For containers (lists, dicts, sets), it returns the size of the container and
#   pointers, NOT the sizes of all referenced elements inside!


def demo_memory_inspection() -> None:
    """Demonstrates checking object memory consumption and generator efficiency."""
    int_size = sys.getsizeof(42)
    str_size = sys.getsizeof("Hello, World!")
    empty_list_size = sys.getsizeof([])
    empty_dict_size = sys.getsizeof({})

    print(f"[sys.getsizeof] Integer (42):        {int_size} bytes")
    print(f"[sys.getsizeof] String ('Hello...'): {str_size} bytes")
    print(f"[sys.getsizeof] Empty list:          {empty_list_size} bytes")
    print(f"[sys.getsizeof] Empty dict:          {empty_dict_size} bytes")

    # Comparing memory: List Comprehension vs Generator Expression
    n = 100_000
    list_comp = [x * 2 for x in range(n)]
    gen_exp = (x * 2 for x in range(n))

    print(f"\n[Memory Comparison for {n:,} items]:")
    print(f"  List comprehension: {sys.getsizeof(list_comp):,} bytes")
    print(f"  Generator expression: {sys.getsizeof(gen_exp):,} bytes  <-- Highly memory efficient!")


# ==============================================================================
# BEST PRACTICE #7: System Limits & Recursion Limits
# ==============================================================================
# - `sys.getrecursionlimit()`: Max depth of Python call stack (default is usually 1000).
# - `sys.setrecursionlimit(n)`: Changes the limit.
# - `sys.maxsize`: Largest integer supported by Python's `Py_ssize_t` type.
#   Indicates bitness: 2**31 - 1 on 32-bit platforms, 2**63 - 1 on 64-bit platforms.
#
# CAUTION:
#   Increasing recursion limit arbitrarily can lead to segmentation faults (OS
#   stack overflow), which crash Python without allowing exception handling.
#   Prefer iterative algorithms or data structures (like stacks) over deeply nested recursion.


def demo_system_limits() -> None:
    """Demonstrates inspecting recursion limits and integer maxsize."""
    current_rec_limit = sys.getrecursionlimit()
    print(f"[sys.getrecursionlimit] Max Call Stack Depth: {current_rec_limit}")

    # Bitness detection using sys.maxsize
    is_64_bit = sys.maxsize > 2**32
    arch = "64-bit" if is_64_bit else "32-bit"
    print(f"[sys.maxsize] Maximum index size: {sys.maxsize} ({arch} architecture)")

    # Byte order (Endianness)
    print(f"[sys.byteorder] System endianness: {sys.byteorder} (e.g. 'little' or 'big')")


# ==============================================================================
# BEST PRACTICE #8: Exception Inspection & Traceback (`sys.exc_info`)
# ==============================================================================
# - `sys.exc_info()`: Returns a 3-tuple `(type, value, traceback)` for the exception
#   currently being handled. If no exception is active, returns `(None, None, None)`.
# - `sys.excepthook`: A global function called for unhandled exceptions. You can
#   override this for global error logging or alert systems (e.g. Sentry/Bugsnag).


def demo_exception_inspection() -> None:
    """Demonstrates inspecting active exceptions and format tracebacks."""
    print("[sys.exc_info] Handling an intentional division by zero:")

    try:
        _ = 1 / 0 # type: ignore
    except ZeroDivisionError:
        exc_type, exc_value, exc_tb = sys.exc_info()
        print(f"  Exception Type:  {exc_type.__name__ if exc_type else 'None'}")
        print(f"  Exception Value: {exc_value}")
        if exc_tb:
            formatted_lines = traceback.format_tb(exc_tb)
            print(f"  Traceback Line:  {formatted_lines[-1].strip()}")


# ==============================================================================
# BEST PRACTICE #9: Loaded Modules & Cache (`sys.modules`)
# ==============================================================================
# - `sys.modules` is a dictionary mapping loaded module names to module objects.
# - When you execute `import foo`, Python checks `sys.modules` first. If present,
#   it returns the cached module immediately without re-reading from disk.
#
# USE CASES:
#   - Check if an optional module has already been imported.
#   - Clean introspection of loaded packages.


def demo_loaded_modules() -> None:
    """Demonstrates inspecting loaded modules and Python import caching."""
    print(f"[sys.modules] Total loaded modules in memory: {len(sys.modules)}")

    # Check for specific modules
    for mod_name in ("sys", "os", "math", "pytest"):
        is_loaded = mod_name in sys.modules
        print(f"  Module '{mod_name}' loaded? {is_loaded}")


# ==============================================================================
# BEST PRACTICE #10: Reference Counting & CPython Internals (`sys.getrefcount`)
# ==============================================================================
# - `sys.getrefcount(object)`: Returns the reference count of the object in CPython.
#
# NOTE:
#   The count is always 1 higher than expected because passing the object
#   as an argument to `sys.getrefcount()` creates a temporary reference!


def demo_reference_counting() -> None:
    """Demonstrates reference counting behavior in CPython."""
    my_object = ["sample", "data"]
    # 1 reference held by `my_object` + 1 temporary reference passed to getrefcount
    ref_count_initial = sys.getrefcount(my_object)
    print(f"[sys.getrefcount] Initial count: {ref_count_initial} (includes +1 from function call)")

    another_reference = my_object
    ref_count_second = sys.getrefcount(my_object)
    print(f"[sys.getrefcount] After second reference: {ref_count_second}")

    del another_reference
    print(f"[sys.getrefcount] After deleting reference: {sys.getrefcount(my_object)}")


# ==============================================================================
# SCRIPT EXECUTION ENTRY POINT
# ==============================================================================
if __name__ == "__main__":
    print("=" * 70)
    print("PYTHON `sys` MODULE: BEST PRACTICES & COMMON METHODS GUIDE")
    print("=" * 70)

    demo_command_line_arguments()
    print("-" * 70)

    demo_exit_and_status_codes()
    print("-" * 70)

    demo_standard_streams()
    print("-" * 70)

    demo_module_search_paths()
    print("-" * 70)

    demo_runtime_and_platform_info()
    print("-" * 70)

    demo_memory_inspection()
    print("-" * 70)

    demo_system_limits()
    print("-" * 70)

    demo_exception_inspection()
    print("-" * 70)

    demo_loaded_modules()
    print("-" * 70)

    demo_reference_counting()

    print("=" * 70)
    print("✓ All sys demonstrations completed successfully!")
    print("=" * 70)
