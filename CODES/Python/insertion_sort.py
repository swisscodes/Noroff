# insertion sort 
"""
get the array of numbers from the user
sort the array using insertion sort algorithm

"""

myarray: list[int] = [64, 34, 25, 12, 22, 11, 90]

def insertion_sort(arr: list[int]) -> list[int]:
    for i in range(1, len(arr)):
        key: int = arr[i]
        j: int = i - 1
        
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Test
sorted_array: list[int] = insertion_sort(myarray)
print(sorted_array)