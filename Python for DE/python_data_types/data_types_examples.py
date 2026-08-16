# Python Data Types Examples
# Covers built-in data types used in production-level Python engineering.

# 1. Numeric Types
print("--- Numeric Types ---")
num_int = 10
num_float = 10.5
num_complex = 2 + 3j

print(type(num_int), num_int)
print(type(num_float), num_float)
print(type(num_complex), num_complex)
print(num_complex.real, num_complex.imag)

# 2. Boolean Type
print("\n--- Boolean Type ---")
flag = True
is_valid = False
print(type(flag), flag)
print(True == 1)
print(False == 0)

# 3. String Type
print("\n--- String Type ---")
text = "Hello Python"
print(text)
print(text[0])
print(text[0:5])
print(text.upper())
print(text.lower())
print(text.split())
print(f"My name is {text}")

# 4. List Type
# mutable
print("\n--- List Type ---")
nums = [1, 2, 3, 4]
nums.reverse()
print(nums)
nums.append(5)
nums.insert(0, 0)
print(nums)
nums.pop()
print(nums)
print(nums[2])

# 5. Tuple Type
print("\n--- Tuple Type ---")
point = (10, 20)
print(point)
print(point[0], point[1])
# point[0] = 15  # TypeError, tuple is immutable

# 6. Range Type
print("\n--- Range Type ---")
values = range(0, 10, 2)
print(list(values))

# 7. Set Type
print("\n--- Set Type ---")
unique_numbers = {1, 2, 3, 3, 4}

spicies = {"cat", "dog", "fish"
           }


print(unique_numbers)
set_a = {1, 2, 3}
set_b = {3, 4, 5}
print(set_a | set_b)
print(set_a & set_b)
print(set_a - set_b)

# 8. Frozenset Type
print("\n--- Frozenset Type ---")
allowed = frozenset({"read", "write"})
print(allowed)

# 9. Dictionary Type
print("\n--- Dictionary Type ---")
user = {"name": "Hitesh", "age": 25, "city": "Delhi"}
print(user)
print(user["name"])
user["country"] = "India"
print(user.get("email", "Not Found"))
print(user)

# 10. Bytes Type
print("\n--- Bytes Type ---")
byte_data = b"hello"
print(byte_data)
print(byte_data[0])
# byte_data[0] = 72  # TypeError, bytes is immutable

# 11. Bytearray Type
print("\n--- Bytearray Type ---")
arr = bytearray(b"hello")
arr[0] = 72
print(arr)
print(arr.decode())

# 12. None Type
print("\n--- None Type ---")
result = None
print(result is None)

# 13. Production-level collection utilities
print("\n--- Collection Utilities ---")
from collections import Counter, defaultdict, deque, namedtuple

# Counter
freq = Counter("banana")
print(freq)

# defaultdict
scores = defaultdict(int)
scores["math"] += 5
scores["science"] += 3
print(scores)

# deque
queue = deque(["a", "b", "c"])
queue.append("d")
queue.popleft()
print(queue)

# namedtuple
Point = namedtuple("Point", ["x", "y"])
p = Point(10, 20)
print(p.x, p.y)

# 14. Dataclass Example
print("\n--- Dataclass ---")
from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int

u = User("Hitesh", 25)
print(u)

# 15. Type hints example
print("\n--- Type Hints ---")
from typing import Dict, List, Optional

names: List[str] = ["Amit", "Neha"]
meta: Dict[str, int] = {"age": 25}
optional_name: Optional[str] = None
print(names)
print(meta)
print(optional_name)

# 16. Example of mutability
print("\n--- Mutability ---")
list_data = [1, 2, 3]
list_data.append(4)
print(list_data)

str_data = "python"
# str_data[0] = 'P'  # TypeError
new_str = 'P' + str_data[1:]
print(new_str)

# 17. Hashability Example
print("\n--- Hashability ---")
print(hash("python"))
# print(hash([1,2,3]))  # TypeError: unhashable type: 'list'

# 18. Real world example: dictionary from data
print("\n--- Real world config example ---")
config = {
    "host": "localhost",
    "port": 8080,
    "debug": True,
    "tags": {"api", "python"},
    "metadata": {"owner": "team"}
}
print(config)

# 19. Numeric precision caution
print("\n--- Float caution ---")
print(0.1 + 0.2)
from decimal import Decimal
print(Decimal("0.1") + Decimal("0.2"))

# 20. String formatting examples
print("\n--- String formatting ---")
name = "Hitesh"
print(f"Hello {name}!")
print("Hello {}!".format(name))
print("%s" % name)

print("\nAll data type examples completed.")
