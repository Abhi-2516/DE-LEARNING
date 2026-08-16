"""
Advanced Loop Patterns
Project: Discount Calculator & Walrus Operator
"""

def discount_calculator_with_dict():
    """
    Calculate discounts using dictionary lookup in loops.
    Demonstrates efficient pattern for handling multiple cases.
    """
    print("=== Discount Calculator ===")
    
    users = [
        {"id": 1, "total": 100, "coupon": "P20"},
        {"id": 2, "total": 150, "coupon": "F10"},
        {"id": 3, "total": 80, "coupon": "P50"}
    ]
    
    discount = {
        "P20": (0.2, 0),      # 20% discount
        "F10": (0.5, 0),      # 50% discount (flat)
        "P50": (0, 10),       # Fixed 10 rupee discount
    }
    
    for user in users:
        percent, fixed = discount.get(user["coupon"], (0, 0))
        discount_amount = user["total"] * percent + fixed
        final_amount = user["total"] - discount_amount
        
        print(f"User {user['id']}: Paid {user['total']}, Discount: {discount_amount}, Final: {final_amount}")


def walrus_operator_example():
    """
    Demonstrate walrus operator (:=) for assignment within conditions.
    Python 3.8+ feature for more concise code.
    """
    print("\n=== Walrus Operator (:=) ===")
    
    value = 13
    if (remainder := value % 5):  # Assign and check in one line
        print(f"Value: {value}, Remainder: {remainder}")


def validate_password_with_walrus():
    """
    Validate password length using walrus operator.
    Demonstrates practical use of := operator.
    """
    print("\n=== Password Validation with Walrus ===")
    password = "secure123"
    
    if (pwd_length := len(password)) >= 8:
        print(f"Password accepted! Length: {pwd_length} characters")
    else:
        print(f"Password too short ({pwd_length} characters). Minimum 8 required.")


def process_data_with_walrus():
    """
    Process data entries and filter using walrus operator.
    Demonstrates walrus in loop conditions.
    """
    print("\n=== Data Processing with Walrus ===")
    data = [10, 25, 30, 5, 45, 8, 100]
    
    # Find first value greater than 40
    for value in data:
        if (squared := value ** 2) > 1600:  # Assign and check
            print(f"Found: {value}, Squared: {squared}")
            break


def iterate_dictionary_simple():
    """
    Iterate through dictionary items.
    Demonstrates basic dictionary looping.
    """
    print("\n=== Iterate Dictionary ===")
    student_scores = {
        "Alice": 95,
        "Bob": 87,
        "Charlie": 92
    }
    
    for name, score in student_scores.items():
        print(f"{name}: {score}")


def iterate_dictionary_keys():
    """
    Iterate through dictionary keys only.
    """
    print("\n=== Iterate Dictionary Keys ===")
    products = {
        "chai": 50,
        "coffee": 80,
        "tea": 40
    }
    
    for product in products.keys():
        print(f"Product: {product}")


def iterate_dictionary_values():
    """
    Iterate through dictionary values only.
    """
    print("\n=== Iterate Dictionary Values ===")
    inventory = {
        "chai": 100,
        "coffee": 75,
        "tea": 120
    }
    
    total = 0
    for quantity in inventory.values():
        total += quantity
    
    print(f"Total items in stock: {total}")


def create_discount_lookup():
    """
    Create efficient discount lookup table.
    Demonstrates dictionary as alternative to if-elif-else.
    """
    print("\n=== Discount Lookup Table ===")
    
    # Instead of multiple if-elif statements
    discount_rates = {
        "gold": 0.20,
        "silver": 0.15,
        "bronze": 0.10,
        "regular": 0.05
    }
    
    customers = ["gold", "silver", "regular", "bronze"]
    base_price = 1000
    
    for customer_type in customers:
        discount_rate = discount_rates.get(customer_type, 0)
        final_price = base_price * (1 - discount_rate)
        print(f"{customer_type.capitalize()}: {base_price} -> {final_price} (Discount: {discount_rate * 100}%)")


def nested_dictionary_iteration():
    """
    Iterate through nested dictionary structures.
    """
    print("\n=== Nested Dictionary Iteration ===")
    
    shop = {
        "beverages": {
            "chai": 50,
            "coffee": 80,
            "tea": 40
        },
        "snacks": {
            "samosa": 20,
            "cookie": 15,
            "cake": 200
        }
    }
    
    for category, items in shop.items():
        print(f"\n{category.upper()}:")
        for item, price in items.items():
            print(f"  {item}: Rs {price}")


def count_occurrences(items: list[str]) -> dict:
    """
    Count occurrences of each item using dictionary in loop.
    
    Args:
        items: List of items to count
    
    Returns:
        Dictionary with counts
    """
    counts = {}
    for item in items:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts


def group_by_criteria(numbers: list[int]) -> dict:
    """
    Group numbers by odd/even using dictionary.
    
    Args:
        numbers: List of numbers
    
    Returns:
        Dictionary with 'odd' and 'even' keys
    """
    groups = {"odd": [], "even": []}
    for num in numbers:
        if num % 2 == 0:
            groups["even"].append(num)
        else:
            groups["odd"].append(num)
    return groups


if __name__ == "__main__":
    # Discount calculator with dictionary
    discount_calculator_with_dict()
    
    # Walrus operator examples
    walrus_operator_example()
    validate_password_with_walrus()
    process_data_with_walrus()
    
    # Dictionary iteration examples
    iterate_dictionary_simple()
    iterate_dictionary_keys()
    iterate_dictionary_values()
    
    # Discount lookup table
    create_discount_lookup()
    
    # Nested dictionary
    nested_dictionary_iteration()
    
    # Count occurrences
    print("\n=== Count Occurrences ===")
    items = ["apple", "banana", "apple", "cherry", "banana", "apple"]
    counts = count_occurrences(items)
    print(counts)
    
    # Group by criteria
    print("\n=== Group Numbers ===")
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    grouped = group_by_criteria(numbers)
    print(grouped)
