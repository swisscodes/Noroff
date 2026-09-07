numbers = [64, 34, 25, 12, 22, 11, 90]
n = len(numbers)

for i in range(n):
    swapped = False
    
    for j in range((n - i) - 1):
        if numbers[j] > numbers[j + 1]:
            # Idiomatic Python tuple swap (no temporary variables needed)
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
            swapped = True
            
    # Early exit: if no swaps happened, the list is already sorted
    if not swapped:
        break

print(numbers)