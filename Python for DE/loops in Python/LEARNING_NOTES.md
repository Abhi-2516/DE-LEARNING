# Loops in Python - Comprehensive Learning Notes

## 📚 Overview
This module covers all fundamental loop constructs in Python, from basic for loops to advanced iteration patterns with dictionaries and the walrus operator.

---

## 🎯 Topics Covered

### 1. **Basic For Loops**
**File:** `01_basic_for_loops/basic_for_loops.py`

**Concept:** Execute a code block multiple times using `for` with `range()`
```python
for variable in range(start, end):
    # Code executes for each iteration
```

**Key Points:**
- `range(1, 11)` generates numbers 1 to 10 (end is exclusive)
- `range(5)` starts from 0 by default: 0, 1, 2, 3, 4
- `range(1, 11, 2)` with step: 1, 3, 5, 7, 9

**Real-world Examples:**
- Token dispensers
- Batch processing
- Multiplication tables

**Best Practices:**
- Use meaningful variable names
- Keep loop body simple (extract complex logic to functions)
- Comment complex loop logic

---

### 2. **For Loops with Lists**
**File:** `02_for_loops_with_lists/for_loops_with_lists.py`

**Concept:** Iterate directly through list elements
```python
for element in list:
    # Access current element
```

**Key Points:**
- No need for index; directly access element
- Works with any iterable (lists, tuples, strings)
- Element type depends on list contents

**Real-world Examples:**
- Processing orders
- Managing tasks
- Iterating through names, products, etc.

**Common Pattern:**
```python
# Building new list while iterating
result = []
for item in items:
    result.append(process(item))
```

---

### 3. **Enumerate Function**
**File:** `03_enumerate/enumerate.py`

**Concept:** Get both index and value while iterating
```python
for index, value in enumerate(list, start=0):
    # index: position (default starts at 0)
    # value: actual element
```

**Key Points:**
- Default start is 0
- Custom start: `enumerate(items, start=1)`
- Much cleaner than manual index tracking

**Use Cases:**
- Creating numbered lists/menus
- Roll number assignment
- Position-based processing

**Comparison:**
```python
# Without enumerate (verbose)
for i in range(len(items)):
    print(f"{i}: {items[i]}")

# With enumerate (clean)
for i, item in enumerate(items):
    print(f"{i}: {item}")
```

---

### 4. **Zip Function**
**File:** `04_zip_function/zip_function.py`

**Concept:** Pair elements from multiple iterables
```python
for elem1, elem2 in zip(list1, list2):
    # Process paired elements
```

**Key Points:**
- Stops at shortest list length
- Pairs elements position-wise
- Can zip 2+ iterables simultaneously

**Real-world Examples:**
- Matching names with scores
- Pairing customers with bills
- Matching questions with answers

**Comparison:**
```python
# Without zip (manual indexing)
for i in range(len(names)):
    print(f"{names[i]}: {scores[i]}")

# With zip (elegant)
for name, score in zip(names, scores):
    print(f"{name}: {score}")
```

---

### 5. **While Loops**
**File:** `05_while_loops/while_loops.py`

**Concept:** Execute block while condition is true
```python
while condition:
    # Code executes while condition is True
    # Must modify condition to avoid infinite loop!
```

**Key Points:**
- Condition checked before each iteration
- Must have counter/condition change inside loop
- Use `while True` with `break` for "do-until" pattern

**Common Pattern - Increment Counter:**
```python
count = 0
while count < 10:
    print(count)
    count += 1  # Must update condition!
```

**Common Pattern - User Input:**
```python
while True:
    user_input = input("Enter command: ")
    if user_input == "quit":
        break
    process(user_input)
```

**Real-world Examples:**
- ATM withdrawals
- Temperature monitoring
- Input validation
- Countdown timers

**For vs While:**
| For | While |
|-----|-------|
| Count-based | Condition-based |
| Known iterations | Unknown iterations |
| `for x in range(10)` | `while x < 10` |

---

### 6. **Loop Control Statements**
**File:** `06_loop_control/loop_control.py`

**Break Statement:**
```python
for item in items:
    if item == target:
        break  # Exit loop immediately
```

**Continue Statement:**
```python
for item in items:
    if item.is_invalid():
        continue  # Skip this iteration
    process(item)
```

**Key Differences:**
| Statement | Effect | Use Case |
|-----------|--------|----------|
| `break` | Exit loop completely | Found target, stop processing |
| `continue` | Skip to next iteration | Skip invalid items |
| (no statement) | Execute block normally | Process item |

**Important:**
- In nested loops, `break` only exits innermost loop
- Use function return to exit multiple levels
- Prefer clear logic over complex control flow

---

### 7. **Advanced Loop Patterns**
**File:** `07_advanced_loops/advanced_loops.py`

#### **Dictionary in Loops**
```python
for key, value in dictionary.items():
    # Access both key and value
```

**Iterating Dictionary:**
```python
# Keys only
for key in dictionary.keys():
    value = dictionary[key]

# Values only
for value in dictionary.values():
    total += value

# Key-value pairs
for key, value in dictionary.items():
    print(f"{key}: {value}")
```

**Use Dictionary Instead of If-Elif:**
```python
# Bad: Many if-elif statements
if category == "gold":
    discount = 0.20
elif category == "silver":
    discount = 0.15
elif category == "bronze":
    discount = 0.10
else:
    discount = 0.05

# Good: Use dictionary lookup
discounts = {
    "gold": 0.20,
    "silver": 0.15,
    "bronze": 0.10,
}
discount = discounts.get(category, 0.05)
```

#### **Walrus Operator (:=)** (Python 3.8+)
Assign a value while using it in a condition
```python
if (remainder := value % 5):
    print(f"Remainder: {remainder}")
```

**Benefits:**
- Avoid computing same value twice
- More concise code
- Clear intent

**Example:**
```python
# Without walrus
password = "secure123"
if len(password) >= 8:
    print(f"Length: {len(password)}")  # Computed twice!

# With walrus
if (pwd_length := len(password)) >= 8:
    print(f"Length: {pwd_length}")  # Computed once
```

---

## 📊 Decision Tree: Which Loop to Use?

```
Do you need to repeat code?
│
├─ Know exact number of iterations?
│  └─ Use: for loop with range()
│
├─ Iterating through a collection?
│  ├─ Need index? → for i, item in enumerate()
│  └─ No index? → for item in collection
│
├─ Need to pair items from lists?
│  └─ Use: zip()
│
├─ Don't know iteration count (condition-based)?
│  └─ Use: while loop
│
└─ Want to get both index AND value?
   └─ Use: enumerate()
```

---

## 🔑 Key Concepts Summary

| Concept | Syntax | Use Case |
|---------|--------|----------|
| For Loop | `for x in range(n):` | Count-based iteration |
| For-In | `for item in list:` | Iterate collection |
| Enumerate | `for i, v in enumerate(list):` | Get index and value |
| Zip | `for a, b in zip(l1, l2):` | Pair items |
| While | `while condition:` | Condition-based iteration |
| Break | `break` | Exit loop |
| Continue | `continue` | Skip iteration |
| Walrus | `if (x := expr):` | Assign in condition |

---

## ⚠️ Common Mistakes & Solutions

### 1. **Off-by-One Error with Range**
```python
# WRONG - range(10) is 0-9, not 1-10
for i in range(10):
    print(f"Token #{i}")  # Prints 0-9

# CORRECT
for i in range(1, 11):
    print(f"Token #{i}")  # Prints 1-10
```

### 2. **Infinite Loop**
```python
# WRONG - condition never becomes False
while True:
    print("This prints forever!")
    # Missing break or condition change

# CORRECT
counter = 0
while counter < 5:
    print(counter)
    counter += 1  # Modify condition!
```

### 3. **Incorrect Walrus Usage**
```python
# WRONG - walrus doesn't work this way
if value := 5:  # Always True!
    print(value)

# CORRECT - walrus for assignment in condition
if (result := compute()) > 0:
    print(result)
```

### 4. **Modifying List While Iterating**
```python
# WRONG - Can cause skipped or repeated items
items = [1, 2, 3, 4, 5]
for item in items:
    if item == 3:
        items.remove(item)  # Dangerous!

# CORRECT - Iterate over copy
for item in items[:]:
    if item == 3:
        items.remove(item)

# BETTER - Use list comprehension
items = [x for x in items if x != 3]
```

### 5. **Break in Nested Loop**
```python
# WRONG - break only exits inner loop
for i in range(3):
    for j in range(3):
        if i == 1 and j == 1:
            break  # Only breaks inner loop!
    # Still loops i=2

# CORRECT - Use flag or function
def search():
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                return True
    return False
```

### 6. **Zip with Different Lengths**
```python
# Unexpected truncation
names = ["Alice", "Bob"]
ages = [25, 30, 35]  # Extra element

for name, age in zip(names, ages):
    print(f"{name}: {age}")
# Output: Alice: 25, Bob: 30
# Age 35 is ignored!

# Use zip_longest if you need all elements
from itertools import zip_longest
for name, age in zip_longest(names, ages, fillvalue="N/A"):
    print(f"{name}: {age}")
```

---

## 💡 Best Practices

1. **Use for loops for known iterations**
   - Cleaner and more Pythonic than while
   - Less error-prone (no infinite loops)

2. **Prefer enumerate over range(len())**
   ```python
   # Bad
   for i in range(len(items)):
       print(f"{i}: {items[i]}")
   
   # Good
   for i, item in enumerate(items):
       print(f"{i}: {item}")
   ```

3. **Use zip for parallel iteration**
   ```python
   # Bad - manual indexing
   for i in range(len(names)):
       print(names[i], scores[i])
   
   # Good - zip handles pairing
   for name, score in zip(names, scores):
       print(name, score)
   ```

4. **Avoid complex nested loops**
   - Limit nesting to 2-3 levels
   - Extract inner logic to functions
   - Consider list comprehensions

5. **Use dictionary for multiple conditions**
   ```python
   # Bad - many if-elif statements
   if type == "A": result = 10
   elif type == "B": result = 20
   
   # Good - use dictionary
   results = {"A": 10, "B": 20}
   result = results.get(type, 0)
   ```

6. **Make loop variables meaningful**
   ```python
   # Bad
   for x in users:
       print(x)
   
   # Good
   for user in users:
       print(user)
   ```

---

## 📝 Practice Exercises

1. **Print 1 to 100** using different loop methods
2. **Find largest number** in a list using loops
3. **Create multiplication table** for a range of numbers
4. **Pair student names with grades** using zip
5. **Sum numbers until 0** is entered (while loop)
6. **Filter list** by removing items matching criteria (continue)
7. **Search for element** and stop when found (break)
8. **Count word occurrences** in a string using dictionaries

---

## 🚀 Next Steps

- Practice basic loops before advanced patterns
- Combine loops with conditionals
- Learn list comprehensions (more on this later)
- Explore iterator and generator concepts
- Learn about `map()`, `filter()` alternatives to loops

---

## 📖 Reference

**Python Documentation:**
- [For Loops](https://docs.python.org/3/tutorial/controlflow.html#for-statements)
- [While Loops](https://docs.python.org/3/tutorial/controlflow.html#while-loops)
- [Enumerate](https://docs.python.org/3/library/functions.html#enumerate)
- [Zip](https://docs.python.org/3/library/functions.html#zip)
- [Break/Continue](https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops)
- [Walrus Operator](https://www.python.org/dev/peps/pep-0572/)

---

**Last Updated:** 2024  
**Python Version:** 3.8+ (for walrus operator)
