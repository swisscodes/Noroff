pi = "3.14159265" # string
print( float(pi) )
# Convert the string to a float first, then cast that float to an int
print( int(float(pi)) )
mylist = [123,'hello world', []] # type: ignore
print( tuple(mylist) ) # type: ignore