print("Hello From VS Code!")

# ==========================================
# MODERN PYTHON GUIDE: SCRIPT ENTRYPOINTS & ENVIRONMENT
# ==========================================

# 1. The Standard Main Idiom: `if __name__ == "__main__":`
# When a script is executed directly from the terminal, Python sets `__name__` to "__main__".
# If the file is imported by another file, `__name__` is set to the module name.
# Wrapping script execution inside this check prevents unwanted code execution on import.

import sys
import platform

def main() -> None:
    print("\n--- Python Environment Diagnostics ---")
    print(f"Python Version: {sys.version.split()[0]} on {platform.system()} ({platform.machine()})")
    print("Execution mode: Top-level standalone script")

if __name__ == "__main__":
    main()