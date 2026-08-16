# Project 5: Delivery Fees Calculator

## 📋 Project Description

A delivery fee calculation system that demonstrates the **ternary operator** (conditional expression), a compact way to assign values based on a condition.

## 🎯 Learning Objective

Learn how to use the ternary operator for concise one-line conditional assignments and when it's appropriate to use instead of full if-else statements.

## 💡 Concept Breakdown

### Ternary Operator Syntax

```python
value = value_if_true if condition else value_if_false
```

### Structure

```
    ↓ true value
    |
value = A if condition else B
             |
             └─ condition
                         |
                         └─ false value
```

### Key Points

1. **Evaluates condition first**
2. **Returns one of two values** based on the condition
3. **Replaces simple if-else** in a single line
4. **More readable than nested if-else** for simple cases

### Project Example

```python
order_amount = 450
delivery_fees = 0 if order_amount > 300 else 30

# If order_amount > 300: delivery_fees = 0
# Otherwise: delivery_fees = 30
```

## 📊 Flowchart

```
Start
  ↓
Get order amount
  ↓
Is order amount > $300?
  ├─ YES → Set delivery fee = $0
  └─ NO  → Set delivery fee = $30
  ↓
Display total
  ↓
End
```

## 🔑 Key Concepts

| Concept | Explanation | Example |
|---------|-------------|---------|
| **Ternary** | Three parts: value, condition, value | `x if cond else y` |
| **Conditional Expression** | Another name for ternary | Same thing |
| **Conciseness** | One line instead of multiple | Better readability |
| **Value Assignment** | Assigns a value based on condition | `var = expr if cond else expr2` |

## 🚀 How to Run

```bash
python delivery_fees_calculator.py
```

**Sample Interaction:**
```
Enter order amount (in dollars): 350
Order Amount: $350
Delivery Fees: $0
Total Amount: $350
```

Another example:
```
Enter order amount (in dollars): 200
Order Amount: $200
Delivery Fees: $30
Total Amount: $230
```

## 💻 Try It Yourself

**Modify the code to:**
1. Add tiered discount system (0-100: $50, 101-300: $30, 300+: free)
2. Add taxes (10% of total)
3. Add coupon codes
4. Add special holiday charges
5. Calculate savings amount

## ⚠️ Common Mistakes

### ❌ Wrong Syntax - Reversed Order
```python
# WRONG - Condition comes after values
result = 10 if 20 else (x > 5)

# CORRECT - Condition is in the middle
result = 10 if (x > 5) else 20
```

### ❌ Too Complex for Ternary
```python
# WRONG - Too complex, should use if-elif-else
result = (10 if x > 50 else (20 if x > 25 else 30)) if condition else 0

# CORRECT - Use if-elif-else for complex logic
if condition:
    if x > 50:
        result = 10
    elif x > 25:
        result = 20
    else:
        result = 30
else:
    result = 0
```

### ❌ Ignoring Operator Precedence
```python
# Can cause unexpected results
result = 10 if x > 5 and y < 10 else 20  # ← What executes if x <= 5?

# Better with parentheses
result = 10 if (x > 5 and y < 10) else 20
```

### ✅ Good Practices
```python
# Simple and clear
discount = 0 if amount > 300 else 50

# Readable with meaningful variable names
free_delivery = 0 if order_value > minimum_threshold else standard_fee

# Multi-line for complex expressions (sometimes)
result = (
    premium_price if customer_type == "premium"
    else standard_price
)
```

## 📝 Extended Examples

### Example 1: Simple Discounts
```python
age = int(input("Enter age: "))
ticket_price = 5 if age < 12 else 10
print(f"Ticket price: ${ticket_price}")
```

### Example 2: Grades
```python
score = int(input("Enter score: "))
grade = "Pass" if score >= 40 else "Fail"
print(f"Result: {grade}")
```

### Example 3: Multiple Ternary (Nested)
```python
amount = int(input("Enter amount: "))
fee = 0 if amount > 500 else (5 if amount > 100 else 10)
print(f"Fee: ${fee}")
```

**Note:** Nested ternary can become hard to read. Consider if-elif-else instead.

### Example 4: Enhanced Delivery Calculator
```python
order_amount = int(input("Enter order amount: "))
customer_type = input("Premium member? (yes/no): ").lower()

# Tier-based delivery fees
if order_amount > 500:
    base_fee = 0
elif order_amount > 300:
    base_fee = 10
else:
    base_fee = 30

# Premium discount
delivery_fee = 0 if customer_type == "yes" else base_fee

print(f"Order: ${order_amount}")
print(f"Delivery: ${delivery_fee}")
print(f"Total: ${order_amount + delivery_fee}")
```

### Example 5: String Ternary
```python
is_available = True
status = "In stock" if is_available else "Out of stock"
print(status)
```

### Example 6: Function Return with Ternary
```python
def get_discount(amount):
    return 0.1 if amount > 1000 else 0.05  # 10% or 5%

order = 1200
discount_rate = get_discount(order)
final_price = order * (1 - discount_rate)
print(f"Final price: ${final_price}")
```

## 📊 Ternary vs If-Else

### Simple Case (Use Ternary)
```python
# Ternary - Concise and readable
discount = 50 if age > 60 else 0

# If-else - Verbose for simple case
if age > 60:
    discount = 50
else:
    discount = 0
```

### Complex Case (Use If-Else)
```python
# WRONG - Multiple nested ternary (hard to read)
result = x if a else y if b else z if c else w

# CORRECT - Use if-elif-else
if a:
    result = x
elif b:
    result = y
elif c:
    result = z
else:
    result = w
```

## 🎯 When to Use Ternary

**✅ Use ternary when:**
- Simple true/false decision
- Quick variable assignment
- One line is more readable
- Condition is straightforward

**❌ Don't use ternary when:**
- Multiple conditions (use if-elif-else)
- Complex logic inside
- Code becomes unreadable
- More than one level of nesting

## 🔄 Real-World Applications

- ✅ Discount calculations (amount > limit)
- ✅ Age verification (age >= 18)
- ✅ Subscription pricing (annual vs monthly)
- ✅ Tax calculations (taxable vs non-taxable)
- ✅ Status messages (available vs unavailable)
- ✅ User roles (admin vs user)

## 📊 Comparison with Other Approaches

| Approach | Code | Readability | Use Case |
|----------|------|-------------|----------|
| Ternary | `v1 if c else v2` | ⭐⭐⭐⭐⭐ | Simple condition |
| If-Else | Multi-line | ⭐⭐⭐⭐ | Medium condition |
| If-Elif-Else | Multi-line | ⭐⭐⭐ | Multiple conditions |
| Nested Ternary | `v1 if c1 else v2 if c2 else v3` | ⭐⭐ | Avoid! |

## 💡 Pro Tips

1. **Keep it simple** - If you need to think about it, use if-else
2. **One condition** - Multiple conditions? Use if-elif-else
3. **No side effects** - Only assign values, no function calls
4. **Use parentheses** - Makes condition clearer `val if (condition) else val2`
5. **Readable first** - Code is read more than written

## 🎯 Next Steps

- [ ] Run the program with different amounts
- [ ] Add tiered pricing system
- [ ] Add multiple discount levels
- [ ] Calculate savings
- [ ] Add tax calculations
- [ ] Create a complete price calculator

## 📚 Related Concepts

- **If-Else:** Full conditional statement
- **If-Elif-Else:** Multiple conditions
- **Boolean Operators:** Combine conditions
- **Operator Precedence:** Order of evaluation

## 🚀 Advanced: Ternary with Operators

```python
# Combining with operators
price = 100
final_price = price * 0.9 if age > 60 else price

# Using in list comprehensions
numbers = [1, 2, 3, 4, 5]
evens = ["even" if n % 2 == 0 else "odd" for n in numbers]

# Using with function calls
message = get_discount() if is_member else get_regular_price()
```

---

**Difficulty Level:** ⭐⭐ (Beginner-Intermediate)  
**Time to Complete:** 15-25 minutes  
**Prerequisites:** Basic if-else, comparison operators
