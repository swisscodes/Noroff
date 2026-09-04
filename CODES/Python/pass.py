x = 'b'
if (x == 'a'): # type: ignore
    print( "x is 'a'" )
elif(x == 'b'):
    print( "x is 'b'" )
    pass # TODO: Do something useful here!
else:
    print( "x does not have 'a' or 'b'" )
