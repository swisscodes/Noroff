s = "some string to be split"
# split using the default parameters
s_split = s.split()
print( "s_split:", s_split )
d = "bob,barker,25,male,red hair,researcher"
# split using a defined separator
d_split = d.split(",")
print( "d.split:", d_split )


#to turn string to list as array
test = "abcdefgh"
print(list(test))

# ==========================================
# MODERN PYTHON GUIDE: STRING SPLITTING & PARSING
# ==========================================

# 1. Limiting Splits with 'maxsplit'
# Great for splitting a key-value header or first item without touching the rest:
log_entry = "2026-09-04 17:35:50 [ERROR] Database connection lost"
date, time, log_message = log_entry.split(" ", maxsplit=2)
print(f"\nMaxsplit result: Date={date}, Time={time}, Msg={log_message}")

# 2. Splitting from the Right with rsplit()
filename = "archive.backup.tar.gz"
name, ext = filename.rsplit(".", maxsplit=1)
print(f"rsplit result: Base='{name}', Extension='{ext}'")

# 3. Safe 3-part Extraction with partition()
# Always returns a 3-tuple: (before, separator, after)
url = "https://example.com/api/v1/users"
protocol, sep, endpoint = url.partition("://")
print(f"partition result: Protocol='{protocol}', Endpoint='{endpoint}'")

# 4. Multi-line Strings with splitlines()
multiline = "First line\r\nSecond line\nThird line"
print("splitlines handles all OS linebreaks:", multiline.splitlines())

