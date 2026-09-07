def split_array(numbers: list[int]) -> tuple[list[int], list[int]]:
    midpoint = len(numbers) // 2
    return numbers[:midpoint], numbers[midpoint:]

def merge_arrays(arrA: list[int], arrB: list[int]) -> list[int]:
    merged: list[int] = []
    i = 0
    j = 0

    while i < len(arrA) and j < len(arrB):
        if arrA[i] <= arrB[j]:
            merged.append(arrA[i])
            i += 1
        else:
            merged.append(arrB[j])
            j += 1

    # Append remaining elements from both arrays
    merged.extend(arrA[i:])
    merged.extend(arrB[j:])
    return merged

def merge_sort(numbers: list[int]) -> list[int]:
    if len(numbers) <= 1:
        return numbers

    arrA, arrB = split_array(numbers)
    arrA = merge_sort(arrA)
    arrB = merge_sort(arrB)

    return merge_arrays(arrA, arrB)

# Test
numbers: list[int] = [64, 34, 25, 12, 22, 11, 90]
sorted_numbers: list[int] = merge_sort(numbers)
print(sorted_numbers)
