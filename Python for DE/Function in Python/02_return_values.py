"""
Functions in Python - Return Values
====================================
Learn: How to return values from functions and improve code traceability
"""

# Example 1: Function returning a single value
def calculate_bill(cups, price_per_cup):
    """Calculate total bill amount."""
    return cups * price_per_cup

my_bill = calculate_bill(3, 45)
print(f"Bill for 3 cups at ₹45 each: ₹{my_bill}\n")


# Example 2: Improving traceability with return values
def apply_vat(price, vat_rate=10):
    """
    Calculate final price with VAT.
    
    Parameters:
        price (float): Original price
        vat_rate (float): VAT percentage (default: 10)
    
    Returns:
        float: Final price including VAT
    """
    return price * (100 + vat_rate) / 100

# Process multiple orders
orders = [100, 200, 300]
print("Order Processing with VAT Calculation:")
print("-" * 40)

for price in orders:
    final_amount = apply_vat(price, 10)
    print(f"Original: ₹{price} → Final: ₹{final_amount:.2f}")

print()


# Example 3: Function returning different types
def get_discount(order_amount):
    """
    Calculate discount based on order amount.
    
    Returns:
        dict: Discount percentage and final amount
    """
    discount_percent = 0
    
    if order_amount >= 500:
        discount_percent = 15
    elif order_amount >= 300:
        discount_percent = 10
    elif order_amount >= 100:
        discount_percent = 5
    
    discount_amount = order_amount * (discount_percent / 100)
    final_amount = order_amount - discount_amount
    
    return {
        'original': order_amount,
        'discount_percent': discount_percent,
        'discount_amount': discount_amount,
        'final_amount': final_amount
    }

# Using function that returns dictionary
result = get_discount(450)
print("Discount Calculation:")
print("-" * 40)
print(f"Original Amount: ₹{result['original']}")
print(f"Discount: {result['discount_percent']}% (₹{result['discount_amount']:.2f})")
print(f"Final Amount: ₹{result['final_amount']:.2f}\n")


# Example 4: Function returning multiple values (tuple unpacking)
def process_order(item, quantity, price_per_item):
    """
    Process order and return multiple values.
    
    Returns:
        tuple: (subtotal, tax, total)
    """
    subtotal = quantity * price_per_item
    tax = subtotal * 0.18  # 18% tax
    total = subtotal + tax
    
    return subtotal, tax, total

# Unpacking return values
subtotal, tax, total = process_order("Masala Chai", 5, 50)
print("Order Processing - Multiple Return Values:")
print("-" * 40)
print(f"Subtotal: ₹{subtotal}")
print(f"Tax (18%): ₹{tax:.2f}")
print(f"Total: ₹{total:.2f}\n")


# Key Takeaways:
print("=" * 50)
print("KEY CONCEPTS - Return Values:")
print("=" * 50)
print("1. Use 'return' to send values back to caller")
print("2. Functions can return single or multiple values")
print("3. Multiple returns use tuple unpacking")
print("4. Functions can return different data types")
print("5. Return improves code traceability")
