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

# ==========================================
# MODERN PYTHON GUIDE: LIST OPERATIONS & DATA STRUCTURES
# ==========================================

# 1. Negative Indexing (Accessing from the End)
print("\n--- Negative Indexing ---")
print("Last element (x[-1]):", x[-1])
print("Second to last (x[-2]):", x[-2])

# 2. Pitfall Warning: Reference Assignment vs Shallow Copy
print("\n--- Safe List Copying ---")
original_list = [10, 20, 30]
alias_list = original_list            # DANGER: Both variables point to SAME list in memory!
actual_copy = original_list.copy()    # SAFE: Creates a distinct new list object

alias_list.append(999)
print(f"Original after modifying alias: {original_list} (Modified unexpectedly!)")
print(f"Independent copy remained:      {actual_copy}")

# 3. Modern Dataclass with Field Defaults
from dataclasses import dataclass, field

@dataclass(slots=True)  # 'slots=True' optimizes memory usage in Python 3.10+
class ModernRecord:
    id: int
    score: float
    description: str
    tags: list[str] = field(default_factory=lambda: list[str]())  # Safe mutable default

new_record = ModernRecord(id=202, score=9.85, description="High priority", tags=["python", "modern"])
print(f"\nModern Dataclass instance:\n{new_record}")