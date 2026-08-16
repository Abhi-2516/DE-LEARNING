# Project 6: Train Seat Booking

## 📋 Project Description

A modern train seat booking system that demonstrates **match-case statement** (structural pattern matching), a Python 3.10+ feature that provides a cleaner alternative to long if-elif-else chains.

## 🎯 Learning Objective

Understand modern pattern matching in Python using match-case and when it's preferable to traditional if-elif-else statements.

## 💡 Concept Breakdown

### Match-Case Syntax

```python
match value:
    case pattern1:
        # Code if value matches pattern1
    case pattern2:
        # Code if value matches pattern2
    case _:
        # Default case (underscore matches anything)
```

### Key Points

1. **Introduced in Python 3.10** (released October 2021)
2. **Cleaner than multiple if-elif** when checking equality
3. **More expressive intent** - clearly shows multiple options
4. **Underscore `_`** is the default case (like `else`)
5. **First matching case executes** - others are skipped

### Project Example

```python
seat_type = input("Enter your seat type (sleeper/ac/general/luxury): ").lower()

match seat_type:
    case "sleeper":
        print("You got a seat to sleep comfortably.")
    case "ac":
        print("You got an AC seat with climate control.")
    case "general":
        print("You got a general seating. Please find your seat.")
    case "luxury":
        print("You got a full compartment along with a personal washroom!")
    case _:
        print("Invalid seat type.")
```

## 📊 Flowchart

```
Start
  ↓
Get seat type from user
  ↓
Match against patterns
  ├─ "sleeper" → Sleeper features
  ├─ "ac" → AC features
  ├─ "general" → General features
  ├─ "luxury" → Luxury features
  └─ anything else → Invalid message
  ↓
End
```

## 🔑 Key Concepts

| Concept | Explanation | Example |
|---------|-------------|---------|
| **match** | Start pattern matching | `match value:` |
| **case** | A pattern to check | `case "sleeper":` |
| **pattern** | Value to match against | Literal, variable, or complex |
| **_** | Wildcard/default case | Matches anything |
| **Guard** | Additional condition | `case x if x > 0:` |

## 🚀 How to Run

```bash
python train_seat_booking.py
```

**Important:** Requires Python 3.10 or higher!

```bash
# Check your Python version
python --version
```

**Sample Interaction:**
```
Enter your seat type (sleeper/ac/general/luxury): luxury
You got a full compartment along with a personal washroom!
```

## 💻 Try It Yourself

**Modify the code to:**
1. Add pricing information for each seat type
2. Add availability checking
3. Add booking confirmation
4. Add cancellation logic
5. Add passenger details collection

## ⚠️ Common Mistakes

### ❌ Using Old Python Version
```
Error: syntax error
```
**Cause:** Match-case requires Python 3.10+

**Solution:**
```bash
python3.10 train_seat_booking.py
# or
python3.11 train_seat_booking.py
```

### ❌ Forgetting Colon After match and case
```python
# WRONG
match seat_type  # ← Missing colon
    case "sleeper"  # ← Missing colon

# CORRECT
match seat_type:
    case "sleeper":
```

### ❌ Using `else` Instead of `_`
```python
# WRONG - else doesn't work with match
match value:
    case "a":
        print("A")
    else:  # ← Wrong!
        print("Default")

# CORRECT - use underscore
match value:
    case "a":
        print("A")
    case _:  # ← Correct!
        print("Default")
```

### ❌ Not Making Default Case
```python
# Risky - No handling for unexpected input
match seat_type:
    case "sleeper":
        print("Sleeper")
    case "ac":
        print("AC")
# What if user enters "luxury"?

# Better - Always include default
match seat_type:
    case "sleeper":
        print("Sleeper")
    case "ac":
        print("AC")
    case _:
        print("Invalid choice")
```

## 📝 Extended Examples

### Example 1: Simple Matching
```python
day = input("Enter day of week: ").lower()

match day:
    case "monday":
        print("Start of work week!")
    case "friday":
        print("Almost weekend!")
    case "saturday" | "sunday":  # ← Multiple patterns!
        print("Weekend time!")
    case _:
        print("Unknown day")
```

### Example 2: With Pricing
```python
seat_type = input("Choose seat: ").lower()

match seat_type:
    case "sleeper":
        price = 500
        features = "Bed, bedding, light"
    case "ac":
        price = 750
        features = "Climate control, comfort"
    case "general":
        price = 250
        features = "Basic seating"
    case "luxury":
        price = 1500
        features = "Private compartment, washroom"
    case _:
        print("Invalid choice")
        return

print(f"Price: Rs. {price}")
print(f"Features: {features}")
```

### Example 3: With Guard Conditions
```python
age = int(input("Enter age: "))

match age:
    case 0:
        category = "Infant"
    case age if age < 13:
        category = "Child"
    case age if age < 20:
        category = "Teen"
    case age if age < 60:
        category = "Adult"
    case _:
        category = "Senior"

print(f"Category: {category}")
```

### Example 4: Pattern Matching with Tuples
```python
coordinates = (1, 2)

match coordinates:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"On Y-axis at {y}")
    case (x, 0):
        print(f"On X-axis at {x}")
    case (x, y):
        print(f"Point at ({x}, {y})")
```

### Example 5: Multiple Options with OR (|)
```python
vehicle_type = input("Enter vehicle: ").lower()

match vehicle_type:
    case "car" | "truck" | "van":
        fee = 100
    case "bike" | "cycle":
        fee = 20
    case "bus":
        fee = 150
    case _:
        print("Unknown vehicle")
        return

print(f"Parking fee: ${fee}")
```

## 📊 Match-Case vs If-Elif-Else

### Approach 1: If-Elif-Else (Works with Python 3.9 and earlier)
```python
if seat_type == "sleeper":
    print("Sleeper")
elif seat_type == "ac":
    print("AC")
elif seat_type == "general":
    print("General")
elif seat_type == "luxury":
    print("Luxury")
else:
    print("Invalid")
```

**Pros:**
- Works with older Python versions
- Familiar to most programmers

**Cons:**
- Repetitive (seat_type == ...)
- Less readable for many options
- Verbose

### Approach 2: Match-Case (Python 3.10+)
```python
match seat_type:
    case "sleeper":
        print("Sleeper")
    case "ac":
        print("AC")
    case "general":
        print("General")
    case "luxury":
        print("Luxury")
    case _:
        print("Invalid")
```

**Pros:**
- Cleaner and more readable
- Less repetitive
- Modern Python idiom
- Clearly shows all options

**Cons:**
- Requires Python 3.10+
- Not familiar to beginners

## 📊 Comparison Table

| Feature | If-Elif-Else | Match-Case |
|---------|--------------|-----------|
| Python Version | 3.7+ | 3.10+ |
| Readability | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| Multiple options | Verbose | Concise |
| Pattern matching | Limited | Advanced |
| Performance | Good | Slightly better |
| Familiarity | Very high | Growing |

## 🎯 When to Use Match-Case

**✅ Use match-case when:**
- Python 3.10+ is available
- Multiple equality checks on same variable
- Code is cleaner and more readable
- You want modern Python style
- Checking many options

**❌ Don't use match-case when:**
- Must support Python 3.9 or earlier
- Simple if-else is enough
- Complex conditions with 'and'/'or'
- Different variables being compared

## 🔄 Real-World Applications

- ✅ Menu systems (choose from options)
- ✅ E-commerce product selection
- ✅ Game state handling
- ✅ Request routing in APIs
- ✅ File type handling
- ✅ Error code processing

## 💡 Advanced Pattern Matching

### Guard Clauses
```python
match score:
    case score if score >= 90:
        grade = 'A'
    case score if score >= 80:
        grade = 'B'
    case score if score >= 70:
        grade = 'C'
    case _:
        grade = 'F'
```

### Multiple Patterns
```python
match status:
    case "available" | "ready" | "active":
        process()
    case "offline" | "disabled":
        skip()
```

### Wildcard Patterns
```python
match point:
    case (0, 0):
        print("Origin")
    case (_, 0):
        print("On X-axis")
    case (0, _):
        print("On Y-axis")
    case _:
        print("General point")
```

## 🎯 Next Steps

- [ ] Verify Python version is 3.10+
- [ ] Run the program
- [ ] Add pricing information
- [ ] Add booking confirmation
- [ ] Add cancellation
- [ ] Add passenger details
- [ ] Create a database backend

## 📚 Related Concepts

- **If-Elif-Else:** Traditional multiple conditions
- **Logical Operators:** Combine conditions
- **PEP 634:** Official pattern matching proposal
- **Type Matching:** Advanced pattern matching

## 🔗 Resources

- [Python 3.10 Release Notes](https://www.python.org/dev/peps/pep-0634/)
- [Structural Pattern Matching Tutorial](https://docs.python.org/3/tutorial/match.html)
- [What's New in Python 3.10](https://docs.python.org/3/whatsnew/3.10.html)

## 📊 Checking Your Python Version

```bash
# Check version
python --version

# Python 3.10+?
python3.10 --version
python3.11 --version
python3.12 --version
```

## 💡 Pro Tips

1. **Always include default case** (`case _:`)
2. **Use `.lower()` for case-insensitive matching**
3. **Consider compatibility** (does your team have Python 3.10+?)
4. **Use guard clauses** for complex conditions
5. **Combine with `|`** for multiple matching patterns

---

**Difficulty Level:** ⭐⭐⭐ (Intermediate)  
**Time to Complete:** 20-30 minutes  
**Prerequisites:** If-elif-else, Python 3.10+
