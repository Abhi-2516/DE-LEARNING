# Project 3: Tea Stall Pricing

## 📋 Project Description

A dynamic tea pricing system that demonstrates the **if-elif-else** statement, which handles multiple mutually exclusive conditions.

## 🎯 Learning Objective

Learn how to handle multiple different options using if-elif-else chains and understand when to use elif instead of nested ifs.

## 💡 Concept Breakdown

### If-Elif-Else Syntax

```python
if condition1:
    # Execute if condition1 is True
elif condition2:
    # Execute if condition2 is True (and condition1 was False)
elif condition3:
    # Execute if condition3 is True
else:
    # Execute if none of the above conditions were True
```

### Key Points

1. **Only the first matching condition executes**
2. Once a condition is `True`, the rest are skipped
3. `elif` = "else if" (check another condition)
4. The `else` clause is optional but recommended

### Project Example

```python
cup_type = input("Enter your cup type (small/medium/large): ").lower()

if cup_type == "small":
    print("Price is: $10")
elif cup_type == "medium":
    print("Price is: $15")
elif cup_type == "large":
    print("Price is: $20")
else:
    print("Unknown cup size. Please choose from small, medium, or large.")
```

## 📊 Flowchart

```
Start
  ↓
Get cup size from user
  ↓
Is it "small"?
  ├─ YES → Price = $10
  └─ NO  → Is it "medium"?
            ├─ YES → Price = $15
            └─ NO  → Is it "large"?
                      ├─ YES → Price = $20
                      └─ NO  → Price = Unknown
  ↓
Display price
  ↓
End
```

## 🔑 Key Concepts

| Concept | Explanation | Example |
|---------|-------------|---------|
| **if** | First condition to check | `if cup_type == "small":` |
| **elif** | Additional condition if previous was False | `elif cup_type == "medium":` |
| **else** | Default case if all above are False | `else:` |
| **Mutual Exclusivity** | Only one block executes | Once matched, skip rest |

## 🚀 How to Run

```bash
python tea_stall_pricing.py
```

**Sample Interaction:**
```
Enter your cup type (small/medium/large): medium
Price is: $15
```

## 💻 Try It Yourself

**Modify the code to:**
1. Add more cup sizes (extra-small, extra-large)
2. Add sugar level options
3. Add milk type options
4. Calculate total cost with tax
5. Apply discounts for bulk orders

## ⚠️ Common Mistakes

### ❌ Forgetting to Use `elif`
```python
# WRONG - Checks all conditions, inefficient and wrong logic
if cup_type == "small":
    print("$10")
if cup_type == "medium":  # ← Should be elif!
    print("$15")
if cup_type == "large":
    print("$20")
```

**Problem:** The code checks every condition even after finding a match.

### ✅ Correct Approach
```python
if cup_type == "small":
    print("$10")
elif cup_type == "medium":  # ← Only checked if above is False
    print("$15")
elif cup_type == "large":
    print("$20")
```

### ❌ Missing else Clause
```python
if cup_type == "small":
    print("$10")
elif cup_type == "medium":
    print("$15")
# ← What if user enters "extra-large"? No output!
```

### ✅ Better Practice
```python
if cup_type == "small":
    print("$10")
elif cup_type == "medium":
    print("$15")
else:
    print("Size not available.")  # Handles unexpected input
```

## 📝 Extended Examples

### Example 1: Grade Assignment
```python
score = int(input("Enter your score: "))

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

print(f"Your grade: {grade}")
```

### Example 2: Traffic Light System
```python
light_color = input("Enter light color: ").lower()

if light_color == "red":
    action = "STOP"
elif light_color == "yellow":
    action = "WAIT"
elif light_color == "green":
    action = "GO"
else:
    action = "INVALID"

print(f"Action: {action}")
```

### Example 3: Enhanced Tea Stall with Extras
```python
cup_type = input("Enter cup type: ").lower()
add_sugar = input("Add sugar? (yes/no): ").lower()

if cup_type == "small":
    price = 10
elif cup_type == "medium":
    price = 15
elif cup_type == "large":
    price = 20
else:
    print("Invalid size!")
    exit()

if add_sugar == "yes":
    price += 2

print(f"Total Price: ${price}")
```

### Example 4: Age-Based Access
```python
age = int(input("Enter your age: "))

if age < 13:
    category = "Child"
elif age < 18:
    category = "Teen"
elif age < 65:
    category = "Adult"
else:
    category = "Senior"

print(f"Category: {category}")
```

## 📊 If-Elif-Else vs Nested If

### ❌ Using Nested If (Bad)
```python
if cup_type == "small":
    print("$10")
else:
    if cup_type == "medium":
        print("$15")
    else:
        if cup_type == "large":
            print("$20")
```

**Problems:**
- Hard to read (deeply nested)
- Error-prone
- Inefficient

### ✅ Using If-Elif-Else (Good)
```python
if cup_type == "small":
    print("$10")
elif cup_type == "medium":
    print("$15")
elif cup_type == "large":
    print("$20")
```

**Advantages:**
- Clean and readable
- Easy to maintain
- Efficient

## 🎯 Order of Conditions

**Important:** Order conditions from **most specific to most general**

```python
# WRONG - General condition first blocks specific ones
if age >= 0:
    print("Anyone")
elif age >= 18:
    print("Adult")  # ← Never reaches here!

# CORRECT - Specific conditions first
if age >= 18:
    print("Adult")
elif age >= 0:
    print("Anyone")  # ← Can reach this
```

## 🔄 Real-World Applications

- ✅ E-commerce sizing system (XS, S, M, L, XL)
- ✅ Temperature ranges (cold, cool, warm, hot)
- ✅ Customer support tiers (bronze, silver, gold, platinum)
- ✅ Speed zones (residential, highway, school)
- ✅ Product categories (food, electronics, clothing)

## 📊 Decision Guide

**Use if-elif-else when:**
- You have multiple mutually exclusive options
- Each condition is different (not same variable compared)
- You need a default case

**DON'T use if-elif-else when:**
- You have deeply nested logic (use separate functions)
- You need to check all conditions (use multiple ifs)

## 🎯 Next Steps

- [ ] Run the program with different inputs
- [ ] Add more cup sizes
- [ ] Add extras (sugar, milk, spice)
- [ ] Calculate totals
- [ ] Create nested conditions for extras
- [ ] Learn about match-case for large option sets

## 📚 Related Concepts

- **Nested If:** If statements inside other if statements
- **Logical Operators:** Combine conditions with `and`, `or`
- **Match-Case:** Modern alternative for multiple options
- **Input Validation:** Checking user input validity

## 💡 Pro Tips

1. **Always include an `else` clause** to handle unexpected inputs
2. **Use `.lower()` or `.upper()`** for case-insensitive comparisons
3. **Order conditions logically** (most common first for performance)
4. **Keep conditions simple** and readable
5. **Test edge cases** (boundary values, invalid input)

---

**Difficulty Level:** ⭐⭐ (Beginner-Intermediate)  
**Time to Complete:** 20-30 minutes  
**Prerequisites:** Basic if-else, logical thinking
