"""
===============================================================================
PYTHON SPECIAL (DUNDER) METHODS - COMPREHENSIVE GUIDE & REFERENCE
===============================================================================
Special methods (also known as "dunder" methods for Double UNDERscore) allow
custom Python classes to hook into Python's built-in operators, functions,
and language features (like +, len(), print(), with, [], ==, etc.).

-------------------------------------------------------------------------------
COMPLETE REFERENCE SUMMARY:
-------------------------------------------------------------------------------
1. LIFECYCLE & OBJECT CREATION
   - __new__(cls, *args, **kwargs) : Allocator (creates instance before __init__)
   - __init__(self, *args, **kw)   : Initializer (sets up instance attributes)
   - __del__(self)                 : Destructor / Finalizer (called on garbage collection)

2. STRING REPRESENTATION & FORMATTING
   - __repr__(self)                : Unambiguous representation (repr(obj), debuggers)
   - __str__(self)                 : Human-friendly string (str(obj), print(obj))
   - __bytes__(self)               : Byte representation (bytes(obj))
   - __format__(self, format_spec) : Formatted representation (format(obj), f"{obj:spec}")

3. COMPARISONS (RICH COMPARISONS) & TRUTHINESS
   - __eq__(self, other)           : Equality (a == b)
   - __ne__(self, other)           : Inequality (a != b)
   - __lt__(self, other)           : Less than (a < b)
   - __le__(self, other)           : Less than or equal (a <= b)
   - __gt__(self, other)           : Greater than (a > b)
   - __ge__(self, other)           : Greater than or equal (a >= b)
   - __bool__(self)                : Truth value test (bool(obj), if obj:)

4. ATTRIBUTE ACCESS & INTROSPECTION
   - __getattr__(self, name)       : Called ONLY when attribute is missing
   - __getattribute__(self, name)  : Intercepts EVERY attribute access
   - __setattr__(self, name, val)  : Intercepts attribute assignment (self.name = val)
   - __delattr__(self, name)       : Intercepts attribute deletion (del self.name)
   - __dir__(self)                 : Called by dir(obj)

5. CONTAINER & SEQUENCE PROTOCOL
   - __len__(self)                 : Length of container (len(obj))
   - __getitem__(self, key)        : Indexing & slicing (obj[key], obj[1:3])
   - __setitem__(self, key, val)   : Item assignment (obj[key] = val)
   - __delitem__(self, key)        : Item deletion (del obj[key])
   - __iter__(self)                : Returns an iterator (iter(obj), for x in obj:)
   - __next__(self)                : Advances iterator (next(it))
   - __reversed__(self)            : Returns reversed iterator (reversed(obj))
   - __contains__(self, item)      : Membership test (item in obj)
   - __missing__(self, key)        : Called on missing key in dict subclasses

6. ARITHMETIC & NUMERIC OPERATORS
   - Binary Arithmetic:
       __add__(self, other)        : Addition (a + b)
       __sub__(self, other)        : Subtraction (a - b)
       __mul__(self, other)        : Multiplication (a * b)
       __truediv__(self, other)    : Float division (a / b)
       __floordiv__(self, other)   : Floor division (a // b)
       __mod__(self, other)        : Modulo (a % b)
       __pow__(self, other[, mod]) : Exponentiation (a ** b, pow(a, b))
       __matmul__(self, other)     : Matrix multiplication (a @ b)
   - Reflected (Right-hand) Arithmetic:
       __radd__, __rsub__, __rmul__, __rtruediv__, __rfloordiv__, __rmod__, __rpow__
   - In-place (Augmented Assignment):
       __iadd__, __isub__, __imul__, __itruediv__, __ifloordiv__, __imod__, __ipow__
   - Unary Math:
       __neg__ (-a), __pos__ (+a), __abs__ (abs(a)), __invert__ (~a)
       __round__ (round(a)), __trunc__, __floor__, __ceil__
   - Conversions:
       __int__(a), __float__(a), __complex__(a), __index__(a)

7. CALLABLE OBJECTS & CONTEXT MANAGERS
   - __call__(self, *args, **kw)   : Invoked when instance is called like a function obj()
   - __enter__(self)               : Setup for 'with obj as x:' context manager
   - __exit__(self, exc, val, tb)  : Teardown for 'with' block (handles exceptions)

8. HASHING & COPYING
   - __hash__(self)                : Hash code for dictionary keys & sets (hash(obj))
   - __sizeof__(self)              : Memory size in bytes (sys.getsizeof(obj))
   - __copy__(self)                : Shallow copy hook (copy.copy(obj))
   - __deepcopy__(self, memo)      : Deep copy hook (copy.deepcopy(obj))

9. DESCRIPTORS & METAPROGRAMMING
   - __get__, __set__, __delete__, __set_name__ (Descriptor protocol)
   - __init_subclass__(cls)        : Hook for when another class inherits from this class
   - __class_getitem__(cls, item)  : Generic type subscripting (MyClass[int])
===============================================================================
"""

from typing import Any, List, Optional


# =============================================================================
# PART 1: PRACTICAL IMPLEMENTATION - THE HOUSE CLASS
# =============================================================================

class House:
    """
    Demonstrates practical usage of Python special (dunder) methods
    on a domain model (House).
    """

    # -------------------------------------------------------------------------
    # 1. LIFECYCLE METHODS
    # -------------------------------------------------------------------------
    def __new__(cls, *args: Any, **kwargs: Any) -> "House":
        """
        __new__ is the real constructor. It allocates memory and returns the
        new instance. It runs BEFORE __init__.
        """
        instance = super().__new__(cls)
        return instance

    def __init__(
        self,
        doors: int = 1,
        windows: int = 4,
        wall_color: str = "blue",
        rooms: Optional[List[str]] = None,
        market_value: float = 250_000.0,
    ) -> None:
        """
        __init__ initializes the newly created instance attributes.
        """
        self.doors: int = doors
        self.windows: int = windows
        self.wall_color: str = wall_color
        self.rooms: List[str] = rooms if rooms is not None else ["Living Room", "Bedroom", "Kitchen"]
        self.market_value: float = market_value
        self.front_door_locked: bool = True

    # -------------------------------------------------------------------------
    # 2. STRING REPRESENTATION & FORMATTING
    # -------------------------------------------------------------------------
    def __repr__(self) -> str:
        """
        Unambiguous official string representation.
        Triggered by: repr(house), interactive shell, or inside lists/dicts.
        """
        return (
            f"House(doors={self.doors}, windows={self.windows}, "
            f"wall_color='{self.wall_color}', market_value={self.market_value})"
        )

    def __str__(self) -> str:
        """
        User-friendly, readable string representation.
        Triggered by: str(house), print(house), f'{house}'.
        """
        return (
            f"A {self.wall_color} house with {self.doors} door(s), "
            f"{self.windows} window(s), and {len(self.rooms)} room(s)."
        )

    def __format__(self, format_spec: str) -> str:
        """
        Custom formatting support.
        Triggered by: format(house, spec) or f"{house:spec}".
        """
        if format_spec == "short":
            return f"House[{self.wall_color}, {self.doors}D/{self.windows}W]"
        if format_spec == "price":
            return f"${self.market_value:,.2f}"
        return str(self)

    # -------------------------------------------------------------------------
    # 3. COMPARISONS & TRUTHINESS
    # -------------------------------------------------------------------------
    def __eq__(self, other: object) -> bool:
        """
        Triggered by: house1 == house2
        Checks equality based on doors, windows, and color.
        """
        if not isinstance(other, House):
            return NotImplemented
        return (
            self.doors == other.doors
            and self.windows == other.windows
            and self.wall_color == other.wall_color
        )

    def __lt__(self, other: "House") -> bool:
        """
        Triggered by: house1 < house2 (e.g. sorting houses)
        Compares houses by market value.
        """
        if not isinstance(other, House):
            return NotImplemented
        return self.market_value < other.market_value

    def __bool__(self) -> bool:
        """
        Triggered by: bool(house), if house:
        Evaluates to True if the house has at least 1 door and 1 window.
        """
        return self.doors > 0 and self.windows > 0

    # -------------------------------------------------------------------------
    # 4. CONTAINER & SEQUENCE PROTOCOL
    # -------------------------------------------------------------------------
    def __len__(self) -> int:
        """
        Triggered by: len(house)
        Returns the number of rooms in the house.
        """
        return len(self.rooms)

    def __getitem__(self, index: int) -> str:
        """
        Triggered by: house[0], house[-1], or slicing house[1:3]
        Enables indexing into the house's rooms.
        """
        return self.rooms[index]

    def __setitem__(self, index: int, room_name: str) -> None:
        """
        Triggered by: house[0] = 'Guest Room'
        Enables item assignment by index.
        """
        self.rooms[index] = room_name

    def __contains__(self, item: str) -> bool:
        """
        Triggered by: 'Kitchen' in house
        Membership test for rooms.
        """
        return item in self.rooms

    def __iter__(self):
        """
        Triggered by: for room in house:
        Yields rooms one by one.
        """
        return iter(self.rooms)

    # -------------------------------------------------------------------------
    # 5. ARITHMETIC / OPERATOR OVERLOADING
    # -------------------------------------------------------------------------
    def __add__(self, other: "House") -> "House":
        """
        Triggered by: combined_house = house1 + house2
        Merges two houses into a larger house.
        """
        if not isinstance(other, House):
            return NotImplemented
        return House(
            doors=self.doors + other.doors,
            windows=self.windows + other.windows,
            wall_color=f"{self.wall_color}-{other.wall_color}",
            rooms=self.rooms + other.rooms,
            market_value=self.market_value + other.market_value,
        )

    # -------------------------------------------------------------------------
    # 6. CALLABLE OBJECT
    # -------------------------------------------------------------------------
    def __call__(self, visitor: str = "Guest") -> str:
        """
        Triggered by: house("Alice") or house()
        Allows the instance to be called directly like a function!
        """
        return f"Ding-dong! {visitor} rang the doorbell at the {self.wall_color} house."

    # -------------------------------------------------------------------------
    # 7. CONTEXT MANAGER PROTOCOL ('with' statement)
    # -------------------------------------------------------------------------
    def __enter__(self) -> "House":
        """
        Triggered when entering a 'with house:' block.
        Unlocks the door upon entry.
        """
        self.front_door_locked = False
        print(f"-> [__enter__] Unlocking front door of {self.wall_color} house.")
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> Optional[bool]:
        """
        Triggered when exiting a 'with house:' block.
        Locks the door upon exit.
        """
        self.front_door_locked = True
        print(f"<- [__exit__] Locking front door of {self.wall_color} house.")
        return False  # False means do not suppress exceptions if any occurred

    # -------------------------------------------------------------------------
    # 8. ATTRIBUTE ACCESS FALLBACK
    # -------------------------------------------------------------------------
    def __getattr__(self, name: str) -> str:
        """
        Triggered ONLY when an attribute is requested that does NOT exist.
        """
        return f"Property '{name}' is not configured for this House."


# =============================================================================
# PART 2: ARITHMETIC OPERATORS DEMO (VECTOR CLASS)
# =============================================================================

class Vector:
    """
    Demonstrates numeric operators, type conversion, and hashing.
    """

    def __init__(self, x: float, y: float) -> None:
        self.x: float = x
        self.y: float = y

    # Representation
    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y})"

    def __str__(self) -> str:
        return f"<{self.x}, {self.y}>"

    # Math Operators
    def __add__(self, other: "Vector") -> "Vector":      # v1 + v2
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":      # v1 - v2
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar: float) -> "Vector":        # v * scalar
        return Vector(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar: float) -> "Vector":       # scalar * v (Reflected)
        return self.__mul__(scalar)

    def __iadd__(self, other: "Vector") -> "Vector":     # v += other (In-place)
        self.x += other.x
        self.y += other.y
        return self

    # Unary & Math
    def __neg__(self) -> "Vector":                       # -v
        return Vector(-self.x, -self.y)

    def __abs__(self) -> float:                          # abs(v) -> magnitude
        return (self.x**2 + self.y**2) ** 0.5

    # Type Conversion
    def __int__(self) -> int:                            # int(v)
        return int(abs(self))

    def __float__(self) -> float:                        # float(v)
        return float(abs(self))

    # Hashing (allows Vector to be a dictionary key or in a set)
    def __eq__(self, other: object) -> bool:
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return False

    def __hash__(self) -> int:                           # hash(v)
        return hash((self.x, self.y))


# =============================================================================
# PART 3: RUNNABLE DEMONSTRATIONS
# =============================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("DEMONSTRATION OF PYTHON SPECIAL METHODS IN ACTION")
    print("=" * 70)

    # 1. Lifecycle & String Representation
    print("\n--- 1. String Representation (__repr__, __str__, __format__) ---")
    house1 = House(doors=2, windows=6, wall_color="white", market_value=320_000.0)
    house2 = House(doors=1, windows=4, wall_color="blue", market_value=250_000.0)

    print("print(house1)       ->", str(house1))                # calls __str__
    print("repr(house1)        ->", repr(house1))               # calls __repr__
    print(f"Format short       -> {house1:short}")              # calls __format__
    print(f"Format price       -> {house1:price}")              # calls __format__

    # 2. Rich Comparisons
    print("\n--- 2. Comparisons (__eq__, __lt__, __bool__) ---")
    house_copy = House(doors=2, windows=6, wall_color="white")
    print("house1 == house_copy ->", house1 == house_copy)      # calls __eq__ (True)
    print("house1 == house2     ->", house1 == house2)          # calls __eq__ (False)
    print("house2 < house1      ->", house2 < house1)           # calls __lt__ (True: 250k < 320k)
    print("bool(house1)         ->", bool(house1))              # calls __bool__ (True)

    # 3. Container & Sequence Protocol
    print("\n--- 3. Container Protocol (__len__, __getitem__, __contains__, __iter__) ---")
    print("len(house1)          ->", len(house1))               # calls __len__
    print("house1[0] (1st room) ->", house1[0])                 # calls __getitem__
    print("'Kitchen' in house1  ->", "Kitchen" in house1)       # calls __contains__
    print("Rooms iteration      ->", [room for room in house1]) # calls __iter__

    # 4. Addition / Operator Overloading
    print("\n--- 4. Operator Overloading (__add__) ---")
    combined_estate = house1 + house2                           # calls __add__
    print("Combined Estate      ->", combined_estate)
    print("Combined Rooms       ->", combined_estate.rooms)

    # 5. Callable Instance
    print("\n--- 5. Callable Object (__call__) ---")
    print(house1("Bob"))                                        # calls __call__

    # 6. Context Manager Protocol
    print("\n--- 6. Context Manager Protocol (__enter__, __exit__) ---")
    with house1 as h:
        print(f"Inside 'with' block: Is front door locked? {h.front_door_locked}")
    print(f"After 'with' block:  Is front door locked? {house1.front_door_locked}")

    # 7. Missing Attribute Fallback
    print("\n--- 7. Attribute Fallback (__getattr__) ---")
    print("house1.swimming_pool ->", house1.swimming_pool)      # calls __getattr__

    # 8. Numeric Vector Demo
    print("\n--- 8. Numeric & Math Operators (Vector Class) ---")
    v1 = Vector(3, 4)
    v2 = Vector(1, 2)
    print("v1 + v2              ->", v1 + v2)                   # calls __add__
    print("v1 - v2              ->", v1 - v2)                   # calls __sub__
    print("v1 * 3               ->", v1 * 3)                    # calls __mul__
    print("2 * v1 (reflected)   ->", 2 * v1)                    # calls __rmul__
    print("-v1 (unary neg)      ->", -v1)                       # calls __neg__
    print("abs(v1) (magnitude)  ->", abs(v1))                   # calls __abs__
    print("int(abs(v1))         ->", int(v1))                   # calls __int__

    # 9. Hashing & Sets
    print("\n--- 9. Hashing (__hash__, __eq__) ---")
    vector_set = {v1, v2, Vector(3, 4)}
    print("Vector set unique count ->", len(vector_set))        # Demonstrates hash dedup (2 unique)
    print("Vector map lookup       ->", {v1: "Vector Point A"}[Vector(3, 4)])

    print("\n" + "=" * 70)
    print("ALL SPECIAL METHOD DEMONSTRATIONS COMPLETED SUCCESSFULLY!")
    print("=" * 70)