"""
Tea Stall Pricing System - If/Elif/Else Statement
Project: Dynamic Pricing Based on Cup Size
"""

def tea_stall_pricing():
    """
    A tea stall system with different prices for different cup sizes.
    Demonstrates if-elif-else conditional statements.
    """
    cup_type = input("Enter your cup type (small/medium/large): ").lower()
    
    if cup_type == "small":
        print("Price is: $10")
    elif cup_type == "medium":
        print("Price is: $15")
    elif cup_type == "large":
        print("Price is: $20")
    else:
        print("Unknown cup size. Please choose from small, medium, or large.")


if __name__ == "__main__":
    tea_stall_pricing()
