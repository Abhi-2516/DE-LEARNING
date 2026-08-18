"""
Functions in Python - Advanced Arguments
=========================================
Learn: Positional, Keyword, *args, **kwargs, Default values, Type Hints
"""

print("=" * 60)
print("ADVANCED ARGUMENT HANDLING")
print("=" * 60)
print()

# EXAMPLE 1: Positional Arguments
print("\n1. POSITIONAL ARGUMENTS - Order matters!")
print("-" * 50)

def make_chai(tea, milk, sugar):
    """Make chai with specific ingredients."""
    print(f"Making {tea} chai with {milk} milk and {sugar} sugar")

make_chai("Darjeeling", "Yes", "Low")  # Positional arguments
print()


# EXAMPLE 2: Keyword Arguments
print("2. KEYWORD ARGUMENTS - Order doesn't matter")
print("-" * 50)

# Same function, different order using keywords
make_chai(tea="Green", sugar="Medium", milk="No")
print()


# EXAMPLE 3: Mixing Positional and Keyword
print("3. MIXING POSITIONAL AND KEYWORD ARGUMENTS")
print("-" * 50)

make_chai("Assam", milk="Yes", sugar="High")
print()


# EXAMPLE 4: *args - Variable number of positional arguments
print("4. *ARGS - Variable number of positional arguments")
print("-" * 50)

def make_special_chai(*ingredients):
    """
    Make special chai with any number of ingredients.
    
    Parameters:
        *ingredients: Variable number of ingredient names
    """
    print("Making special chai with:")
    for ingredient in ingredients:
        print(f"  - {ingredient}")
    return ingredients

result = make_special_chai("Cinnamon", "Cardamom", "Clove", "Ginger")
print()


# EXAMPLE 5: **kwargs - Variable keyword arguments
print("5. **KWARGS - Variable keyword arguments")
print("-" * 50)

def order_chai(**preferences):
    """
    Order chai with various preferences.
    
    Parameters:
        **preferences: Keyword arguments for preferences
    """
    print("Chai order details:")
    for key, value in preferences.items():
        print(f"  {key.capitalize()}: {value}")

order_chai(temperature="Hot", sweetness="Medium", spice="High", milk="Double")
print()


# EXAMPLE 6: Combining *args and **kwargs
print("6. COMBINING *ARGS AND **KWARGS")
print("-" * 50)

def prepare_order(customer_name, *items, **extras):
    """
    Prepare order combining all argument types.
    
    Parameters:
        customer_name: Required positional argument
        *items: Variable positional arguments (items to order)
        **extras: Variable keyword arguments (extras/preferences)
    """
    print(f"\nOrder for: {customer_name}")
    
    if items:
        print("Items ordered:")
        for item in items:
            print(f"  - {item}")
    
    if extras:
        print("Extra preferences:")
        for key, value in extras.items():
            print(f"  - {key}: {value}")

prepare_order("Aman", "Chai", "Samosa", "Biscuit", 
              temperature="Hot", sweetness="Medium", foam="Yes")
print()


# EXAMPLE 7: Default Arguments
print("7. DEFAULT ARGUMENTS - Providing default values")
print("-" * 50)

def serve_drink(drink="Water", quantity=1, temperature="Room"):
    """
    Serve a drink with default parameters.
    
    Parameters:
        drink (str): Type of drink (default: Water)
        quantity (int): Number of servings (default: 1)
        temperature (str): Serving temperature (default: Room)
    """
    print(f"Serving {quantity} serving(s) of {temperature} {drink}")

serve_drink()
serve_drink("Tea")
serve_drink("Tea", 2, "Hot")
print()


# EXAMPLE 8: ⚠️ CAREFUL - Mutable Default Arguments (Common Pitfall)
print("8. ⚠️ COMMON PITFALL - Mutable Default Arguments")
print("-" * 50)

# ❌ WRONG WAY - Using mutable object as default
def chai_order_wrong(order=[]):
    """❌ Wrong: Using list as default argument."""
    order.append("Masala")
    return order

print("❌ Wrong way (mutable default):")
print(f"First call: {chai_order_wrong()}")
print(f"Second call: {chai_order_wrong()}")  # Unexpected! List persists!
print()

# ✅ CORRECT WAY - Using None with type checking
def chai_order_correct(order=None):
    """✅ Correct: Using None as default, create new list."""
    if order is None:
        order = []
    order.append("Masala")
    return order

print("✅ Correct way (None as default):")
print(f"First call: {chai_order_correct()}")
print(f"Second call: {chai_order_correct()}")  # Fresh list each time!
print()


# EXAMPLE 9: Type Hints - Documenting argument types
print("9. TYPE HINTS - Making code self-documenting")
print("-" * 50)

def calculate_total_cost(
    base_price: float,
    quantity: int,
    discount: float = 0.0,
    tax_rate: float = 0.18
) -> float:
    """
    Calculate total cost with discount and tax.
    
    Parameters:
        base_price (float): Price per unit
        quantity (int): Number of units
        discount (float): Discount percentage (0-100)
        tax_rate (float): Tax percentage (default: 18%)
    
    Returns:
        float: Final total cost
    """
    subtotal = base_price * quantity
    discounted = subtotal * (1 - discount / 100)
    total = discounted * (1 + tax_rate)
    return total

total_cost = calculate_total_cost(100, 5, discount=10, tax_rate=0.18)
print(f"Total Cost: ₹{total_cost:.2f}\n")


# EXAMPLE 10: Complex Real-World Example - Invoice Generator
print("10. REAL-WORLD EXAMPLE - Invoice Generation")
print("-" * 50)

def generate_invoice(
    customer_name: str = "Guest",
    *items: str,
    **charges: float
) -> str:
    """
    Generate invoice with all argument types.
    
    Parameters:
        customer_name (str): Customer name (default: "Guest")
        *items (str): Items purchased
        **charges (float): Named charges (tax, shipping, etc.)
    
    Returns:
        str: Formatted invoice
    """
    total = 0.0
    invoice_lines = [
        "=" * 40,
        f"INVOICE FOR {customer_name.upper()}",
        "=" * 40
    ]
    
    if items:
        invoice_lines.append("\nItems Purchased:")
        for item in items:
            invoice_lines.append(f"  ✓ {item}")
    
    if charges:
        invoice_lines.append("\nCharges:")
        for label, amount in charges.items():
            invoice_lines.append(f"  {label.capitalize()}: ₹{amount}")
            total += amount
    
    invoice_lines.append("-" * 40)
    invoice_lines.append(f"Total Amount Due: ₹{total:.2f}")
    invoice_lines.append("=" * 40)
    
    return "\n".join(invoice_lines)

# Generate sample invoice
invoice = generate_invoice(
    "Rahul Singh",
    "Masala Chai",
    "Samosa",
    "Biscuit",
    tax=54.00,
    delivery=30.00,
    discount=20.00
)
print(invoice)
print()

# Key Takeaways:
print("=" * 60)
print("KEY CONCEPTS - Advanced Arguments:")
print("=" * 60)
print("✓ Positional arguments: order matters")
print("✓ Keyword arguments: name matters, order doesn't")
print("✓ *args: accept any number of positional arguments")
print("✓ **kwargs: accept any number of keyword arguments")
print("✓ Default values: provide sensible defaults")
print("✓ Type hints: document expected types")
print("✓ Order matters: positional → *args → keyword → **kwargs")
print("✓ Avoid mutable defaults (use None instead)")
