import time
# 1. Get the current Unix timestamp
# time.time() returns the number of seconds since the epoch (January 1, 1970, 00:00:00 UTC).
current_timestamp = time.time()
print(f"Current Unix Timestamp: {current_timestamp}")
# 2. Convert a timestamp to a human-readable string (local time)
# time.ctime() takes a timestamp (or current time if no argument) and returns a string like "Mon Oct 26 14:30:00 2023".
human_readable_time = time.ctime(current_timestamp)
print(f"Human-readable time from timestamp: {human_readable_time}")
print(f"Current human-readable time: {time.ctime()}") # No argument uses current time
# 3. Pause script execution (sleep)
print("Pausing for 3 seconds...")
time.sleep(3) # Pauses the program for 3 seconds
print("Resumed after 3 seconds!")
# 4. Measure execution time of a code block (simple benchmarking)
start_time = time.time()
print("Performing a short task...")
for _ in range(1_000_000):
    pass # Do nothing, just loop
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Task took {elapsed_time:.4f} seconds.")
# 5. High-resolution performance counter (often better for benchmarking)
# time.perf_counter() provides a high-resolution timer for measuring short durations.
# Its starting point is arbitrary, so only differences between calls are meaningful.
perf_start = time.perf_counter()
print("Performing another short task...")
_ = [x*x for x in range(10_000)] # A slightly more intensive task
perf_end = time.perf_counter()
perf_elapsed = perf_end - perf_start
print(f"High-resolution task took {perf_elapsed:.6f} seconds.")