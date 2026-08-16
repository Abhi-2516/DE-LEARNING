# Project 4: Zip Function

## 📋 Project Description

Demonstrates the `zip()` function to pair elements from multiple lists simultaneously. Includes order summaries and student score reports.

## 🎯 Learning Objective

Learn to combine multiple lists by pairing elements at the same position using the `zip()` function.

## 💡 Concept Breakdown

### Zip Syntax

```python
for elem1, elem2, elem3 in zip(list1, list2, list3):
    # elem1: element from list1
    # elem2: element from list2
    # elem3: element from list3
```

### Key Points

```python
names = ["Alice", "Bob"]
scores = [95, 87]

# Without zip (manual indexing)
for i in range(len(names)):
    print(f"{names[i]}: {scores[i]}")

# With zip (elegant)
for name, score in zip(names, scores):
    print(f"{name}: {score}")
```

## 🔑 Key Concepts

| Concept | Explanation | Example |
|---------|-------------|---------|
| **Pairing** | Matching elements by position | Names matched with scores |
| **Parallel** | Process multiple lists together | Simultaneous iteration |
| **Stop** | Stops at shortest list | Unmatched items ignored |
| **Unpack** | Extract paired elements | `name, score in zip()` |

## 📊 How Zip Works

```
names:   ["Alice", "Bob", "Charlie"]
scores:  [95, 87, 92]

zip produces:
("Alice", 95)
("Bob", 87)
("Charlie", 92)
```

### With Different Lengths
```
names:   ["Alice", "Bob", "Charlie"]
scores:  [95, 87]  # Shorter list

zip stops at shortest:
("Alice", 95)
("Bob", 87)
# Charlie is ignored!
```

## 🚀 How to Run

```bash
python zip_function.py
```

## 💻 Try It Yourself

1. Pair cities with temperatures
2. Match products with quantities
3. Create name-email pairs
4. Build Q&A pairs

## ⚠️ Common Mistakes

### ❌ Forgetting Different Lengths
```python
# WRONG - Assumes same length
names = ["Alice", "Bob"]
scores = [95, 87, 92, 78]  # Extra elements!

for name, score in zip(names, scores):
    print(f"{name}: {score}")
# Missing: 92, 78 are ignored!

# SOLUTION: Check lengths first
if len(names) != len(scores):
    print("Warning: Lists have different lengths")
```

### ❌ Wrong Unpacking
```python
# WRONG - Trying to unpack into single variable
for pair in zip(names, scores):
    print(pair)  # Prints tuple: ('Alice', 95)

# CORRECT - Unpack properly
for name, score in zip(names, scores):
    print(f"{name}: {score}")
```

### ❌ Modifying While Zipping
```python
# WRONG - Can't modify original lists while zipping
for name, score in zip(names, scores):
    names.remove(name)  # Dangerous!

# CORRECT - Create copies or modify after
zipped = list(zip(names, scores))
for name, score in zipped:
    # Now safe to modify
```

## 📝 Extended Examples

### Example 1: Create Dictionary
```python
def create_score_dict(names: list[str], scores: list[int]) -> dict:
    return {name: score for name, score in zip(names, scores)}

names = ["Alice", "Bob", "Charlie"]
scores = [95, 87, 92]
scores_dict = create_score_dict(names, scores)
print(scores_dict)
# {'Alice': 95, 'Bob': 87, 'Charlie': 92}
```

### Example 2: Create List of Tuples
```python
def pair_elements(list1: list, list2: list) -> list[tuple]:
    return list(zip(list1, list2))

products = ["Chai", "Coffee", "Tea"]
prices = [50, 80, 40]
pairs = pair_elements(products, prices)
print(pairs)
# [('Chai', 50), ('Coffee', 80), ('Tea', 40)]
```

### Example 3: Multiple Lists
```python
users = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 28]
cities = ["NYC", "LA", "Chicago"]

for user, age, city in zip(users, ages, cities):
    print(f"{user} ({age}) lives in {city}")
```

### Example 4: With Enumerate
```python
names = ["Alice", "Bob", "Charlie"]
scores = [95, 87, 92]

for idx, (name, score) in enumerate(zip(names, scores), start=1):
    print(f"{idx}. {name}: {score}")
# Output:
# 1. Alice: 95
# 2. Bob: 87
# 3. Charlie: 92
```

## 🔄 Real-World Applications

- ✅ Pair names with IDs
- ✅ Match products with prices
- ✅ Combine questions with answers
- ✅ Correlate dates with values
- ✅ Link employees with salaries
- ✅ Associate cities with temperatures
- ✅ Create lookup tables

## 📊 Zip with Different Lengths

### Default Behavior (Stops at Shortest)
```python
names = ["Alice", "Bob", "Charlie"]
scores = [95, 87]

for name, score in zip(names, scores):
    print(name, score)
# Output: Alice 95, Bob 87
# Charlie is skipped!
```

### Using zip_longest()
```python
from itertools import zip_longest

for name, score in zip_longest(names, scores, fillvalue="N/A"):
    print(name, score)
# Output: Alice 95, Bob 87, Charlie N/A
```

## 💡 Pro Tips

1. **Check lengths before zipping**
   ```python
   if len(list1) != len(list2):
       print("Warning: Different lengths")
   ```

2. **Use meaningful variable names**
   ```python
   # Good
   for name, score in zip(names, scores):
       process(name, score)
   
   # Bad
   for x, y in zip(names, scores):
       process(x, y)
   ```

3. **Can zip multiple lists**
   ```python
   for a, b, c in zip(list1, list2, list3):
       process(a, b, c)
   ```

4. **Unzip with zip(*pairs)**
   ```python
   pairs = [('a', 1), ('b', 2), ('c', 3)]
   letters, numbers = zip(*pairs)
   print(letters)   # ('a', 'b', 'c')
   print(numbers)   # (1, 2, 3)
   ```

## 🎯 Next Steps

- [ ] Run the program
- [ ] Pair items from different lists
- [ ] Create dictionaries from zipped lists
- [ ] Handle lists of different lengths
- [ ] Combine zip with enumerate
- [ ] Learn about zip_longest

## 📚 Related Concepts

- **Enumerate:** Get index and value
- **Dictionary Creation:** Using zip to create dicts
- **Itertools:** Advanced iteration tools

---

**Difficulty Level:** ⭐⭐ (Beginner-Intermediate)  
**Time to Complete:** 15-20 minutes  
**Prerequisites:** For loops with lists, enumerate
