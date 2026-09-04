def while_countdown(n: int):
    while n > 0:
        print(n)
        n -= 1
    print("Countdown finished!")

while_countdown(5)

"""
Infinity loop happens when we have a recursive function or a loop that doesnt have proper exit condition
for example the while loop above if we havent decremented n, there will be no way our program will understand
when or how to stop the loop, and it will keep running forever. this is called infinity loop.
"""