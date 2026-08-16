# Project 1: Basic For Loops

## 📋 Project Description

A foundation project demonstrating basic for loops using practical examples like tea token dispensers and batch processing.

## 🎯 Learning Objective

Understand how to create loops that execute a specific number of times using `range()` and basic loop structure.

## 💡 Concept Breakdown

### For Loop Syntax

```python
for variable in range(start, end, step):
    # Code executes for each iteration
```

### Understanding range()

| Syntax | Output | Notes |
|--------|--------|-------|
| `range(5)` | 0, 1, 2, 3, 4 | Starts at 0 by default |
| `range(1, 5)` | 1, 2, 3, 4 | End is exclusive |
| `range(1, 11)` | 1, 2, ..., 10 | Common for 1-10 |
| `range(1, 11, 2)` | 1, 3, 5, 7, 9 | Step of 2 |
| `range(10, 0, -1)` | 10, 9, ..., 1 | Counting down |

### Project Examples

**Tea Token Dispenser:**
```python
for token in range(1, 11):
    print(f"Serving chai with token #{token}")
```

**Output:**
```
Serving chai with token #1
Serving chai with token #2
...
Serving chai with token #10
```

## 🔑 Key Concepts

| Concept | Explanation | Example |
|---------|-------------|---------|
| **Variable** | Loop counter/tracker | `for token in` |
| **range()** | Number sequence generator | `range(1, 11)` |
| **Start** | First value (inclusive) | `range(1, ...)` |
| **End** | Last value (exclusive) | `range(..., 11)` |
| **Step** | Increment size | `range(0, 10, 2)` |
| **Iteration** | One execution of loop body | Each pass through |

## 📊 Flowchart

```
Start
  ↓
Initialize counter = 1
  ↓
Is counter ≤ 10?
  ├─ YES → Execute loop body
  │         Print token #
  │         counter++
  │         Go back to condition check
  └─ NO → End loop
  ↓
End
```

## 🚀 How to Run

```bash
python basic_for_loops.py
```

**Expected Output:**
```
=== Tea Token Dispenser ===
Serving chai with token #1
Serving chai with token #2
...
Serving chai with token #10

=== Tea Batch Processor ===
Batch 1 is being prepared...
...
Batch 4 is being prepared...

=== Multiplication Table ===
5 x 1 = 5
5 x 2 = 10
...
5 x 10 = 50
```

## 💻 Try It Yourself

**Modify the code to:**

1. Change token range (e.g., 1-20)
2. Create countdown (10, 9, 8, ...)
3. Print only even numbers
4. Generate different multiplication tables
5. Create a nested loop for a pattern

## ⚠️ Common Mistakes

### ❌ Off-by-One Error
```python
# WRONG - range(10) is 0-9, not 1-10
for i in range(10):
    print(i)  # Prints 0-9, not 1-10

# CORRECT
for i in range(1, 11):
    print(i)  # Prints 1-10
```

### ❌ Forgetting Loop Body Indentation
```python
# WRONG
for i in range(5):
print(i)  # Error: expected indented block

# CORRECT
for i in range(5):
    print(i)  # Properly indented
```

### ❌ Modifying Loop Variable
```python
# WRONG - Changes don't affect loop
for i in range(5):
    i = i * 2  # This doesn't skip iterations!
    print(i)

# If you need to skip: use conditional
for i in range(5):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i)
```

### ❌ Confusing range() Parameters
```python
# WRONG - Forgot step affects all
for i in range(1, 10, 2):
    print(i)  # 1, 3, 5, 7, 9 - correct!

# WRONG - Wrong order
for i in range(10, 1):
    print(i)  # No output! Needs negative step

# CORRECT
for i in range(10, 1, -1):
    print(i)  # 10, 9, 8, ..., 2
```

## 📝 Extended Examples

### Example 1: Multiplication Table Function
```python
def multiplication_table(number: int) -> list[str]:
    result = []
    for i in range(1, 11):
        result.append(f"{number} x {i} = {number * i}")
    return result

# Test
table = multiplication_table(7)
for line in table:
    print(line)
```

### Example 2: Number Patterns
```python
# Print triangle pattern
for row in range(1, 6):
    for col in range(row):
        print("*", end=" ")
    print()
# Output:
# *
# * *
# * * *
# * * * *
# * * * * *
```

### Example 3: Sum of Numbers
```python
def sum_range(n: int) -> int:
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

print(sum_range(100))  # 5050
```

### Example 4: Countdown Timer
```python
def countdown(seconds: int):
    for i in range(seconds, 0, -1):  # Countdown
        print(f"{i} seconds left...")
    print("Time's up!")

countdown(5)
```

### Example 5: Generate List
```python
# Create list of squares
squares = []
for i in range(1, 6):
    squares.append(i ** 2)
print(squares)  # [1, 4, 9, 16, 25]
```

## 🔄 Real-World Applications

- ✅ Generate ID numbers or tokens
- ✅ Process batches of data
- ✅ Create lookup tables (multiplication, conversion)
- ✅ Generate test data
- ✅ Repeat actions N times
- ✅ Create ASCII art or patterns
- ✅ Initialize arrays/lists

## 📊 Range Function Deep Dive

### Single Parameter
```python
range(5)  # 0, 1, 2, 3, 4 (0 to 4)
```

### Two Parameters
```python
range(2, 7)  # 2, 3, 4, 5, 6 (start=2, stop=7)
```

### Three Parameters
```python
range(0, 10, 2)  # 0, 2, 4, 6, 8 (start, stop, step)
```

### Negative Step
```python
range(10, 0, -1)  # 10, 9, 8, ..., 1 (counting down)
```

### Using with len()
```python
items = ["a", "b", "c"]
for i in range(len(items)):
    print(f"{i}: {items[i]}")
# Note: Prefer enumerate() for this pattern
```

## 💡 Pro Tips

1. **Use meaningful variable names**
   - `for token in range(1, 11):` (good)
   - `for x in range(1, 11):` (bad)

2. **range() creates a sequence, not a list**
   - It's memory-efficient
   - `list(range(5))` converts to list if needed

3. **Combine with conditions**
   ```python
   for i in range(1, 11):
       if i % 2 == 0:
           print(f"{i} is even")
   ```

4. **Use loop variable meaningfully**
   ```python
   # Good - variable name indicates purpose
   for batch_number in range(1, 5):
       process_batch(batch_number)
   ```

## 🎯 Next Steps

- [ ] Run the program
- [ ] Modify range values and observe output
- [ ] Create multiplication table for different numbers
- [ ] Create nested loops (loop within loop)
- [ ] Experiment with negative steps (countdown)
- [ ] Learn about for loops with lists

## 📚 Related Concepts

- **Nested For Loops:** Loops inside loops
- **For-In Loops:** Iterate through lists
- **Enumerate:** Get both index and value
- **Range Function:** Python's number generator

---

**Difficulty Level:** ⭐ (Beginner)  
**Time to Complete:** 10-15 minutes  
**Prerequisites:** Basic Python syntax, variables
