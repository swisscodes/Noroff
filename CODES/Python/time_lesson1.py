from datetime import datetime, date, time, timedelta
# 1. Get the Current Date and Time
# datetime.now() returns a datetime object representing the current moment.
now = datetime.now()
print(f"Current Date and Time: {now}")
# 2. Extract Date and Time Components
print(f"Year: {now.year}, Month: {now.month}, Day: {now.day}")
print(f"Hour: {now.hour}, Minute: {now.minute}, Second: {now.second}")
# 3. Format a datetime object into a String (strftime - string format time)
# You can use various format codes (e.g., %Y for full year, %m for month, %d for day, %H for hour).
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print(f"Formatted Date and Time: {formatted_date}")
# 4. Create a specific datetime object
# You can specify year, month, day, hour, minute, second, microsecond.
specific_moment = datetime(2023, 10, 26, 14, 30, 0)
print(f"Specific Moment: {specific_moment}")
# 5. Perform Date Arithmetic using timedelta
# timedelta represents a duration. You can add or subtract it from datetime objects.
one_week_later = now + timedelta(weeks=1)
print(f"One week from now: {one_week_later.strftime('%Y-%m-%d')}")
three_days_ago = now - timedelta(days=3)
print(f"Three days ago: {three_days_ago.strftime('%Y-%m-%d')}")
time_difference = one_week_later - three_days_ago
print(f"Time difference (days): {time_difference.days}")
# 6. Parse a String into a datetime object (strptime - string parse time)
# You need to provide the exact format string that matches your input string.
date_string = "2024-07-15 10:45:00"
parsed_date = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print(f"Parsed Date from string: {parsed_date}")
# 7. Get only the date or only the time part
today_date_only = now.date()
current_time_only = now.time()
print(f"Today's date only: {today_date_only}")
print(f"Current time only: {current_time_only}")