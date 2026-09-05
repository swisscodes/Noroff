path = r"C:\\Program Files\My Games\The Game\saved games\lost"
print( path )

# ==========================================
# MODERN PYTHON GUIDE: ESCAPE CHARACTERS & PATHS
# ==========================================

# 1. Common Escape Sequences
print("\n--- Common Escape Characters ---")
print("1. Newline: Line 1\nLine 2")
print("2. Tab indentation:\tColumn A\tColumn B")
print("3. Quotes inside string: \"Python\" is great, or 'Single quotes'")
print("4. Backslash itself: C:\\Users\\Name")

# 2. Why Raw Strings (r"...") Matter
# Without 'r', '\U' or '\t' in a Windows path is interpreted as an escape code:
# e.g., "C:\test\new" -> '\t' becomes a tab, '\n' becomes a newline!
raw_example = r"C:\test\new_folder\saved"
print(f"\nRaw string output: {raw_example}")

# 3. Modern Best Practice: 'pathlib.Path' (Standard since Python 3.4)
# Instead of managing raw strings and OS slash directions manually, use pathlib:
from pathlib import Path

save_dir = Path("C:/Program Files") / "My Games" / "The Game" / "saved games"
print(f"\nModern pathlib object: {save_dir}")
print(f"Directory name: {save_dir.name}")
print(f"Parent directory: {save_dir.parent}")