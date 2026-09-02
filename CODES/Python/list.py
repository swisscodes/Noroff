from dataclasses import dataclass

@dataclass
class Record:
    id: int
    score: float
    description: str
    notes: list[str] | None = None

x = []
y = [1,2,3,4,5]
z = ["h","e","l","l","o"," ","w","o","r","l","d"]
q = Record(id=123, score=4.567, description="eight nine ten", notes=["acceptable"]) #this is for later typing practice


x = [1,2,3,4] # declare our simple list
# len(list)
print( "len(x): ", len(x) )
# list[position]
print( "x[0]: ", x[0] )
x[0] = 9 # assignment
print( "x[0]: ", x[0] )
# list.append(item)
x.append(5)
print( "list.append: ", x )