"""Python `shutil` Module: Best Practices, Common Functions, and Shell Utilities.

This module provides a comprehensive, hands-on reference for high-level file and
directory operations using Python's standard `shutil` (shell utilities) module.
It covers copying files and directories, recursive deletion, moving items across
filesystems, locating system binaries, inspecting disk space, creating/extracting
archives, and production anti-patterns.
"""

from datetime import datetime
import os
from pathlib import Path
import shutil
import stat
import sys


# ==============================================================================
# BEST PRACTICE #0: CRITICAL NAMING RULE — NEVER NAME YOUR FILE `shutil.py`
# ==============================================================================
# ANTI-PATTERN:
#   Saving your script as `shutil.py`.
#
# WHY THIS IS DANGEROUS (Shadowing):
#   When Python executes `import shutil`, it searches the current directory first.
#   Naming your file `shutil.py` masks the standard library module, breaking
#   any module or package that depends on it and throwing errors like
#   `AttributeError: module 'shutil' has no attribute 'copyfile'`.
#
# RULE:
#   Never name your script after standard library modules (e.g., `shutil.py`,
#   `os.py`, `sys.py`, `tarfile.py`, `zipfile.py`).
#   Use descriptive names such as `shell_utils.py` or `shutil_demo.py`.


# ==============================================================================
# BEST PRACTICE #1: Copying Files (`copyfile` vs `copy` vs `copy2`)
# ==============================================================================
# Python's `shutil` has three primary file copy functions. Choosing the right one
# is critical depending on whether you need metadata, speed, or directory destinations:
#
# 1. `shutil.copyfile(src, dst)`:
#    - Copies ONLY file contents.
#    - Fastest, does NOT preserve permissions, flags, or timestamps.
#    - `dst` MUST be the full destination filename (cannot be a directory path).
#
# 2. `shutil.copy(src, dst)`:
#    - Copies contents AND file permissions (`chmod` bits / execution flags).
#    - Does NOT preserve file creation/modification timestamps.
#    - `dst` can be a directory name (preserves source filename).
#
# 3. `shutil.copy2(src, dst)`: [PRODUCTION RECOMMENDED]
#    - Copies contents, permissions, AND full metadata (timestamps, flags).
#    - Essentially the equivalent of `cp -p` on Linux/macOS.
#    - Ideal for backup scripts, synchronizers, and archival pipelines.


def demo_file_copying(sandbox_dir: Path) -> None:
    """Demonstrates copyfile, copy, and copy2, comparing metadata preservation."""
    source_file = sandbox_dir / "source_document.txt"
    source_file.write_text("Hello from shutil lesson: original content.\n", encoding="utf-8")

    # Destination paths
    dst_copyfile = sandbox_dir / "copyfile_output.txt"
    dst_copy = sandbox_dir / "copy_output.txt"
    dst_copy2 = sandbox_dir / "copy2_output.txt"

    # 1. copyfile (content only)
    shutil.copyfile(source_file, dst_copyfile)

    # 2. copy (content + permission bits)
    shutil.copy(source_file, dst_copy)

    # 3. copy2 (content + permissions + modification timestamps)
    shutil.copy2(source_file, dst_copy2)

    print("[shutil.copy2 vs copy vs copyfile]:")
    print(f"  Source file mtime:   {datetime.fromtimestamp(source_file.stat().st_mtime)}")
    print(f"  copyfile dst mtime:  {datetime.fromtimestamp(dst_copyfile.stat().st_mtime)}")
    print(f"  copy dst mtime:      {datetime.fromtimestamp(dst_copy.stat().st_mtime)}")
    print(f"  copy2 dst mtime:     {datetime.fromtimestamp(dst_copy2.stat().st_mtime)} (Preserved!)")


# ==============================================================================
# BEST PRACTICE #2: Copying Directory Trees (`shutil.copytree`)
# ==============================================================================
# - Recursively copies an entire directory tree to a destination directory.
#
# KEY PARAMETERS & MODERN BEST PRACTICES:
#   - `dirs_exist_ok=True` (Python 3.8+):
#     By default, copytree raises `FileExistsError` if the destination folder
#     already exists. Setting `dirs_exist_ok=True` behaves like `cp -R`, merging
#     files into the existing directory.
#   - `ignore=shutil.ignore_patterns(...)`:
#     Callable filter to exclude specific patterns (e.g. `*.pyc`, `__pycache__`, `.git`).
#   - `copy_function=shutil.copy2`:
#     Default is `copy2`, which preserves metadata across all copied files.


def demo_directory_copying(sandbox_dir: Path) -> None:
    """Demonstrates copying directory trees with filtering and dirs_exist_ok."""
    source_tree = sandbox_dir / "project_src"
    source_tree.mkdir(parents=True, exist_ok=True)
    (source_tree / "main.py").write_text("print('Main')", encoding="utf-8")
    (source_tree / "debug.log").write_text("DEBUG LOGS", encoding="utf-8")
    (source_tree / "temp.cache").write_text("CACHE DATA", encoding="utf-8")

    dst_tree = sandbox_dir / "project_backup"

    # Copy tree ignoring logs and cache files
    shutil.copytree(
        source_tree,
        dst_tree,
        dirs_exist_ok=True,
        ignore=shutil.ignore_patterns("*.log", "*.cache")
    )

    copied_files = [p.name for p in dst_tree.iterdir()]
    print("[shutil.copytree] Directory tree copied successfully:")
    print(f"  Source items: {[p.name for p in source_tree.iterdir()]}")
    print(f"  Copied items (excluding *.log, *.cache): {copied_files}")


# ==============================================================================
# BEST PRACTICE #3: Recursive Directory Deletion (`shutil.rmtree`)
# ==============================================================================
# - `shutil.rmtree(path)` removes an entire directory tree (like `rm -rf`).
#
# ANTI-PATTERNS:
#   - Using `os.rmdir()` on folders that contain files -> Crashes with `OSError`!
#   - Calling `shutil.rmtree("")` or unvalidated paths without checking safety.
#
# ROBUST ERROR HANDLING (Handling Read-Only / Permission Errors):
#   On Windows or restricted environments, read-only files cause `rmtree` to fail.
#   We can supply an error handler callback to clear the read-only bit and retry.


def demo_recursive_removal(sandbox_dir: Path) -> None:
    """Demonstrates safe recursive directory tree removal with error handling."""
    folder_to_delete = sandbox_dir / "to_be_deleted"
    folder_to_delete.mkdir(parents=True, exist_ok=True)
    nested_file = folder_to_delete / "inner_file.txt"
    nested_file.write_text("To be deleted", encoding="utf-8")

    def handle_remove_readonly(func, path, exc_info):
        """Clear read-only attribute on permission errors and retry removal."""
        try:
            os.chmod(path, stat.S_IWRITE)
            func(path)
        except Exception as e:
            print(f"  Failed to delete {path}: {e}", file=sys.stderr)

    if folder_to_delete.exists():
        # Python 3.12+ supports `onexc`, while `onerror` is supported in earlier versions
        if sys.version_info >= (3, 12):
            def on_exc_handler(func, path, exc):
                handle_remove_readonly(func, path, None)
            shutil.rmtree(folder_to_delete, onexc=on_exc_handler)
        else:
            shutil.rmtree(folder_to_delete, onerror=handle_remove_readonly)

        print(f"[shutil.rmtree] Successfully removed directory tree: {folder_to_delete.name}")


# ==============================================================================
# BEST PRACTICE #4: Moving Files & Folders (`shutil.move`)
# ==============================================================================
# - `shutil.move(src, dst)`: High-level move (like `mv`).
#
# WHY `shutil.move` INSTEAD OF `os.rename` / `os.replace`?
#   - `os.rename()` and `os.replace()` FAIL with `EXDEV: Invalid cross-device link`
#     if source and destination are on different filesystem mount points / partitions!
#   - `shutil.move()` automatically falls back to copy2 + unlink across filesystems,
#     making it truly universal and safe across disks or external drives.


def demo_moving_files(sandbox_dir: Path) -> None:
    """Demonstrates moving files and directories safely across filesystems."""
    staging_file = sandbox_dir / "staging.csv"
    staging_file.write_text("id,name\n1,Alpha\n", encoding="utf-8")

    processed_dir = sandbox_dir / "processed_data"
    processed_dir.mkdir(exist_ok=True)

    destination_file = processed_dir / "archive.csv"

    # shutil.move handles both file renames and relocation to directories
    shutil.move(str(staging_file), str(destination_file))

    print(f"[shutil.move] Moved '{staging_file.name}' -> '{destination_file.relative_to(sandbox_dir)}'")
    print(f"  Destination file exists: {destination_file.exists()}")


# ==============================================================================
# BEST PRACTICE #5: Locating System Binaries (`shutil.which`)
# ==============================================================================
# - `shutil.which(cmd)`: Returns the path to an executable which would run if
#   given command was called, or `None` if not found on the system `PATH`.
# - Standard library replacement for the UNIX `which` or Windows `where` commands.
#
# PRODUCTION USE CASE:
#   Always verify external tool dependencies (e.g. `git`, `docker`, `ffmpeg`)
#   before spawning `subprocess.run()`.


def demo_locating_executables() -> None:
    """Demonstrates checking if required CLI tools exist on the host machine."""
    tools_to_check = ["python3", "git", "docker", "ffmpeg", "non_existent_binary_xyz"]

    print("[shutil.which] Inspecting executable availability in system PATH:")
    for tool in tools_to_check:
        location = shutil.which(tool)
        status = f"FOUND at {location}" if location else "NOT FOUND"
        print(f"  {tool:<26} -> {status}")


# ==============================================================================
# BEST PRACTICE #6: Inspecting Disk Usage (`shutil.disk_usage`)
# ==============================================================================
# - `shutil.disk_usage(path)`: Returns a named tuple `(total, used, free)` in bytes
#   for the filesystem containing the specified path.
#
# PRODUCTION USE CASE:
#   Pre-flight checks in data processing or ingestion pipelines to prevent
#   filling up server disks or crashing due to `ENOSPC: No space left on device`.


def demo_disk_space_inspection() -> None:
    """Demonstrates measuring total, used, and free disk space."""
    target_path = Path.cwd()
    usage = shutil.disk_usage(target_path)

    to_gb = 1024 ** 3
    total_gb = usage.total / to_gb
    used_gb = usage.used / to_gb
    free_gb = usage.free / to_gb
    percent_used = (usage.used / usage.total) * 100

    print(f"[shutil.disk_usage] Filesystem containing '{target_path}':")
    print(f"  Total Space: {total_gb:.2f} GB")
    print(f"  Used Space:  {used_gb:.2f} GB ({percent_used:.1f}%)")
    print(f"  Free Space:  {free_gb:.2f} GB")


# ==============================================================================
# BEST PRACTICE #7: Creating & Extracting Archives (`make_archive` & `unpack_archive`)
# ==============================================================================
# Python's `shutil` provides high-level archive utilities so you don't have to
# write boilerplate code with `zipfile` or `tarfile`.
#
# Supported formats include: 'zip', 'tar', 'gztar', 'bztar', 'xztar'.
#
# SECURITY WARNING (Archive Extraction / Zip Slip):
#   Never unpack untrusted archives from third parties without validating member
#   paths (Python 3.12+ introduced `filter='data'` to protect against path traversal).


def demo_archives(sandbox_dir: Path) -> None:
    """Demonstrates creating and extracting ZIP and TAR archives."""
    # 1. Inspect supported archive and unpack formats
    archive_formats = [fmt[0] for fmt in shutil.get_archive_formats()]
    print(f"[shutil.get_archive_formats] Supported: {archive_formats}")

    # 2. Prepare files to archive
    content_folder = sandbox_dir / "docs_to_archive"
    content_folder.mkdir(exist_ok=True)
    (content_folder / "readme.txt").write_text("Project Documentation", encoding="utf-8")
    (content_folder / "data.json").write_text('{"status": "ok"}', encoding="utf-8")

    # 3. Create zip archive
    archive_base = sandbox_dir / "project_release"
    created_archive = shutil.make_archive(
        base_name=str(archive_base),
        format="zip",
        root_dir=str(content_folder)
    )
    print(f"[shutil.make_archive] Created archive: {Path(created_archive).name}")

    # 4. Extract archive
    extraction_target = sandbox_dir / "extracted_docs"
    extraction_target.mkdir(exist_ok=True)
    shutil.unpack_archive(created_archive, extract_dir=str(extraction_target))

    extracted_items = [p.name for p in extraction_target.iterdir()]
    print(f"[shutil.unpack_archive] Extracted files: {extracted_items}")


# ==============================================================================
# BEST PRACTICE #8: Terminal Dimensions (`shutil.get_terminal_size`)
# ==============================================================================
# - `shutil.get_terminal_size(fallback=(columns, lines))`:
#   Returns the active terminal window size as `os.terminal_size(columns, lines)`.
#
# BEST PRACTICE:
#   Use this to dynamically format CLI dividers, progress bars, and column layouts.
#   Always provide a sensible fallback (e.g. 80 columns) for non-interactive
#   environments like Docker containers, CI/CD runners, or redirected logs.


def demo_terminal_size() -> None:
    """Demonstrates dynamic terminal layout adaptation."""
    size = shutil.get_terminal_size(fallback=(80, 24))
    print(f"[shutil.get_terminal_size] Width: {size.columns} cols, Height: {size.lines} rows")

    # Adapt divider line width dynamically to the user's terminal
    divider = "~" * min(size.columns, 70)
    print(f"Dynamic separator line:\n{divider}")


# ==============================================================================
# BEST PRACTICE #9: Low-Level Stream Copying (`shutil.copyfileobj`)
# ==============================================================================
# - `shutil.copyfileobj(fsrc, fdst, length=...)`:
#   Copies data between two open file-like objects using buffered chunks.
#
# BEST PRACTICE:
#   Ideal for streaming large network responses, in-memory buffers, or
#   decompression streams directly to a file without loading entire data into RAM.


def demo_copyfileobj(sandbox_dir: Path) -> None:
    """Demonstrates stream-to-stream buffered copying for memory efficiency."""
    src_path = sandbox_dir / "large_stream_source.txt"
    dst_path = sandbox_dir / "stream_dest.txt"

    # Create dummy source data
    with open(src_path, "w", encoding="utf-8") as f_src:
        for i in range(1000):
            f_src.write(f"Stream line record #{i}\n")

    # Copy using 64 KB buffer chunks
    with open(src_path, "rb") as f_in, open(dst_path, "wb") as f_out:
        shutil.copyfileobj(f_in, f_out, length=64 * 1024)

    print(f"[shutil.copyfileobj] Stream copied {dst_path.stat().st_size} bytes in chunks.")


# ==============================================================================
# BEST PRACTICE #10: Summary Comparison (`os` vs `pathlib` vs `shutil`)
# ==============================================================================
# | Operation                 | `os` Module                 | `pathlib.Path`            | `shutil` Module            |
# |---------------------------|-----------------------------|---------------------------|----------------------------|
# | Copy file content + meta  | N/A (low-level read/write)  | N/A                       | `shutil.copy2(src, dst)`   |
# | Copy entire folder tree   | N/A (requires manual loop)  | N/A                       | `shutil.copytree(src, dst)`|
# | Remove non-empty folder   | N/A (`os.rmdir` fails)      | N/A (`Path.rmdir` fails)  | `shutil.rmtree(path)`      |
# | Move across filesystems   | `os.replace` (fails EXDEV)  | `Path.rename` (fails EXDEV)| `shutil.move(src, dst)`   |
# | Find CLI executable       | Manual PATH loop            | N/A                       | `shutil.which(cmd)`        |
# | Check disk free space     | `os.statvfs` (POSIX only)   | N/A                       | `shutil.disk_usage(path)`  |
# | Create ZIP/TAR archive    | N/A                         | N/A                       | `shutil.make_archive(...)` |


# ==============================================================================
# SCRIPT EXECUTION ENTRY POINT
# ==============================================================================
if __name__ == "__main__":
    print("=" * 70)
    print("PYTHON `shutil` MODULE: BEST PRACTICES & COMMON METHODS GUIDE")
    print("=" * 70)

    # Prepare an isolated temporary sandbox for hands-on demonstration
    sandbox = Path.cwd() / "demo_shutil_sandbox"
    sandbox.mkdir(exist_ok=True)

    try:
        demo_file_copying(sandbox)
        print("-" * 70)

        demo_directory_copying(sandbox)
        print("-" * 70)

        demo_recursive_removal(sandbox)
        print("-" * 70)

        demo_moving_files(sandbox)
        print("-" * 70)

        demo_locating_executables()
        print("-" * 70)

        demo_disk_space_inspection()
        print("-" * 70)

        demo_archives(sandbox)
        print("-" * 70)

        demo_terminal_size()
        print("-" * 70)

        demo_copyfileobj(sandbox)

    finally:
        # Guarantee clean sandbox teardown after demonstrations
        if sandbox.exists():
            shutil.rmtree(sandbox, ignore_errors=True)
            print("-" * 70)
            print("✓ Cleaned up temporary sandbox directory.")

    print("=" * 70)
    print("✓ All shutil demonstrations completed successfully!")
    print("=" * 70)
