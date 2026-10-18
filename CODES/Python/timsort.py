"""
===============================================================================
TIMSORT ALGORITHM IMPLEMENTATION
===============================================================================
TimSort is a hybrid, stable sorting algorithm derived from Merge Sort and
Insertion Sort. It was designed by Tim Peters in 2002 for use in Python
(powering Python's built-in sorted() and list.sort()).

How TimSort works:
1. Divide the array into small chunks called "runs" (typically of size 32 or 64).
2. Sort each small run using Insertion Sort (which is exceptionally fast on
   small arrays).
3. Repeatedly merge the sorted runs together using a Merge procedure (similar
   to Merge Sort) until the entire list is fully sorted.

Time Complexity:
- Best Case:    O(n)        (when the array is already mostly sorted)
- Average Case: O(n log n)
- Worst Case:   O(n log n)

Space Complexity:
- O(n) auxiliary space for merging
===============================================================================
"""

MIN_RUN: int = 32


def calc_min_run(n: int) -> int:
    """
    Calculates the minimum run length for TimSort.
    Keeps the value in [32, 64] such that N / min_run is close to,
    or slightly less than, a power of 2.
    """
    r: int = 0
    while n >= MIN_RUN:
        r |= n & 1
        n >>= 1
    return n + r


def insertion_sort(arr: list[int], left: int, right: int) -> None:
    """
    Sorts a subarray arr[left..right] in-place using Insertion Sort.
    Insertion Sort is optimal for small slices of data.
    """
    for i in range(left + 1, right + 1):
        key: int = arr[i]
        j: int = i - 1

        # Move elements of arr[left..i-1] that are greater than key
        # to one position ahead of their current position
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def merge(arr: list[int], left: int, mid: int, right: int) -> None:
    """
    Merges two adjacent sorted subarrays:
    - Left run:  arr[left..mid]
    - Right run: arr[mid+1..right]
    """
    # Create temporary copies of the left and right runs
    len1: int = mid - left + 1
    len2: int = right - mid

    left_part: list[int] = arr[left : left + len1]
    right_part: list[int] = arr[mid + 1 : mid + 1 + len2]

    i: int = 0  # Initial index for left_part
    j: int = 0  # Initial index for right_part
    k: int = left  # Initial index for merged subarray in arr

    # Merge elements in sorted order
    while i < len1 and j < len2:
        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1
        k += 1

    # Copy remaining elements of left_part, if any
    while i < len1:
        arr[k] = left_part[i]
        i += 1
        k += 1

    # Copy remaining elements of right_part, if any
    while j < len2:
        arr[k] = right_part[j]
        j += 1
        k += 1


def timsort(arr: list[int]) -> list[int]:
    """
    Sorts the given list of integers using the TimSort algorithm.
    Sorts in-place and returns the sorted list.
    """
    n: int = len(arr)
    if n <= 1:
        return arr

    min_run: int = calc_min_run(n)

    # Step 1: Sort individual subarrays of size min_run using Insertion Sort
    for start in range(0, n, min_run):
        end: int = min(start + min_run - 1, n - 1)
        insertion_sort(arr, start, end)

    # Step 2: Merge sorted runs. Start merging from size min_run,
    # then double the size (size *= 2) each iteration.
    size: int = min_run
    while size < n:
        for left in range(0, n, 2 * size):
            mid: int = min(n - 1, left + size - 1)
            right: int = min(left + 2 * size - 1, n - 1)

            # Only merge if mid < right (i.e. there is a right run to merge)
            if mid < right:
                merge(arr, left, mid, right)

        size *= 2

    return arr


# =============================================================================
# TEST & DEMONSTRATION
# =============================================================================
if __name__ == "__main__":
    import random

    # Test 1: Small array (smaller than MIN_RUN)
    sample_array: list[int] = [64, 34, 25, 12, 22, 11, 90]
    print("Original small array: ", sample_array)
    sorted_sample: list[int] = timsort(sample_array)
    print("Sorted small array:   ", sorted_sample)

    # Test 2: Large array (triggers both insertion sort runs and merging)
    large_array: list[int] = [random.randint(1, 1000) for _ in range(100)]
    expected_sorted: list[int] = sorted(large_array)
    timsorted_array: list[int] = timsort(large_array)

    print("\nLarge array test (100 elements):")
    print(f"Matches Python's built-in sorted(): {timsorted_array == expected_sorted}")
    print(f"First 10 sorted elements: {timsorted_array[:10]}")
    print(f"Last 10 sorted elements:  {timsorted_array[-10:]}")
