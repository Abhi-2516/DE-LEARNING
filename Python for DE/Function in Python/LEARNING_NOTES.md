# Functions in Python - Comprehensive Learning Notes

## 📚 Course Overview
This comprehensive guide covers all aspects of functions in Python, from basic concepts to advanced patterns. Functions are fundamental building blocks that enable code reusability, modularity, and maintainability.

---

## 📖 Table of Contents
1. [Introduction to Functions](#introduction-to-functions)
2. [Function Basics](#function-basics)
3. [Return Values](#return-values)
4. [Variable Scopes](#variable-scopes)
5. [Advanced Arguments](#advanced-arguments)
6. [Function Types](#function-types)
7. [Best Practices](#best-practices)
8. [Common Pitfalls](#common-pitfalls)
9. [Real-World Examples](#real-world-examples)

---

## Introduction to Functions

### What are Functions?
Functions are reusable blocks of code that perform specific tasks. They:
- **Eliminate code duplication** - Write once, use many times
- **Improve readability** - Give meaningful names to code blocks
- **Enable modularity** - Break complex problems into smaller pieces
- **Facilitate testing** - Test individual components
- **Hide implementation details** - Abstract complexity

### Why Use Functions?
```python
# Without functions - Code duplication
print("Aman ordered chai: masala")
print("Hitesh ordered chai: mint")
print("Priya ordered chai: ginger")

# With functions - Reusable code
def print_order(name, types):
    print(f"{name} ordered chai: {types}")

print_order("Aman", "masala")
print_order("Hitesh", "mint")
print_order("Priya", "ginger")
```

---

## Function Basics

### Defining Functions
```python
def function_name(parameter1, parameter2):
    """Docstring explaining what the function does."""
    # Function body
    return result
```

### Key Terminology
- **Parameters**: Variables defined in function definition
- **Arguments**: Values passed when calling the function
- **Return Statement**: Sends value back to caller

### Simple Example
```python
def calculate_bill(cups, price_per_cup):
    return cups * price_per_cup

total = calculate_bill(3, 50)  # 3 and 50 are arguments
print(total)  # Output: 150
```

### Breaking Down Complex Tasks
```python
# Task: Generate monthly cafe report
def fetch_sales():
    """Fetch sales data."""
    pass

def filter_valid_sales(sales):
    """Filter valid data."""
    pass

def summarize_data(sales):
    """Create summary."""
    pass

def generate_report():
    """Orchestrate all steps."""
    sales = fetch_sales()
    valid_sales = filter_valid_sales(sales)
    summary = summarize_data(valid_sales)
    return summary
```

### Abstraction (Hiding Implementation)
Functions allow you to hide complex logic:
```python
def user_registration():
    """Simple user registration - hides all complexity."""
    get_input()
    validate_input()
    save_to_db()
    print("Registration complete!")

# Caller doesn't need to know the steps
user_registration()
```

---

## Return Values

### Single Return Value
```python
def add(a, b):
    return a + b

result = add(5, 3)  # result = 8
```

### Multiple Return Values (Tuple)
```python
def divide_with_remainder(a, b):
    quotient = a // b
    remainder = a % b
    return quotient, remainder

q, r = divide_with_remainder(17, 5)
print(f"17 ÷ 5 = {q} remainder {r}")
```

### Returning Different Data Types
```python
def get_discount(amount):
    if amount > 1000:
        return {'discount': 0.20, 'type': 'premium'}
    elif amount > 500:
        return {'discount': 0.10, 'type': 'standard'}
    else:
        return {'discount': 0.05, 'type': 'basic'}

result = get_discount(800)
print(result)  # {'discount': 0.10, 'type': 'standard'}
```

### Early Returns
```python
def validate_age(age):
    if age < 0:
        return "Age cannot be negative"
    if age > 150:
        return "Age seems unrealistic"
    return "Age is valid"
```

### Functions with No Return
```python
def print_details(name, age):
    print(f"Name: {name}")
    print(f"Age: {age}")
    # Implicitly returns None

result = print_details("Aman", 25)
print(result)  # Output: None
```

---

## Variable Scopes (LEGB Rule)

Python searches for variables in this order: **Local → Enclosing → Global → Built-in**

### 1. Local Scope
Variables defined inside a function:
```python
def function():
    local_var = "I'm local"  # Only accessible inside this function
    print(local_var)

function()
print(local_var)  # ❌ NameError - local_var doesn't exist here
```

### 2. Enclosing Scope (Closure)
Variables in outer function (for nested functions):
```python
def outer():
    enclosing_var = "I'm from outer"
    
    def inner():
        print(enclosing_var)  # ✓ Can access enclosing variable
    
    inner()

outer()  # Output: I'm from outer
```

### 3. Global Scope
Variables at module level:
```python
global_var = "I'm global"

def function():
    print(global_var)  # ✓ Can read global variables

function()
print(global_var)  # ✓ Can access here too
```

### 4. Built-in Scope
Python's built-in functions and constants:
```python
print(len([1, 2, 3]))  # len is built-in
print(True)             # True is built-in constant
```

### Modifying Global Variables
Use `global` keyword to modify global variables:
```python
counter = 0

def increment():
    global counter  # Declare intention to modify global
    counter += 1
    return counter

print(increment())  # 1
print(increment())  # 2
print(counter)      # 2
```

### Modifying Enclosing Variables
Use `nonlocal` keyword for nested functions:
```python
def outer():
    value = 10
    
    def inner():
        nonlocal value  # Modify enclosing variable
        value += 5
        return value
    
    return inner()

print(outer())  # 15
```

### LEGB Table
| Scope     | Access | Modify | Keyword |
|-----------|--------|--------|---------|
| Local     | ✓      | ✓      | -       |
| Enclosing| ✓      | ✓      | nonlocal|
| Global    | ✓      | ✓      | global  |
| Built-in | ✓      | ✗      | -       |

---

## Advanced Arguments

### 1. Positional Arguments
Order matters:
```python
def make_chai(tea, milk, sugar):
    print(f"{tea} with {milk} milk and {sugar} sugar")

make_chai("Darjeeling", "Yes", "Low")
# Order is critical - can't swap positions
```

### 2. Keyword Arguments
Order doesn't matter:
```python
make_chai(tea="Green", sugar="Medium", milk="No")
# Order is flexible - arguments are identified by name
```

### 3. Mix Positional and Keyword
```python
make_chai("Assam", milk="Yes", sugar="High")
# Positional arguments must come before keyword arguments
```

### 4. *args - Variable Positional Arguments
Accept any number of positional arguments:
```python
def add_ingredients(*ingredients):
    print("Ingredients:")
    for ingredient in ingredients:
        print(f"  - {ingredient}")

add_ingredients("Cinnamon", "Cardamom", "Clove", "Ginger")
# *ingredients becomes a tuple: ("Cinnamon", "Cardamom", ...)
```

### 5. **kwargs - Variable Keyword Arguments
Accept any number of keyword arguments:
```python
def order_chai(**preferences):
    for key, value in preferences.items():
        print(f"{key}: {value}")

order_chai(temperature="Hot", sweetness="Medium", spice="High")
# **preferences becomes a dict: {'temperature': 'Hot', ...}
```

### 6. Combining *args and **kwargs
```python
def prepare_order(customer_name, *items, **extras):
    print(f"Order for: {customer_name}")
    
    for item in items:
        print(f"  - {item}")
    
    for key, value in extras.items():
        print(f"  {key}: {value}")

prepare_order("Aman", "Chai", "Samosa", temp="Hot", milk="Double")
```

### 7. Default Arguments
Provide default values:
```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

greet("Aman")           # Uses default "Hello"
greet("Priya", "Hi")    # Uses provided "Hi"
```

### 8. ⚠️ Mutable Default Arguments (Pitfall!)
```python
# ❌ WRONG - List is created once
def add_item(item, items=[]):
    items.append(item)
    return items

print(add_item("A"))     # ['A']
print(add_item("B"))     # ['A', 'B'] - UNEXPECTED!

# ✅ CORRECT - Create new list each time
def add_item_correct(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

print(add_item_correct("A"))  # ['A']
print(add_item_correct("B"))  # ['B'] - CORRECT!
```

### 9. Type Hints
Document parameter and return types:
```python
def calculate_total(
    price: float,
    quantity: int,
    discount: float = 0.0
) -> float:
    """
    Calculate total with optional discount.
    
    Args:
        price: Price per unit
        quantity: Number of units
        discount: Discount percentage (0-100)
    
    Returns:
        Total cost after discount
    """
    return price * quantity * (1 - discount/100)

total = calculate_total(100.0, 5, 10.0)
```

### 10. Argument Order Rule
```
positional → *args → keyword → **kwargs
```

Example:
```python
def function(pos, *args, keyword=None, **kwargs):
    pass

function(1, 2, 3, keyword=4, extra=5)
# pos=1, args=(2,3), keyword=4, kwargs={'extra':5}
```

---

## Function Types

### 1. Pure Functions
- Same input → Same output (deterministic)
- No side effects (don't modify external state)
- Easy to test and reason about

```python
def add(a, b):
    """Pure function - always returns a + b."""
    return a + b

print(add(2, 3))  # Always 5
```

### 2. Impure Functions
- Modify global state or external data
- Have side effects beyond return value
- Harder to test

```python
sales_total = 0

def record_sale(amount):
    """Impure - modifies global state."""
    global sales_total
    sales_total += amount  # Side effect!
```

### 3. Recursive Functions
Functions that call themselves:

```python
def factorial(n):
    # Base case - prevents infinite recursion
    if n <= 1:
        return 1
    # Recursive case
    return n * factorial(n - 1)

print(factorial(5))  # 5! = 120
```

**Key components:**
- **Base case**: When to stop recursing
- **Recursive case**: Function calling itself with smaller input

Example: Recursive sum
```python
def sum_list(numbers):
    if not numbers:      # Base case: empty list
        return 0
    # Recursive case: first + sum of rest
    return numbers[0] + sum_list(numbers[1:])

print(sum_list([1, 2, 3, 4, 5]))  # 15
```

### 4. Lambda Functions
Anonymous functions for simple operations:

```python
# Basic lambda
square = lambda x: x ** 2
print(square(5))  # 25

# Lambda with multiple parameters
add = lambda x, y: x + y
print(add(3, 4))  # 7

# Lambda with filter()
numbers = [1, 2, 3, 4, 5]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4]

# Lambda with map()
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)  # [2, 4, 6, 8, 10]

# Lambda with sorted()
people = [{'name': 'Aman', 'age': 25}, {'name': 'Priya', 'age': 23}]
sorted_people = sorted(people, key=lambda p: p['age'])
```

**When to use Lambda:**
- Simple operations only
- Single expression
- Used as callback/argument
- Avoid complex logic (use def instead)

### 5. Higher-Order Functions
Functions that take or return other functions:

```python
def apply_operation(a, b, operation):
    """Takes a function as parameter."""
    return operation(a, b)

def multiply(x, y):
    return x * y

print(apply_operation(3, 4, multiply))  # 12
print(apply_operation(3, 4, lambda x, y: x + y))  # 7
```

### 6. Decorators
Functions that modify other functions:

```python
def add_logging(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Returned {result}")
        return result
    return wrapper

@add_logging
def add(a, b):
    return a + b

add(3, 4)
# Output:
# Calling add
# Returned 7
```

---

## Best Practices

### 1. Write Docstrings
```python
def calculate_discount(amount, discount_percent):
    """
    Calculate discounted amount.
    
    Parameters:
        amount (float): Original amount
        discount_percent (float): Discount percentage (0-100)
    
    Returns:
        float: Amount after discount
    
    Examples:
        >>> calculate_discount(100, 10)
        90.0
    """
    return amount * (1 - discount_percent / 100)
```

### 2. Use Type Hints
```python
def greet(name: str, age: int = 0) -> str:
    """Greet someone with optional age."""
    if age:
        return f"Hello {name}, age {age}!"
    return f"Hello {name}!"
```

### 3. Keep Functions Small
- Single Responsibility Principle
- Easier to test
- Easier to understand

### 4. Use Meaningful Names
```python
# ❌ Bad
def f(x):
    return x * 2

# ✓ Good
def calculate_double(amount):
    return amount * 2
```

### 5. Default to Pure Functions
- Easier to test
- Easier to reason about
- Avoid global state when possible

### 6. Prefer Explicit Over Implicit
```python
# ❌ Less clear
def process(data):
    return [x for x in data if x > 10]

# ✓ More clear
def filter_large_items(data, threshold=10):
    """Filter items larger than threshold."""
    return [item for item in data if item > threshold]
```

---

## Common Pitfalls

### 1. Mutable Default Arguments
```python
# ❌ WRONG
def append_item(item, items=[]):
    items.append(item)
    return items

# ✓ CORRECT
def append_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

### 2. Modifying Global State Unintentionally
```python
# ❌ WRONG - Side effect on list
data = [1, 2, 3]

def process(items):
    items.append(4)  # Modifies original!
    return items

# ✓ CORRECT - No side effects
def process_correct(items):
    new_items = items.copy()
    new_items.append(4)
    return new_items
```

### 3. Forgetting to Return
```python
# ❌ WRONG - Returns None
def calculate_total(price, quantity):
    price * quantity  # Missing return!

# ✓ CORRECT
def calculate_total(price, quantity):
    return price * quantity
```

### 4. Too Many Parameters
```python
# ❌ WRONG - Too many parameters
def create_user(name, email, phone, address, city, country, zipcode):
    pass

# ✓ CORRECT - Group related parameters
def create_user(name, email, address_dict):
    pass
```

### 5. Not Using Docstrings
```python
# ❌ WRONG - No documentation
def calc(a, b, c):
    return a + b * c

# ✓ CORRECT - Clear documentation
def calculate_total(price, quantity, tax_rate):
    """
    Calculate total with tax.
    
    Args:
        price: Price per unit
        quantity: Number of items
        tax_rate: Tax percentage
    
    Returns:
        Total amount including tax
    """
    subtotal = price * quantity
    return subtotal * (1 + tax_rate)
```

---

## Real-World Examples

### Project 1: Student Grading System
See: `06_project_grading_system.py`

**Concepts demonstrated:**
- Multiple functions working together
- Type hints
- Docstrings
- Processing collections
- Statistics and aggregation

### Project 2: Invoice Generation System
See: `07_project_invoice_system.py`

**Concepts demonstrated:**
- *args and **kwargs
- Complex return values
- String formatting
- Financial calculations
- Flexible parameter handling

---

## Summary of Key Concepts

| Concept | Purpose | Example |
|---------|---------|---------|
| Parameters | Input to function | `def func(param)` |
| Return | Output from function | `return value` |
| Local Scope | Variables inside function | `x = 5` (in function) |
| Global Scope | Module-level variables | `x = 5` (in module) |
| *args | Variable positional args | `def func(*args)` |
| **kwargs | Variable keyword args | `def func(**kwargs)` |
| Default Args | Provide defaults | `def func(x=5)` |
| Type Hints | Document types | `def func(x: int) -> int` |
| Lambda | Anonymous function | `lambda x: x * 2` |
| Decorator | Modify functions | `@decorator def func()` |

---

## Learning Path

1. **Start here:**
   - Learn basic function definition
   - Understand parameters and arguments
   - Practice with simple examples

2. **Then move to:**
   - Return values and multiple returns
   - Variable scopes (LEGB rule)
   - Default arguments

3. **Progress to:**
   - *args and **kwargs
   - Type hints and docstrings
   - Different function types

4. **Master:**
   - Decorators
   - Higher-order functions
   - Design patterns
   - Performance optimization

---

## Practice Exercises

1. Create a function to calculate bill with VAT
2. Build a function that processes student grades
3. Write a function to generate formatted invoices
4. Create recursive functions for mathematical problems
5. Use lambda with filter(), map(), sorted()
6. Practice scope with nested functions
7. Create decorators for logging and timing

---

## Resources for Further Learning

- **Python Official Docs:** https://docs.python.org/3/tutorial/controlflow.html
- **PEP 8:** Style Guide for Python Code
- **PEP 257:** Docstring Conventions
- **Type Hints:** PEP 484

---

**Happy Learning! 🚀**
