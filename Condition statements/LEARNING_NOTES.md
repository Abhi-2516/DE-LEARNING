# Conditional Statements in Python - Learning Notes

## 📚 Overview
This module covers all fundamental conditional statements in Python, from basic if-else to advanced pattern matching with match-case.

---

## 🎯 Topics Covered

### 1. **Basic If-Else Statement**
**File:** `01_notification_system/notification_system.py`

**Concept:** Simple true/false decision making
```python
if condition:
    # Execute if condition is True
else:
    # Execute if condition is False
```

**Real-world Example:** Kettle boiling notification
- **Use Case:** When you need to execute different code based on a simple boolean condition
- **Key Learning:** The most fundamental control flow structure

---

### 2. **If-Else with Logical Operators**
**File:** `02_snack_system/snack_system.py`

**Concept:** Combining multiple conditions using `or`, `and`, `not`
```python
if condition1 or condition2:
    # Execute if either condition is True
    
if condition1 and condition2:
    # Execute only if both conditions are True
    
if not condition:
    # Execute if condition is False
```

**Real-world Example:** Snack availability checker
- **Use Case:** When you need to check multiple conditions simultaneously
- **Key Learning:** Logical operators allow flexible condition checking
- **Common Mistakes:**
  - Using `or snack == "cookies"` instead of `snack == "cookies" or snack == "samosa"`
  - Confusing `and` with `or`

---

### 3. **If-Elif-Else Statement**
**File:** `03_tea_stall_pricing/tea_stall_pricing.py`

**Concept:** Checking multiple conditions in sequence
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

**Real-world Example:** Tea stall pricing system
- **Use Case:** When you have multiple mutually exclusive options
- **Key Learning:** 
  - Only the first matching condition executes
  - Use `elif` for multiple exclusive choices
  - Always include `else` for unexpected inputs
- **Best Practice:** Order conditions from most specific to most general

---

### 4. **Nested If Statements**
**File:** `04_smart_thermostat/smart_thermostat.py`

**Concept:** If statements inside other if statements
```python
if outer_condition:
    if inner_condition:
        # Execute if both conditions are True
```

**Real-world Example:** Smart thermostat monitoring
- **Use Case:** When you need to check conditions hierarchically or have dependencies
- **Key Learning:**
  - Useful for dependent conditions
  - Improves code readability when conditions are related
  - Indentation is critical in Python
- **Common Mistakes:**
  - Indentation errors
  - Forgetting that nested conditions must all be true

---

### 5. **Ternary/Conditional Expression**
**File:** `05_delivery_fees_calculator/delivery_fees_calculator.py`

**Concept:** One-line conditional assignment
```python
value = value_if_true if condition else value_if_false
```

**Real-world Example:** Delivery fee calculator
- **Use Case:** Simple conditional value assignment in one line
- **Key Learning:**
  - Compact and readable for simple conditions
  - Cannot replace complex if-elif-else logic
  - Improves code conciseness
- **When to Use:**
  - Simple true/false decisions
  - Quick variable assignment based on condition
- **When NOT to Use:**
  - Multiple conditions (use if-elif-else instead)
  - Complex logic

---

### 6. **Match-Case Statement (Pattern Matching)**
**File:** `06_train_seat_booking/train_seat_booking.py`

**Concept:** Structural pattern matching (Python 3.10+)
```python
match value:
    case pattern1:
        # Execute if value matches pattern1
    case pattern2:
        # Execute if value matches pattern2
    case _:
        # Default case (underscore represents any value)
```

**Real-world Example:** Train seat booking system
- **Use Case:** When you have many specific values to match
- **Key Learning:**
  - Modern replacement for long if-elif-else chains
  - More readable and Pythonic for multiple options
  - Requires Python 3.10 or higher
  - The `_` (underscore) is the default case
- **Advantages over if-elif-else:**
  - Cleaner syntax for multiple equality checks
  - Better performance for many cases
  - More expressive intent

---

## 📊 Decision Tree: Which Statement to Use?

```
Do you need to check a condition?
│
├─ Is it a simple True/False? 
│  └─ Use: if-else
│
├─ Do you have multiple different values to match?
│  ├─ Python 3.10+? → Use: match-case
│  └─ Earlier Python? → Use: if-elif-else
│
├─ Do you have multiple conditions with AND/OR?
│  └─ Use: if with logical operators (or, and, not)
│
├─ Do you have nested dependencies?
│  └─ Use: nested if statements
│
└─ Need a quick one-line conditional value?
   └─ Use: ternary operator (conditional expression)
```

---

## 🔑 Key Concepts Summary

| Concept | Syntax | Use Case |
|---------|--------|----------|
| If-Else | `if cond: ... else: ...` | Simple boolean decision |
| If-Elif-Else | `if c1: ... elif c2: ... else: ...` | Multiple exclusive options |
| Logical Operators | `and`, `or`, `not` | Combine conditions |
| Nested If | If inside if | Dependent conditions |
| Ternary | `val if cond else val2` | One-line assignment |
| Match-Case | `match val: case x: ...` | Multiple value matching (3.10+) |

---

## ⚠️ Common Mistakes & How to Avoid Them

### 1. **Forgetting Colons**
```python
# ❌ Wrong
if x > 5
    print("x is greater than 5")

# ✅ Correct
if x > 5:
    print("x is greater than 5")
```

### 2. **Indentation Errors**
```python
# ❌ Wrong
if condition:
print("This will cause IndentationError")

# ✅ Correct
if condition:
    print("Properly indented")
```

### 3. **Assignment vs. Comparison**
```python
# ❌ Wrong (assignment, not comparison)
if x = 5:
    print("x is 5")

# ✅ Correct (comparison)
if x == 5:
    print("x is 5")
```

### 4. **Logical Operator Confusion**
```python
# ❌ Wrong
if snack == "cookies" or "samosa":
    # This always evaluates to True because "samosa" is truthy!

# ✅ Correct
if snack == "cookies" or snack == "samosa":
    print("Valid snack")
```

### 5. **Case Sensitivity**
```python
# ❌ Wrong
if name == "Alice":
    # Won't match if user enters "alice"

# ✅ Correct
if name.lower() == "alice":
    # Works with any case variation
```

---

## 💡 Best Practices

1. **Keep conditions simple and readable**
   - Break complex conditions into multiple lines
   - Use meaningful variable names

2. **Always include error handling**
   - Use `else` clause to handle unexpected inputs
   - Don't assume valid input

3. **Order conditions logically**
   - Most specific conditions first
   - Most common cases first for performance

4. **Use appropriate statement type**
   - Don't use match-case for complex logic
   - Keep nested ifs to 2-3 levels maximum

5. **Test edge cases**
   - Boundary values
   - Empty/null values
   - Invalid inputs

---

## 📝 Practice Exercises

1. **Modify the snack system** to accept multiple snacks
2. **Extend the tea stall** with sizes (small, medium, large) and extras
3. **Enhance the thermostat** with temperature ranges (cold, normal, warm, hot)
4. **Add discounts** to the delivery calculator based on order amount tiers
5. **Create a student grading system** using if-elif-else
6. **Build a login system** combining multiple conditions

---
