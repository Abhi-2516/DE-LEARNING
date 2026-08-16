# Project 2: Snack System

## 📋 Project Description

A restaurant snack ordering system that demonstrates how to use **logical operators** (`or`, `and`) to combine multiple conditions in a single if statement.

## 🎯 Learning Objective

Learn how to check multiple conditions using logical operators and make decisions based on combined criteria.

## 💡 Concept Breakdown

### Logical Operators

#### 1. **OR Operator** (`or`)
Returns `True` if **at least one** condition is `True`
```python
if condition1 or condition2:
    # Execute if either condition1 or condition2 (or both) is True
```

**Truth Table:**
| A | B | A or B |
|---|---|--------|
| T | T | T |
| T | F | T |
| F | T | T |
| F | F | F |

#### 2. **AND Operator** (`and`)
Returns `True` only if **all** conditions are `True`
```python
if condition1 and condition2:
    # Execute only if both conditions are True
```

**Truth Table:**
| A | B | A and B |
|---|---|---------|
| T | T | T |
| T | F | F |
| F | T | F |
| F | F | F |

#### 3. **NOT Operator** (`not`)
Returns the opposite of the condition
```python
if not condition:
    # Execute if condition is False
```

### Project Example

```python
snack = input("Enter your preferred snack: ").lower()

if snack == "cookies" or snack == "samosa":
    print("Best choice!")
else:
    print("No product available.")
```

## 🔑 Key Concepts

| Operator | Syntax | Meaning | Example |
|----------|--------|---------|---------|
| OR | `or` | At least one condition is True | `x > 5 or x < 2` |
| AND | `and` | All conditions are True | `x > 5 and x < 10` |
| NOT | `not` | Reverse the condition | `not x == 5` |

## 📊 Flowchart

```
Start
  ↓
User enters snack
  ↓
Is snack "cookies" OR "samosa"?
  ├─ YES → Print "Best choice!"
  └─ NO  → Print "No product available."
  ↓
End
```

## 🚀 How to Run

```bash
python snack_system.py
```

**Sample Interaction:**
```
Enter your preferred snack: cookies
User says: cookies
Best choice!
```

## 💻 Try It Yourself

**Modify the code to:**
1. Add more snack options (pizza, burger, samosa, cookies)
2. Add prices for each snack
3. Accept multiple snacks in one order
4. Add combinations (e.g., combo = samosa + chai)

## ⚠️ Common Mistakes

### ❌ Wrong Usage of `or`
```python
# WRONG - This always evaluates to True!
if snack == "cookies" or "samosa":
    print("Available")

# CORRECT - Check each value separately
if snack == "cookies" or snack == "samosa":
    print("Available")
```

**Why?** `"samosa"` is a non-empty string, which is always `True` in Python!

### ❌ Confusing `and` with `or`
```python
# WRONG - Both conditions must be true
if snack == "cookies" and snack == "samosa":  # Impossible!
    print("Available")

# CORRECT - Use or for multiple options
if snack == "cookies" or snack == "samosa":
    print("Available")
```

### ❌ Forgetting `.lower()`
```python
# Case-sensitive comparison (unreliable)
snack = input("Enter snack: ")
if snack == "cookies":  # Won't match "Cookies" or "COOKIES"

# Case-insensitive comparison (better)
snack = input("Enter snack: ").lower()
if snack == "cookies":  # Works for any case variation
```

## 📝 Extended Examples

### Example 1: Using AND
```python
age = int(input("Enter your age: "))
income = int(input("Enter your income: "))

if age >= 18 and income >= 5000:
    print("Eligible for loan!")
else:
    print("Not eligible.")
```

### Example 2: Using NOT
```python
discount_available = True

if not discount_available:
    print("No discount today.")
else:
    print("Get 10% discount!")
```

### Example 3: Combining Multiple Operators
```python
snack = "pizza"
price = 250
available = True

if (snack == "pizza" or snack == "burger") and price < 300 and available:
    print("Order confirmed!")
else:
    print("Cannot process order.")
```

### Example 4: Enhanced Snack System with Prices
```python
snack = input("Enter snack: ").lower()

if snack == "cookies":
    price = 50
    available = True
elif snack == "samosa":
    price = 20
    available = True
elif snack == "pizza":
    price = 300
    available = True
else:
    available = False

if available:
    print(f"Price: ${price}")
else:
    print("Not available.")
```

## 🎯 Operator Precedence

When combining operators, remember the order:
```
NOT > AND > OR
```

**Example:**
```python
if a or b and c:  # Evaluated as: a or (b and c)
```

If you want different precedence, use parentheses:
```python
if (a or b) and c:  # Different result!
```

## 🔄 Real-World Applications

- ✅ User authentication (username AND password correct)
- ✅ E-commerce filtering (size AND color match)
- ✅ Game logic (player has sword OR bow)
- ✅ Access control (admin OR owner can edit)
- ✅ Validation (email correct AND password strong)

## 📊 Decision Guide

**Use `or` when:**
- Multiple options are acceptable
- "Either this OR that" scenario

**Use `and` when:**
- Multiple conditions must ALL be true
- "This AND that" scenario

**Use `not` when:**
- You want the opposite result
- "NOT this" scenario

## 🎯 Next Steps

- [ ] Run the program with different inputs
- [ ] Add more snack options
- [ ] Create a pricing system
- [ ] Combine with `and` operator
- [ ] Learn about if-elif-else chains

## 📚 Related Concepts

- **If-Elif-Else:** Multiple conditions in sequence
- **Comparison Operators:** `==`, `!=`, `<`, `>`, etc.
- **Boolean Algebra:** Logic and truth tables
- **String Methods:** `.lower()`, `.upper()`, `.strip()`

---

**Difficulty Level:** ⭐⭐ (Beginner-Intermediate)  
**Time to Complete:** 15-20 minutes  
**Prerequisites:** Basic if-else, logical thinking
