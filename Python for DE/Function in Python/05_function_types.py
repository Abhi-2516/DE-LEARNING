"""
Functions in Python - Function Types
=====================================
Learn: Pure vs Impure, Recursive, Lambda, and Higher-Order Functions
"""

print("=" * 60)
print("TYPES OF FUNCTIONS")
print("=" * 60)
print()

# TYPE 1: Pure Functions
print("\n1. PURE FUNCTIONS - No side effects, same input = same output")
print("-" * 50)

def calculate_chai_cost(cups: int, price_per_cup: int) -> int:
    """
    Pure function: Always returns same result for same input.
    No side effects (doesn't modify global state or external data).
    """
    return cups * price_per_cup

print(f"3 cups @ ₹50: ₹{calculate_chai_cost(3, 50)}")
print(f"5 cups @ ₹50: ₹{calculate_chai_cost(5, 50)}")
print("✓ Same input always gives same output")
print()


# TYPE 2: Impure Functions
print("2. IMPURE FUNCTIONS - Side effects that modify state")
print("-" * 50)

sales_total = 0  # Global variable

def record_sale(amount: int) -> None:
    """
    Impure function: Modifies global state.
    Has side effects beyond just returning a value.
    """
    global sales_total
    sales_total += amount
    print(f"Sale recorded: ₹{amount}")
    print(f"Running total: ₹{sales_total}")

record_sale(100)
record_sale(200)
print("⚠️ Function modifies global state")
print()


# TYPE 3: Recursive Functions
print("3. RECURSIVE FUNCTIONS - Functions that call themselves")
print("-" * 50)

def factorial(n: int) -> int:
    """
    Recursive function to calculate factorial.
    Base case: n == 0 or n == 1 → return 1
    Recursive case: n * factorial(n-1)
    """
    # Base case - prevents infinite recursion
    if n <= 1:
        return 1
    
    # Recursive case - function calls itself with smaller input
    return n * factorial(n - 1)

print(f"Factorial of 5: {factorial(5)}")
print(f"Factorial of 6: {factorial(6)}")
print()


# Example: Recursive countdown
def countdown(n: int) -> None:
    """Recursively count down from n to 0."""
    if n < 0:
        print("🎉 Blast off!")
        return
    
    print(f"Countdown: {n}")
    countdown(n - 1)

countdown(5)
print()


# Example: Recursive sum of list
def sum_list(numbers: list) -> int:
    """
    Recursively sum all numbers in a list.
    Base case: empty list → 0
    Recursive case: first element + sum of rest
    """
    if not numbers:  # Base case: empty list
        return 0
    
    return numbers[0] + sum_list(numbers[1:])  # Recursive case

result = sum_list([10, 20, 30, 40])
print(f"Sum of [10, 20, 30, 40]: {result}")
print()


# TYPE 4: Lambda Functions (Anonymous Functions)
print("4. LAMBDA FUNCTIONS - Inline anonymous functions")
print("-" * 50)

# Simple lambda
square = lambda x: x ** 2
print(f"Lambda square(5): {square(5)}")

# Lambda with multiple parameters
add = lambda x, y: x + y
print(f"Lambda add(3, 4): {add(3, 4)}")
print()


# Lambda with filter()
print("Using Lambda with filter():")
colors = ['red', 'light', 'long', 'green', 'laser']
short_words = list(filter(lambda word: len(word) < 6, colors))
print(f"Original: {colors}")
print(f"Filtered (< 6 chars): {short_words}")
print()


# Lambda with map()
print("Using Lambda with map():")
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(f"Original: {numbers}")
print(f"Doubled: {doubled}")
print()


# Lambda with sorted()
print("Using Lambda with sorted():")
orders = [
    {'customer': 'Aman', 'amount': 500},
    {'customer': 'Priya', 'amount': 1200},
    {'customer': 'Raj', 'amount': 800}
]
sorted_orders = sorted(orders, key=lambda x: x['amount'], reverse=True)
print("Orders sorted by amount (highest first):")
for order in sorted_orders:
    print(f"  {order['customer']}: ₹{order['amount']}")
print()


# TYPE 5: Higher-Order Functions
print("5. HIGHER-ORDER FUNCTIONS - Functions that operate on functions")
print("-" * 50)

def apply_operation(a: int, b: int, operation) -> int:
    """
    Higher-order function: Takes a function as parameter.
    
    Parameters:
        a, b: Numbers
        operation: A function to apply
    
    Returns:
        Result of operation(a, b)
    """
    return operation(a, b)

# Define some operations
def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y if y != 0 else 0

# Use higher-order function
print(f"apply_operation(20, 4, multiply): {apply_operation(20, 4, multiply)}")
print(f"apply_operation(20, 4, divide): {apply_operation(20, 4, divide)}")
print(f"apply_operation(20, 4, lambda x,y: x+y): {apply_operation(20, 4, lambda x,y: x+y)}")
print()


# TYPE 6: Decorators (Functions that modify functions)
print("6. DECORATORS - Functions that modify other functions")
print("-" * 50)

def add_logger(func):
    """Decorator that adds logging to a function."""
    def wrapper(*args, **kwargs):
        print(f"→ Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"← {func.__name__} returned: {result}")
        return result
    return wrapper

@add_logger
def greet(name, greeting="Hello"):
    """Greet someone."""
    return f"{greeting}, {name}!"

print(greet("Aman"))
print()
print(greet("Priya", greeting="Hi"))
print()


# PRACTICAL EXAMPLE: Combining Function Types
print("=" * 60)
print("PRACTICAL EXAMPLE - Receipt Generator")
print("=" * 60)

def generate_receipt(customer: str, *items, **prices):
    """
    Generate receipt using multiple function concepts.
    """
    print(f"\n{'RECEIPT':-^40}")
    print(f"Customer: {customer}")
    print("-" * 40)
    
    # Using lambda to calculate item total
    calculate_item_total = lambda price, qty: price * qty
    
    total = 0
    for item in items:
        price = prices.get(item, 0)
        item_total = calculate_item_total(price, 1)
        total += item_total
        print(f"{item:<20} ₹{price:>6.2f}")
    
    print("-" * 40)
    
    # Apply tax using pure function concept
    def apply_tax(amount, rate=0.18):
        return amount * (1 + rate)
    
    final_total = apply_tax(total)
    print(f"{'Subtotal':<20} ₹{total:>6.2f}")
    print(f"{'Tax (18%)':<20} ₹{final_total - total:>6.2f}")
    print(f"{'TOTAL':<20} ₹{final_total:>6.2f}")
    print("-" * 40)
    
    return final_total

# Generate receipt
generate_receipt(
    "Aman",
    "Masala Chai", "Samosa", "Biscuit",
    **{
        "Masala Chai": 50,
        "Samosa": 30,
        "Biscuit": 20
    }
)

print()
print("=" * 60)
print("KEY CONCEPTS - Function Types:")
print("=" * 60)
print("✓ Pure functions: Same input → Same output, no side effects")
print("✓ Impure functions: Have side effects, modify state")
print("✓ Recursive: Function calls itself with smaller input")
print("✓ Lambda: Anonymous inline functions for simple operations")
print("✓ Higher-order: Functions that take/return other functions")
print("✓ Decorators: Modify behavior of other functions")
