x = ['a','b','c','d']
y = [100,200,300,400]
for (item) in zip(x,y):
   item_x = item[0]
   item_y = item[1]
   print( f"{item}: Item {item_x} has the value NOR{item_y}" )


#Similar to enumerate, we can also use tuple unpacking in a for loop to access each item easily:
items = []
products = ["cheese", "chocolate", "pie", "pants"]
prices = [29.99, 15.50, 17.99, 199.99]
sales = [2, 10, 0, 200]
for (p1, p2, s) in zip(products,prices,sales):
   items.append({"product":p1, "price":p2, "sale":s}) # type: ignore
   print( f"{p1} sold for a profit of {p2 * s}" )
   print(items ) # type: ignore
   