# Project 6: Loop Control Statements

## 📋 Project Description

Demonstrates how to control loop flow using `break` and `continue` statements. Includes menu selection and search examples.

## 🎯 Learning Objective

Learn to exit loops early with `break` and skip iterations with `continue` for more flexible loop control.

## 💡 Concept Breakdown

### Break Statement

```python
for item in items:
    if item == target:
        break  # Exit loop immediately
```

**Purpose:** Stop loop execution completely

### Continue Statement

```python
for item in items:
    if item.is_invalid():
        continue  # Skip to next iteration
    process(item)
```

**Purpose:** Skip current iteration and move to next

## 🔑 Key Concepts

| Statement | Effect | Use Case | Example |
|-----------|--------|----------|---------|
| `break` | Exit loop completely | Found target | `if found: break` |
| `continue` | Skip this iteration | Skip invalid | `if invalid: continue` |
| (none) | Execute normally | Process item | `process(item)` |

## 📊 Flowchart

### Break
```
Loop starts
    ↓
Iteration
    ├─ Found target? → break → Loop ends
    └─ Continue → Next iteration
```

### Continue
```
Loop starts
    ↓
Iteration
    ├─ Skip condition? → continue → Next iteration
    └─ Process → Next iteration
```

## 🚀 How to Run

```bash
python loop_control.py
```

## 💻 Try It Yourself

1. Create early exit scenarios
2. Filter invalid data
3. Search with early stopping
4. Skip specific items
5. Build nested loops with control

## ⚠️ Common Mistakes

### ❌ Break in Nested Loop Only Exits Inner Loop
```python
# WRONG - break only exits inner loop
found = False
for i in range(3):
    for j in range(3):
        if i == 1 and j == 1:
            found = True
            break  # Only breaks inner loop!
    if found:
        break  # Must add this to break outer

# CORRECT - Use function for clean exit
def search():
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                return True
    return False

if search():
    print("Found!")
```

### ❌ Confusing Continue with Break
```python
# WRONG - continue skips, doesn't exit
items = [1, 2, 3, 4, 5]
for item in items:
    if item == 3:
        continue  # Skips 3, continues with 4, 5
    print(item)
# Output: 1 2 4 5

# CORRECT - use break to exit
for item in items:
    if item == 3:
        break  # Exits completely
    print(item)
# Output: 1 2
```

### ❌ Unnecessary Continue
```python
# WRONG - unnecessary continue
for item in items:
    if valid(item):
        continue  # Skips nothing
    process(item)

# CORRECT - use logic inversion
for item in items:
    if not valid(item):
        process(item)
```

## 📝 Extended Examples

### Example 1: Search and Exit
```python
def find_in_list(items: list[int], target: int) -> int:
    for idx, item in enumerate(items):
        if item == target:
            return idx  # Found!
    return -1  # Not found

print(find_in_list([10, 20, 30, 40], 30))  # 2
```

### Example 2: Skip Invalid Items
```python
def process_valid_only(items: list[int]):
    for item in items:
        if item < 0:
            continue  # Skip negative
        print(f"Processing: {item}")

process_valid_only([1, -2, 3, -4, 5])
# Output: Processing: 1, 3, 5
```

### Example 3: Filter List
```python
def filter_duplicates(items: list[str]) -> list[str]:
    result = []
    for item in items:
        if item in result:
            continue  # Skip duplicates
        result.append(item)
    return result

print(filter_duplicates(["a", "b", "a", "c"]))
# ['a', 'b', 'c']
```

### Example 4: Nested with Break
```python
def find_pattern(grid: list[list[int]], target: int) -> bool:
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == target:
                return True  # Found!
    return False

grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(find_pattern(grid, 5))  # True
```

## 🔄 Real-World Applications

- ✅ Search algorithms (exit when found)
- ✅ Data validation (skip invalid)
- ✅ Filtering lists
- ✅ Error recovery
- ✅ Menu systems
- ✅ Game loops
- ✅ Early termination

## 📊 Continue vs If Not Pattern

### Using Continue
```python
for item in items:
    if item.is_invalid():
        continue
    process(item)
```

### Using If Not
```python
for item in items:
    if not item.is_invalid():
        process(item)
```

Both are valid; choose what's clearer in context.

## 💡 Pro Tips

1. **Prefer early returns in functions**
   ```python
   # Good - clear and avoids nesting
   def search(items, target):
       for item in items:
           if item == target:
               return True
       return False
   
   # Avoid - nested breaks
   found = False
   for item in items:
       if item == target:
           break
   ```

2. **Use flags for nested loop breaks**
   ```python
   found = False
   for i in range(10):
       if found:
           break
       for j in range(10):
           if grid[i][j] == target:
               found = True
               break
   ```

3. **Combine with conditions**
   ```python
   # Skip and process pattern
   for item in items:
       if skip_condition(item):
           continue
       if stop_condition(item):
           break
       process(item)
   ```

4. **Avoid over-using**
   ```python
   # Too many control statements = hard to read
   for item in items:
       if condition1:
           continue
       if condition2:
           break
       if condition3:
           continue
   
   # Better - refactor to function
   if should_process(items):
       for item in items:
           process(item)
   ```

## 🎯 Next Steps

- [ ] Run the program
- [ ] Create search functions with break
- [ ] Build filters with continue
- [ ] Handle nested loops with break
- [ ] Learn about advanced patterns

## 📚 Related Concepts

- **For Loops:** Basic iteration
- **While Loops:** Condition-based loops
- **Functions:** Cleaner alternative to break
- **Exceptions:** Error handling alternative

---

**Difficulty Level:** ⭐⭐⭐ (Intermediate)  
**Time to Complete:** 20-25 minutes  
**Prerequisites:** For/while loops, conditionals
