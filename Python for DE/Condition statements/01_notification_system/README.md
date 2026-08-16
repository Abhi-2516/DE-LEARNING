# Project 1: Notification System

## 📋 Project Description

A simple kettle boiling notification system that demonstrates the fundamental **if-else** conditional statement in Python.

## 🎯 Learning Objective

Understand how to use basic if-else statements to execute different code blocks based on a condition.

## 💡 Concept Breakdown

### Basic If-Else Syntax
```python
if condition:
    # Code to execute if condition is True
else:
    # Code to execute if condition is False
```

### How It Works

```python
kt_boiled = True

if kt_boiled:
    print("Kettle is boiled, you can make tea now.")
else:
    print("Kettle is not boiled yet, please wait.")
```

**Output:** `Kettle is boiled, you can make tea now.`

## 🔑 Key Concepts

| Concept | Explanation |
|---------|-------------|
| **Condition** | A statement that evaluates to `True` or `False` |
| **Boolean** | A data type with only two values: `True` or `False` |
| **Indentation** | Python uses indentation (4 spaces) to define code blocks |
| **Colon** | Required after `if` and `else` statements |

## 📊 Flowchart

```
Start
  ↓
Is kettle boiled?
  ├─ YES → Print "Kettle is boiled..."
  └─ NO  → Print "Kettle is not boiled yet..."
  ↓
End
```

## 🚀 How to Run

```bash
python notification_system.py
```

## 💻 Try It Yourself

**Modify the code to:**
1. Change `kt_boiled` to `False` and observe the output
2. Add more boolean variables (e.g., water level, gas availability)
3. Create a version that asks for user input

## ⚠️ Common Mistakes

### ❌ Missing Colon
```python
if kt_boiled:  # ← Colon is required!
    print("Ready")
```

### ❌ Wrong Indentation
```python
if kt_boiled:
print("Ready")  # ← Must be indented!
```

### ❌ Using Assignment (=) Instead of Comparison (==)
```python
if kt_boiled = True:  # ← Wrong! Use == for comparison
    print("Ready")
```

## 🔄 Real-World Applications

- ✅ Checking if a user is logged in
- ✅ Verifying if a file exists
- ✅ Checking if a number is positive/negative
- ✅ Verifying age eligibility
- ✅ Checking if username/password is correct

## 📝 Example Modifications

### Example 1: Interactive Version
```python
status = input("Is kettle boiled? (yes/no): ").lower()

if status == "yes":
    print("Tea is ready!")
else:
    print("Please wait for boiling.")
```

### Example 2: With Multiple Checks
```python
kt_boiled = True
water_available = True

if kt_boiled and water_available:
    print("You can make tea now!")
else:
    print("Missing resources.")
```

## 🎯 Next Steps

- [ ] Run the program
- [ ] Modify the condition and test
- [ ] Add more variables
- [ ] Convert to interactive version
- [ ] Learn about logical operators (`and`, `or`, `not`)

## 📚 Related Concepts

- **Logical Operators:** `and`, `or`, `not`
- **Comparison Operators:** `==`, `!=`, `<`, `>`, `<=`, `>=`
- **Boolean Algebra:** Truth tables and logic

---

**Difficulty Level:** ⭐ (Beginner)  
**Time to Complete:** 5-10 minutes  
**Prerequisites:** Basic Python syntax
