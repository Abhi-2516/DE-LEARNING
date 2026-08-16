"""
Snack System - If/Else with Logical Operators
Project: Restaurant Snack Availability Checker
"""

def snack_availability():
    """
    A snack system that confirms order if customer asks for available items.
    Demonstrates if-else with logical operators (or).
    """
    snack = input("Enter your preferred snack: ").lower()
    
    print(f"User says: {snack}")
    
    if snack == "cookies" or snack == "samosa":
        print("Best choice!")
    else:
        print("No product available.")


if __name__ == "__main__":
    snack_availability()
