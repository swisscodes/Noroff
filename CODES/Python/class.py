class House:
    '''This is class definition for a House object'''
    
    doors = 1
    windows = 4
    wall_color = 'blue'
    def house_info(self):
        return f'''This is a {self.wall_color} house \
        with {self.doors} doors \
        and {self.windows} windows.'''
print(House)
print(House.doors)
print(House.house_info)

House1 = House()
print( House1 )
print( House1.house_info() )


class QuickAdd:
    def add(self, x, y): # self must be defined first
        return x + y
qa = QuickAdd()
print(qa.add(10, 5)) # no self needed!