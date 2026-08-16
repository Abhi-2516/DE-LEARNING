# Project 4: Smart Thermostat

## 📋 Project Description

An intelligent temperature monitoring system that demonstrates **nested if statements**, where conditions depend on previous conditions being true.

## 🎯 Learning Objective

Understand how to structure dependent conditions using nested if statements and when nested logic is appropriate.

## 💡 Concept Breakdown

### Nested If Syntax

```python
if outer_condition:
    if inner_condition:
        # Code only executes if BOTH conditions are True
    else:
        # Code executes if outer is True but inner is False
else:
    # Code executes if outer condition is False
```

### Key Points

1. **Inner if only evaluates if outer if is True**
2. **Both conditions must be True** for inner block to execute
3. **Indentation is critical** for defining nesting levels
4. Use nesting for **dependent conditions**

### Project Example

```python
device_status = 'active'
temp = 38

if device_status == 'active':
    if temp > 35:
        print("ALERT: Temperature is too high!")
    else:
        print("Normal temperature.")
else:
    print("Device is offline.")
```

## 📊 Flowchart

```
Start
  ↓
Is device status 'active'?
  ├─ YES → Is temperature > 35?
  │         ├─ YES → Print "ALERT"
  │         └─ NO  → Print "Normal"
  └─ NO  → Print "Device is offline"
  ↓
End
```

## 🔑 Key Concepts

| Concept | Explanation | Example |
|---------|-------------|---------|
| **Nested If** | If inside another if | `if a: if b:` |
| **Dependency** | Inner condition depends on outer | Device status → Temperature check |
| **Indentation** | Shows nesting levels (4 spaces) | Level 1, Level 2, Level 3 |
| **Scope** | Variables accessible within indentation | Local scope in Python |

## 🚀 How to Run

```bash
python smart_thermostat.py
```

**Sample Output:**
```
--- Auto Check ---
ALERT: Temperature is too high!

--- Interactive Check ---
Enter device status (active/offline): active
Enter current temperature: 28
Normal temperature.
```

## 💻 Try It Yourself

**Modify the code to:**
1. Add more temperature ranges (cold, normal, warm, hot)
2. Add humidity checking
3. Add automatic adjustment mode
4. Add alert history logging
5. Create a GUI interface

## ⚠️ Common Mistakes

### ❌ Indentation Error
```python
if device_status == 'active':
if temp > 35:  # ← Wrong! Not properly indented
    print("ALERT")
```

**Error:** `IndentationError: expected an indented block`

### ✅ Correct
```python
if device_status == 'active':
    if temp > 35:  # ← Properly indented (4 spaces)
        print("ALERT")
```

### ❌ Too Many Nesting Levels
```python
if a:
    if b:
        if c:
            if d:
                if e:  # ← Too deep! Hard to read
                    print("Finally!")
```

**Problem:** 
- Difficult to read and maintain
- Higher chance of errors
- "Arrow anti-pattern" (code looks like arrow)

### ✅ Better Approach
```python
# Combine conditions with 'and' instead
if a and b and c and d and e:
    print("All conditions met!")
```

### ❌ Using Nested If for Non-Dependent Conditions
```python
# WRONG - These aren't dependent
if age > 18:
    if income > 5000:
        print("Loan approved")
```

### ✅ Use 'and' for Independent Conditions
```python
# CORRECT - Use and for multiple independent conditions
if age > 18 and income > 5000:
    print("Loan approved")
```

## 📝 Extended Examples

### Example 1: Multi-Level Temperature Control
```python
device_status = 'active'
temp = 42

if device_status == 'active':
    if temp < 15:
        print("COLD - Turn heater ON")
    elif temp <= 25:
        print("COOL - Increase by 2 degrees")
    elif temp <= 35:
        print("NORMAL - Current setting OK")
    else:
        print("HOT - Turn AC ON")
else:
    print("Device is offline")
```

### Example 2: Smart Home System
```python
is_user_home = True
time_of_day = "morning"

if is_user_home:
    if time_of_day == "morning":
        print("Turn on lights")
        print("Start coffee maker")
    elif time_of_day == "evening":
        print("Lower lights")
        print("Close blinds")
else:
    print("Activate security mode")
    print("Lock doors")
```

### Example 3: Nested with Multiple Branches
```python
age = 25
has_license = True

if age >= 18:
    if has_license:
        print("Can rent a car")
    else:
        print("Need to get a license first")
else:
    if has_license:
        print("Still too young to rent")
    else:
        print("Too young and no license")
```

### Example 4: Bank Account System
```python
account_type = "premium"
balance = 50000

if account_type == "premium":
    if balance > 100000:
        interest_rate = 7.5
    else:
        interest_rate = 6.5
elif account_type == "standard":
    if balance > 50000:
        interest_rate = 4.5
    else:
        interest_rate = 3.5
else:
    interest_rate = 2.0

print(f"Interest Rate: {interest_rate}%")
```

## 📊 Nested If vs Multiple Conditions

### Option 1: Nested If (Use for Dependent Conditions)
```python
if device_active:           # Check device first
    if temp_high:          # Then check temperature
        print("Alert!")
```

**When to use:** Conditions depend on each other

### Option 2: Multiple Conditions with 'and' (Use for Independent Conditions)
```python
if device_active and temp_high:
    print("Alert!")
```

**When to use:** Conditions are independent

### Option 3: Nested with else (Clear flow)
```python
if device_active:
    if temp_high:
        print("Alert!")
    else:
        print("Normal")
else:
    print("Device offline")
```

## 🎯 Nesting Depth Guidelines

| Depth | Status | Recommendation |
|-------|--------|-----------------|
| 1 | Single if-else | ✅ Good |
| 2 | One nested level | ✅ Acceptable |
| 3+ | Multiple nested | ❌ Consider refactoring |

**Refactoring Deep Nesting:**
```python
# Instead of deep nesting, use functions
def check_thermostat():
    if device_offline():
        return handle_offline()
    
    return check_temperature()
```

## 🔄 Real-World Applications

- ✅ Thermostat systems (device status → temperature control)
- ✅ Game logic (player exists → can move → check collision)
- ✅ Banking (account valid → balance ok → process transaction)
- ✅ User authentication (user found → password correct → login)
- ✅ E-commerce (item available → stock > 0 → allow purchase)

## 📊 Decision Guide

**Use nested if when:**
- Conditions are dependent on each other
- Inner condition only makes sense if outer is true
- Logical flow requires sequential checks

**Use 'and' operator when:**
- Conditions are independent
- You need all conditions to be true
- Keep code flat and readable

## 💡 Pro Tips

1. **Limit nesting to 2-3 levels maximum**
2. **Extract complex nested logic into functions**
3. **Use 'and'/'or' operators for independent conditions**
4. **Comment why nesting is necessary**
5. **Test all branches** (both outer and inner paths)

## 🎯 Next Steps

- [ ] Run the program with different inputs
- [ ] Add more temperature ranges
- [ ] Add humidity monitoring
- [ ] Create automatic adjustment
- [ ] Log temperature history
- [ ] Learn about functions to reduce nesting

## 📚 Related Concepts

- **If-Elif-Else:** Linear multiple conditions
- **Logical Operators:** Combine with 'and', 'or', 'not'
- **Functions:** Extract nested logic
- **Error Handling:** Try-except for exceptions

## 💼 Refactoring Complex Nesting

**Before (Deep Nesting):**
```python
if device_on:
    if mode == "heating":
        if temp < 20:
            if user_home:
                print("Heat now")
```

**After (Using Functions):**
```python
def should_heat():
    return device_on and mode == "heating" and temp < 20 and user_home

if should_heat():
    print("Heat now")
```

---

**Difficulty Level:** ⭐⭐⭐ (Intermediate)  
**Time to Complete:** 30-40 minutes  
**Prerequisites:** if-elif-else, logical operators, indentation
