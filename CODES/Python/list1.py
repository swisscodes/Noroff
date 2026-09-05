# Creating a list using square brackets
my_list = [1, 2, 3, "four", 5.0] # type:ignore
# Creating a list using the list() function
another_list = list("hello")
# This creates a list of individual characters: ['h', 'e', 'l', 'l', 'o']


# List of useful methods for lists:
# list.append(item) - Adds an item to the end of the list.
# list.extend(iterable) - Extends the list by appending elements from the iterable.
# list.insert(index, item) - Inserts an item at a given position.
# list.remove(item) - Removes the first occurrence of an item from the list.
# list.pop([index]) - Removes and returns the item at the given position in the list. If no index is specified, removes and returns the last item in the list.
# list.clear() - Removes all items from the list.
# list.index(item) - Returns the index of the first occurrence of an item in the list.
# list.count(item) - Returns the number of occurrences of an item in the list.
# list.sort(key=None, reverse=False) - Sorts the        items of the list in place (the arguments can be used for custom sorting).

listB: list[str] = []
listB.append("hello")
listB.append("world")
print( *listB )
print(",".join(listB))


listC = [0,1,2,3,4]
listC.insert(2,99)
print( listC )

listD = [0,1,2,3,4]
print( listD.pop(1) )
print( listD )




listE = list("hello world")
listE.remove('l')
print( listE )


# for string we can use replace to remove characters globally
# Python's str.replace() accepts an optional third argument called count:
text = "hello world"
clean_text = text.replace("l", "")
print(clean_text)  # "heo word"

result = text.replace("l", "X", 1)

print(result)


listF = list("hello world")
print( 'o' in listF )
print( 'x' not in listF )

text = "hello world"

print("o" in text)      # True
print("x" not in text)  # True



# Task,                             JavaScript,                     Python
# Substring check,              str.includes("world")            "world" in str"
# Substring NOT present,        !str.includes("x")               "x" not in str"
# Starts with,                  "str.startsWith("he")            str.startswith("he")
# Ends with,                    "str.endsWith("ld")              str.endswith("ld")


# String in Is Actually More Powerful Than List in
# When you use in on a list, it only checks for exact individual elements:

# ==========================================
# MODERN PYTHON GUIDE: ADVANCED LIST PATTERNS
# ==========================================

# 1. List Comprehensions (Modern standard for mapping and filtering)
raw_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Filter even numbers and square them in a single expressive line:
even_squares = [n ** 2 for n in raw_numbers if n % 2 == 0]
print(f"\nEven squares (List Comprehension): {even_squares}")

# 2. Sorting: In-place .sort() vs sorted()
# .sort() mutates the original list in-place (returns None)
# sorted() returns a BRAND NEW sorted list (original stays unchanged)
scores = [88, 42, 95, 70, 60]
sorted_descending = sorted(scores, reverse=True)
print(f"Original scores: {scores}")
print(f"New sorted list (descending): {sorted_descending}")

# Sorting by custom key:
words = ["banana", "pie", "apple", "watermelon"]
words.sort(key=len)  # Sort in-place by string length
print(f"Sorted by word length: {words}")

# 3. Performance Warning: list.pop(0) vs collections.deque
# list.pop(0) has to shift every single element to the left (O(N) time complexity).
# For fast queues (FIFO), use collections.deque (O(1) constant time):
from collections import deque
queue = deque(["task1", "task2", "task3"])
queue.append("task4")
first_out = queue.popleft()  # Lightning fast O(1)
print(f"Deque processed '{first_out}', remaining queue: {list(queue)}")