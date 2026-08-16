"""
Delivery Fees Calculator - Conditional Expression (Ternary Operator)
Project: Dynamic Delivery Fee Based on Order Amount
"""

def calculate_delivery_fees():
    """
    Calculates delivery fees based on order amount.
    Demonstrates the ternary/conditional expression operator.
    
    Rule: If order amount > $300, delivery is free, otherwise $30
    """
    order_amount = int(input("Enter order amount (in dollars): "))
    
    # Ternary operator: value_if_true if condition else value_if_false
    delivery_fees = 0 if order_amount > 300 else 30
    
    print(f"Order Amount: ${order_amount}")
    print(f"Delivery Fees: ${delivery_fees}")
    print(f"Total Amount: ${order_amount + delivery_fees}")


if __name__ == "__main__":
    calculate_delivery_fees()
