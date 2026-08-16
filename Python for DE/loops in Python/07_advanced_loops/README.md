# Project 7: Advanced Loop Patterns

## 📋 Project Description

Covers advanced loop patterns including dictionary iteration, efficient discount calculations, and the walrus operator (`:=`). Demonstrates how to write clean, Pythonic code.

## 🎯 Learning Objective

Master advanced loop techniques including dictionaries, walrus operator, and replace-if-elif chains with elegant lookup patterns.

## 💡 Concept Breakdown

### Dictionary in Loops

**Iterating Keys:**
```python
for key in dictionary:
    value = dictionary[key]
```

**Iterating Values:**
```python
for value in dictionary.values():
    print(value)
```

**Iterating Key-Value Pairs:**
```python
for key, value in dictionary.items():
    print(f"{key}: {value}")
```

### Walrus Operator (:=) - Python 3.8+

Assign a value while using it in a condition:
```python
if (x := compute()) > 0:
    print(f"Value: {x}")
```

**Benefits:**
- Avoid computing same value twice
- More concise code
- Clear intent

## 🔑 Key Concepts

| Concept | Explanation | Example |
|---------|-------------|---------|
| **Dictionary** | Key-value mapping | `{"gold": 0.20}` |
| **items()** | Get key-value pairs | `dict.items()` |
| **values()** | Get all values | `dict.values()` |
| **Walrus** | Assign in condition | `if (x := 5):` |
| **Lookup** | Find value by key | `dict.get(key)` |

## 📊 Dictionary vs If-Elif

### Bad: Many If-Elif Statements
```python
if customer_type == "gold":
    discount = 0.20
elif customer_type == "silver":
    discount = 0.15
elif customer_type == "bronze":
    discount = 0.10
else:
    discount = 0.05
```

**Problems:**
- Repetitive
- Hard to maintain
- Scales poorly

### Good: Dictionary Lookup
```python
discounts = {
    "gold": 0.20,
    "silver": 0.15,
    "bronze": 0.10,
}
discount = discounts.get(customer_type, 0.05)
```

**Advantages:**
- Clean and concise
- Easy to maintain
- Scales well

## 🚀 How to Run

```bash
python advanced_loops.py
```

## 💻 Try It Yourself

1. Create complex discount systems
2. Process nested data structures
3. Use walrus operator creatively
4. Build efficient lookup tables
5. Combine patterns creatively

## ⚠️ Common Mistakes

### ❌ Wrong Dictionary Iteration
```python
# WRONG - Iterates keys only
for item in dictionary:
    print(item)  # Prints keys only

# CORRECT - If you need values
for value in dictionary.values():
    print(value)

# CORRECT - If you need both
for key, value in dictionary.items():
    print(f"{key}: {value}")
```

### ❌ Walrus in Wrong Context
```python
# WRONG - Walrus doesn't work this way
x := 5  # Syntax error! Must be in expression

# CORRECT - In condition
if (x := compute()) > 0:
    print(x)

# CORRECT - In while condition
while (line := input()) != "quit":
    process(line)
```

### ❌ Missing Dictionary Default
```python
# WRONG - KeyError if key not found
discount = discounts[customer_type]

# CORRECT - Use get() with default
discount = discounts.get(customer_type, 0.05)
```

## 📝 Extended Examples

### Example 1: Discount Calculator
```python
def calculate_discount(users: list[dict]) -> list[dict]:
    discount_rates = {
        "gold": 0.20,
        "silver": 0.15,
        "bronze": 0.10,
    }
    
    result = []
    for user in users:
        rate = discount_rates.get(user["type"], 0.05)
        discount = user["amount"] * rate
        user["discount"] = discount
        result.append(user)
    return result

users = [
    {"type": "gold", "amount": 1000},
    {"type": "silver", "amount": 500},
    {"type": "unknown", "amount": 100},
]

discounts = calculate_discount(users)
for user in discounts:
    print(f"{user['type']}: {user['discount']}")
```

### Example 2: Nested Dictionary Iteration
```python
shop = {
    "beverages": {
        "chai": 50,
        "coffee": 80,
        "tea": 40
    },
    "snacks": {
        "samosa": 20,
        "cookie": 15
    }
}

for category, items in shop.items():
    print(f"\n{category.upper()}:")
    for item, price in items.items():
        print(f"  {item}: Rs {price}")
```

### Example 3: Walrus Operator
```python
def validate_password():
    while (password := input("Enter password: ")) != "":
        if (pwd_length := len(password)) < 8:
            print(f"Too short ({pwd_length} chars)")
        else:
            return password

pwd = validate_password()
print(f"Password set: {pwd}")
```

### Example 4: Count Occurrences
```python
def count_items(items: list[str]) -> dict:
    counts = {}
    for item in items:
        counts[item] = counts.get(item, 0) + 1
    return counts

items = ["apple", "banana", "apple", "cherry"]
print(count_items(items))
# {'apple': 2, 'banana': 1, 'cherry': 1}
```

### Example 5: Group by Category
```python
def group_numbers(numbers: list[int]) -> dict:
    groups = {"even": [], "odd": []}
    for num in numbers:
        if num % 2 == 0:
            groups["even"].append(num)
        else:
            groups["odd"].append(num)
    return groups

nums = [1, 2, 3, 4, 5, 6]
print(group_numbers(nums))
# {'even': [2, 4, 6], 'odd': [1, 3, 5]}
```

## 🔄 Real-World Applications

- ✅ Configuration management
- ✅ Discount/pricing systems
- ✅ Status mappings
- ✅ Error code lookups
- ✅ Feature flags
- ✅ Data categorization
- ✅ Frequency counting

## 📊 Pattern Comparison

### Pattern 1: If-Elif (Old Style)
```python
if status == "active":
    result = "Running"
elif status == "paused":
    result = "Paused"
elif status == "stopped":
    result = "Stopped"
```

### Pattern 2: Dictionary (Modern)
```python
status_map = {
    "active": "Running",
    "paused": "Paused",
    "stopped": "Stopped",
}
result = status_map.get(status, "Unknown")
```

**Modern approach is cleaner!**

## 💡 Pro Tips

1. **Use .get() for safe lookups**
   ```python
   # Safe - provides default
   value = dictionary.get(key, default_value)
   
   # Risky - KeyError if not found
   value = dictionary[key]
   ```

2. **Dictionary for multiple conditions**
   ```python
   # Good: Clean mapping
   type_map = {
       "admin": ["read", "write", "delete"],
       "user": ["read"],
       "guest": [],
   }
   
   # Bad: Many if-elif statements
   ```

3. **Use walrus for validation**
   ```python
   # Compute once, use in condition
   if (result := expensive_computation()) > threshold:
       process(result)  # Reuse result
   ```

4. **Nest dictionaries for complexity**
   ```python
   config = {
       "database": {
           "host": "localhost",
           "port": 5432,
       },
       "cache": {
           "host": "localhost",
           "port": 6379,
       }
   }
   ```

## 🎯 Next Steps

- [ ] Run the program
- [ ] Build discount calculator
- [ ] Create nested dictionaries
- [ ] Use walrus operator
- [ ] Replace if-elif with dictionaries
- [ ] Optimize with lookups

## 📚 Related Concepts

- **Dictionaries:** Key-value storage
- **List Comprehension:** Alternative iteration
- **Lambda Functions:** Inline functions
- **Generators:** Memory-efficient loops

---

## 📖 Walrus Operator Reference

**Introduced:** Python 3.8  
**Purpose:** Assign and use value in same expression  
**Syntax:** `(variable := expression)`

### Common Uses:
```python
# In conditions
if (x := compute()) > 0:
    use(x)

# In while loops
while (line := file.readline()) != "":
    process(line)

# In list comprehensions
[y for x in data if (y := transform(x)) is not None]
```

---

**Difficulty Level:** ⭐⭐⭐ (Intermediate-Advanced)  
**Time to Complete:** 25-35 minutes  
**Prerequisites:** All previous loop concepts, dictionaries
