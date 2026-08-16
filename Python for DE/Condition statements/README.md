# Conditional Statements in Python - Complete Module

Welcome to the comprehensive guide on **Conditional Statements in Python**! This module breaks down all the fundamental decision-making constructs in Python through practical, real-world examples.

## 📁 Project Structure

```
Condition statements/
├── 01_notification_system/
│   ├── notification_system.py (Basic if-else)
│   └── README.md
├── 02_snack_system/
│   ├── snack_system.py (If-else with logical operators)
│   └── README.md
├── 03_tea_stall_pricing/
│   ├── tea_stall_pricing.py (If-elif-else)
│   └── README.md
├── 04_smart_thermostat/
│   ├── smart_thermostat.py (Nested if statements)
│   └── README.md
├── 05_delivery_fees_calculator/
│   ├── delivery_fees_calculator.py (Ternary operator)
│   └── README.md
├── 06_train_seat_booking/
│   ├── train_seat_booking.py (Match-case statement)
│   └── README.md
├── LEARNING_NOTES.md (Comprehensive theory & concepts)
└── README.md (This file)
```

## 🎯 Learning Objectives

By completing this module, you will understand:

- ✅ Basic if-else conditional statements
- ✅ Logical operators (and, or, not)
- ✅ If-elif-else chains
- ✅ Nested conditional statements
- ✅ Ternary/conditional expressions
- ✅ Match-case pattern matching (Python 3.10+)
- ✅ Real-world applications of conditionals
- ✅ Best practices and common pitfalls

## 🚀 Quick Start

### Running Individual Examples

```bash
# Example 1: Basic if-else
python 01_notification_system/notification_system.py

# Example 2: Logical operators
python 02_snack_system/snack_system.py

# Example 3: If-elif-else
python 03_tea_stall_pricing/tea_stall_pricing.py

# Example 4: Nested if
python 04_smart_thermostat/smart_thermostat.py

# Example 5: Ternary operator
python 05_delivery_fees_calculator/delivery_fees_calculator.py

# Example 6: Match-case (Python 3.10+)
python 06_train_seat_booking/train_seat_booking.py
```

## 📚 Module Breakdown

### 1️⃣ Notification System
**Concept:** Basic If-Else  
**Difficulty:** Beginner  
**File:** [01_notification_system/notification_system.py](01_notification_system/notification_system.py)

Simple notification checking if a kettle is boiled.

```python
if kettle_boiled:
    print("Tea is ready!")
else:
    print("Please wait...")
```

---

### 2️⃣ Snack System
**Concept:** Logical Operators (OR)  
**Difficulty:** Beginner  
**File:** [02_snack_system/snack_system.py](02_snack_system/snack_system.py)

Restaurant ordering system using OR operator for multiple valid options.

```python
if snack == "cookies" or snack == "samosa":
    print("Available!")
else:
    print("Not available.")
```

---

### 3️⃣ Tea Stall Pricing
**Concept:** If-Elif-Else Chain  
**Difficulty:** Beginner  
**File:** [03_tea_stall_pricing/tea_stall_pricing.py](03_tea_stall_pricing/tea_stall_pricing.py)

Dynamic pricing system based on multiple cup sizes.

```python
if cup_type == "small":
    price = 10
elif cup_type == "medium":
    price = 15
elif cup_type == "large":
    price = 20
```

---

### 4️⃣ Smart Thermostat
**Concept:** Nested If Statements  
**Difficulty:** Intermediate  
**File:** [04_smart_thermostat/smart_thermostat.py](04_smart_thermostat/smart_thermostat.py)

Temperature monitoring system with dependent conditions.

```python
if device_status == "active":
    if temp > 35:
        print("ALERT!")
```

---

### 5️⃣ Delivery Fees Calculator
**Concept:** Ternary/Conditional Expression  
**Difficulty:** Intermediate  
**File:** [05_delivery_fees_calculator/delivery_fees_calculator.py](05_delivery_fees_calculator/delivery_fees_calculator.py)

Quick conditional assignment for fee calculation.

```python
delivery_fee = 0 if order_amount > 300 else 30
```

---

### 6️⃣ Train Seat Booking
**Concept:** Match-Case Pattern Matching  
**Difficulty:** Intermediate  
**File:** [06_train_seat_booking/train_seat_booking.py](06_train_seat_booking/train_seat_booking.py)

Modern pattern matching for multiple seat types.

```python
match seat_type:
    case "sleeper":
        print("Sleep mode activated!")
    case "ac":
        print("AC enabled!")
```

---

## 📖 Recommended Learning Path

1. **Start with:** `01_notification_system` - Understand basic if-else
2. **Then learn:** `02_snack_system` - Combine conditions with AND/OR
3. **Progress to:** `03_tea_stall_pricing` - Handle multiple choices
4. **Advance to:** `04_smart_thermostat` - Nested conditions
5. **Optimize with:** `05_delivery_fees_calculator` - Ternary expressions
6. **Modern approach:** `06_train_seat_booking` - Match-case (Python 3.10+)

## 📝 Comprehensive Learning Notes

For detailed theory, concepts, best practices, and common mistakes, refer to:
→ **[LEARNING_NOTES.md](LEARNING_NOTES.md)**

This document includes:
- Concept explanations with code examples
- Real-world use cases
- Decision tree for choosing the right statement
- Common mistakes and how to avoid them
- Best practices and tips
- Reference materials

---

## 🎮 Practice Challenges

Try modifying the examples to:

1. **Notification System**
   - Add multiple device statuses
   - Add temperature thresholds

2. **Snack System**
   - Add prices for each snack
   - Accept multiple snack orders

3. **Tea Stall**
   - Add extras (sugar level, milk type)
   - Apply discounts for bulk orders

4. **Thermostat**
   - Add multiple temperature ranges
   - Add auto-adjustment mode

5. **Delivery Calculator**
   - Add tiered discounts
   - Add taxes and coupon codes

6. **Train Booking**
   - Add availability checking
   - Add booking confirmation

---

## 🐛 Debugging Tips

- **Check indentation:** Python is indent-sensitive
- **Use print() statements:** Debug by printing intermediate values
- **Test edge cases:** Empty strings, None, zero, negative numbers
- **Check operator precedence:** `and` has higher precedence than `or`
- **Use Python debugger:** `pdb` module for step-by-step debugging

---

## 📊 Conditional Statements Comparison

| Type | Syntax | Use | Complexity |
|------|--------|-----|-----------|
| If-Else | `if c: ... else: ...` | Binary choice | Low |
| If-Elif-Else | `if c1: ... elif c2: ...` | Multiple choices | Low |
| Logical Ops | `and`, `or`, `not` | Combined conditions | Low |
| Nested If | If inside if | Dependent conditions | Medium |
| Ternary | `x if c else y` | Quick assignment | Low |
| Match-Case | `match x: case y: ...` | Pattern matching | Medium |

---

## 💻 System Requirements

- Python 3.7+ (for all except match-case)
- Python 3.10+ (for match-case statement)
- Any code editor (VS Code, PyCharm, Notepad++, etc.)

To check your Python version:
```bash
python --version
```

---

## 🔗 Additional Resources

- [Python Official Documentation - Control Flow](https://docs.python.org/3/tutorial/controlflow.html)
- [Python Docs - if statements](https://docs.python.org/3/reference/compound_stmts.html#the-if-statement)
- [PEP 634 - Structural Pattern Matching (Match-Case)](https://www.python.org/dev/peps/pep-0634/)

---

## 📌 Key Takeaways

1. **If-else** is the foundation of decision-making in programming
2. **Logical operators** allow combining multiple conditions
3. **If-elif-else** handles multiple exclusive options
4. **Nested ifs** manage dependent conditions
5. **Ternary expressions** provide concise one-line conditions
6. **Match-case** is the modern, readable approach for multiple options
7. Always consider **edge cases** and **invalid inputs**
8. Keep conditions **simple and readable**

---

## ✅ Progress Tracking

- [ ] Completed: Notification System
- [ ] Completed: Snack System
- [ ] Completed: Tea Stall Pricing
- [ ] Completed: Smart Thermostat
- [ ] Completed: Delivery Fees Calculator
- [ ] Completed: Train Seat Booking
- [ ] Read: LEARNING_NOTES.md
- [ ] Practice: All challenges
- [ ] Mastered: Conditional statements!

---

**Happy Learning! 🚀**

*Last Updated: 2024*  
*Python Version: 3.10+*  
*Difficulty Level: Beginner to Intermediate*
