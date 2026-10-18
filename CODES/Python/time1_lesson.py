"""
=============================================================================
                    PYTHON TIME & DATETIME BEST PRACTICES
=============================================================================
This lesson covers modern Python (3.9+) standards for handling dates, time,
timezones, intervals, and benchmarking correctly and reliably.
=============================================================================
"""

import time
from datetime import datetime, timezone, timedelta
from zoneinfo import ZoneInfo

print("=" * 70)
print("LESSON: MODERN PYTHON TIME & DATETIME BEST PRACTICES")
print("=" * 70)

# ---------------------------------------------------------------------------
# 1. NAIVE VS. AWARE DATETIMES (THE #1 RULE)
# ---------------------------------------------------------------------------
# - NAIVE datetime: Has NO timezone info attached (e.g. datetime.now()).
#   Problem: Python doesn't know what timezone it belongs to. Comparing two
#   naive datetimes across servers or timezones causes silent, critical bugs.
# - AWARE datetime: Has explicit timezone info (e.g. UTC or IANA zone).
#   BEST PRACTICE: Always work with timezone-aware datetimes!
# ---------------------------------------------------------------------------
print("\n--- 1. Aware vs. Naive Datetimes ---")

# DEPRECATED IN PYTHON 3.12+: datetime.utcnow() (Returns a naive datetime!)
# BEST PRACTICE:
utc_now = datetime.now(timezone.utc)
print(f"Current UTC time (Aware)     : {utc_now}")
print(f"Timezone information attached: {utc_now.tzinfo}")

# ---------------------------------------------------------------------------
# 2. THE GOLDEN STORAGE RULE: STORE IN UTC, DISPLAY IN LOCAL
# ---------------------------------------------------------------------------
# Always store and process timestamps in UTC (database, APIs, files).
# Convert to the user's local timezone ONLY at the presentation layer (UI).
# ---------------------------------------------------------------------------
print("\n--- 2. Timezone Conversion (Using standard 'zoneinfo') ---")

# Convert the UTC time to specific local timezones:
oslo_tz = ZoneInfo("Europe/Oslo")
new_york_tz = ZoneInfo("America/New_York")
tokyo_tz = ZoneInfo("Asia/Tokyo")

oslo_time = utc_now.astimezone(oslo_tz)
ny_time = utc_now.astimezone(new_york_tz)
tokyo_time = utc_now.astimezone(tokyo_tz)

print(f"UTC Time     : {utc_now.strftime('%Y-%m-%d %H:%M:%S %Z')}")
print(f"Oslo Time    : {oslo_time.strftime('%Y-%m-%d %H:%M:%S %Z (UTC%z)')}")
print(f"New York     : {ny_time.strftime('%Y-%m-%d %H:%M:%S %Z (UTC%z)')}")
print(f"Tokyo        : {tokyo_time.strftime('%Y-%m-%d %H:%M:%S %Z (UTC%z)')}")

# ---------------------------------------------------------------------------
# 3. SERIALIZATION: ISO 8601 (THE STANDARD FOR APIs & JSON)
# ---------------------------------------------------------------------------
# Don't invent custom date string formats like '13/09/2026 10:30 PM'.
# Use ISO 8601 strings: 'YYYY-MM-DDTHH:MM:SS+00:00'.
# ---------------------------------------------------------------------------
print("\n--- 3. ISO 8601 Strings (Serialization & Parsing) ---")

# Convert datetime to standard ISO string
iso_string = utc_now.isoformat()
print(f"Serialized to ISO 8601: {iso_string}")

# Parse standard ISO string back to datetime (built into Python!)
restored_dt = datetime.fromisoformat(iso_string)
print(f"Parsed from ISO 8601  : {restored_dt} (Timezone: {restored_dt.tzinfo})")

# ---------------------------------------------------------------------------
# 4. WORKING WITH UNIX TIMESTAMPS SAFELY
# ---------------------------------------------------------------------------
# Unix timestamp = Seconds elapsed since Jan 1, 1970 00:00:00 UTC.
# When converting back to datetime, ALWAYS specify tz=timezone.utc.
# ---------------------------------------------------------------------------
print("\n--- 4. Unix Timestamps ---")

current_epoch_seconds = utc_now.timestamp()
print(f"Current Unix timestamp: {current_epoch_seconds}")

# BEST PRACTICE: Always pass tz=timezone.utc to fromtimestamp
dt_from_timestamp = datetime.fromtimestamp(current_epoch_seconds, tz=timezone.utc)
print(f"Datetime from timestamp: {dt_from_timestamp}")

# ---------------------------------------------------------------------------
# 5. CHOOSING THE RIGHT CLOCK FOR BENCHMARKING & INTERVALS
# ---------------------------------------------------------------------------
# Why NEVER use time.time() to measure elapsed time?
# - time.time() follows the system wall clock, which can jump backwards or
#   forwards (e.g. NTP synchronization, user adjusts clock, daylight saving).
#
# Use the correct tool for the job:
# - time.monotonic()    : Guaranteed to never go backwards. Best for timeouts.
# - time.perf_counter()  : Highest resolution clock available. Best for benchmarking.
# - time.process_time()  : Measures CPU time used by current process (ignores sleep/IO).
# ---------------------------------------------------------------------------
print("\n--- 5. Measuring Elapsed Time Correctly ---")

start_perf = time.perf_counter()
start_cpu = time.process_time()

# Simulate a task with both CPU work and sleeping (I/O simulation)
sum(x * x for x in range(500_000))
time.sleep(0.1)

end_perf = time.perf_counter()
end_cpu = time.process_time()

print(f"Wall-clock elapsed (perf_counter) : {end_perf - start_perf:.6f} s (Includes sleep)")
print(f"CPU execution time (process_time) : {end_cpu - start_cpu:.6f} s (Excludes sleep)")

# ---------------------------------------------------------------------------
# 6. TIMEDELTA ARITHMETIC (DURATIONS & EXPIRATIONS)
# ---------------------------------------------------------------------------
# Use timedelta for adding/subtracting intervals or setting expiration dates.
# ---------------------------------------------------------------------------
print("\n--- 6. Timedelta (Expirations and Windows) ---")

session_timeout = timedelta(hours=2, minutes=30)
expires_at = utc_now + session_timeout
remaining = expires_at - utc_now

print(f"Now                 : {utc_now.strftime('%H:%M:%S')}")
print(f"Session expires at  : {expires_at.strftime('%H:%M:%S')}")
print(f"Total duration (sec): {remaining.total_seconds():.0f} seconds")

# ---------------------------------------------------------------------------
# 7. SUMMARY CHEAT SHEET: THE 6 GOLDEN RULES
# ---------------------------------------------------------------------------
print("\n" + "=" * 70)
print("SUMMARY: THE 6 GOLDEN RULES OF TIME IN PYTHON")
print("=" * 70)
print("1. Avoid naive datetimes; always use timezone-aware datetimes.")
print("2. Never use datetime.utcnow() (deprecated). Use datetime.now(timezone.utc).")
print("3. Always store & exchange time in UTC (ISO 8601 format).")
print("4. Convert to local timezone (via zoneinfo.ZoneInfo) ONLY when presenting to users.")
print("5. Use time.perf_counter() for benchmarking, and time.monotonic() for timeouts.")
print("6. Never use time.time() for measuring code execution duration.")
print("=" * 70)