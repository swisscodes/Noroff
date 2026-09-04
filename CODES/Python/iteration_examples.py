students = ["Alice", "Bob", "Charlie", "David", "Eve"]

for student in students:
    print(f"Hello, {student}!")


for student in range(len(students)):
    print("range starts here")
    print(f"Hello, {students[student]}!")

items = ["apple", "banana", "cherry"]
prices = [1.50, 0.75, 2.00]

# Find the maximum character length across all items
the_length = max(len(item) for item in items)

for item, price in zip(items, prices):
    if(len(item) > the_length):
        the_length = len(item)
    print(f"The price of {item:<{the_length}} is ${price:.2f}.")