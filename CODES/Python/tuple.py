persons = [ ("Alice","Alpha", 40), ("Bob","Beta",23) ]
for (name, surname, age) in persons:
    print(f"{name} {surname} is age {age}")

# ==========================================
# MODERN PYTHON GUIDE: TUPLE UNPACKING & NAMEDTUPLES
# ==========================================

# 1. Extended Unpacking with '*' (Rest operator)
record = ("EMP-1042", "Sarah", "Connor", "Lead", "Dev", "Cyberdyne")
emp_id, first_name, last_name, *job_titles, company = record
print(f"\nID: {emp_id}, Name: {first_name} {last_name}")
print(f"Job Titles: {job_titles}")
print(f"Company: {company}")

# 2. Modern Self-Documenting Tuples: typing.NamedTuple
# Standard tuples access by index (e.g. person[2]), which is prone to bugs.
# NamedTuples give you attribute access (person.age) with ZERO extra memory overhead!
from typing import NamedTuple

class Person(NamedTuple):
    name: str
    surname: str
    age: int

alice = Person(name="Alice", surname="Alpha", age=40)
print(f"\nNamedTuple: {alice.name} is {alice.age} years old.")
print(f"Dictionary conversion: {alice._asdict()}")

