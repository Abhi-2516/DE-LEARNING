"""
Loop Control Statements
Project: Menu Selection & Inventory Management
"""

def tea_menu_with_stock():
    """
    Display tea menu and skip out-of-stock items using continue.
    Demonstrates continue statement to skip iterations.
    """
    print("=== Tea Menu (Skip Out of Stock) ===")
    menu = ["Ginger", "Lemon", "Out of stock", "Discontinued", "Tulsi"]
    
    for item in menu:
        if item == "Out of stock":
            continue  # Skip this iteration
        if item == "Discontinued":
            print(f"NOTICE: {item} item found - stopping menu")
            break  # Exit loop completely
        print(f"✓ {item} chai - Available")


def find_target_number(numbers: list[int], target: int) -> bool:
    """
    Search for a target number in a list using break.
    
    Args:
        numbers: List of numbers to search
        target: Number to find
    
    Returns:
        True if found, False otherwise
    """
    print(f"\n=== Searching for {target} ===")
    for num in numbers:
        print(f"Checking {num}...")
        if num == target:
            print(f"Found {target}!")
            return True
    print(f"{target} not found")
    return False


def filter_even_numbers(numbers: list[int]) -> list[int]:
    """
    Filter even numbers using continue to skip odd ones.
    
    Args:
        numbers: List of numbers
    
    Returns:
        List containing only even numbers
    """
    result = []
    for num in numbers:
        if num % 2 == 1:  # Skip odd numbers
            continue
        result.append(num)
    return result


def process_orders_until_closure():
    """
    Process orders until shop closes using break.
    Demonstrates break in a realistic scenario.
    """
    print("\n=== Order Processing ===")
    orders = ["Order 1", "Order 2", "Shop Closed", "Order 3", "Order 4"]
    
    for order in orders:
        if order == "Shop Closed":
            print("Shop is closing! Stopping order processing.")
            break
        print(f"Processing: {order}")


def skip_invalid_entries(entries: list[str]):
    """
    Process entries, skipping empty ones using continue.
    
    Args:
        entries: List of entries (some may be empty)
    """
    print("\n=== Processing Entries (Skip Empty) ===")
    for entry in entries:
        if entry == "":
            continue  # Skip empty entries
        print(f"Processing: {entry}")


def search_password_in_list(passwords: list[str], target: str) -> int:
    """
    Find the position of a password in a list using break.
    
    Args:
        passwords: List of passwords
        target: Password to find
    
    Returns:
        Index of password, or -1 if not found
    """
    for index, pwd in enumerate(passwords):
        if pwd == target:
            return index
    return -1


def nested_loop_with_break():
    """
    Demonstrate break in nested loops.
    Shows how break only exits the innermost loop.
    """
    print("\n=== Nested Loop with Break ===")
    for i in range(1, 4):
        print(f"Outer loop: {i}")
        for j in range(1, 4):
            if j == 2:
                print(f"  Breaking inner loop at j={j}")
                break
            print(f"  Inner loop: {j}")


def continue_with_range():
    """
    Use continue to skip certain iterations.
    Demonstrates skipping multiples of 3.
    """
    print("\n=== Skip Multiples of 3 ===")
    for num in range(1, 11):
        if num % 3 == 0:
            continue  # Skip multiples of 3
        print(num, end=" ")
    print()  # Newline


def validate_user_input():
    """
    Validate input and use break when valid input is received.
    Demonstrates while True with break pattern.
    """
    print("\n=== Input Validation ===")
    while True:
        user_input = input("Enter 'exit' to quit: ")
        if user_input.lower() == "exit":
            print("Exiting program...")
            break
        if user_input.strip() == "":
            continue  # Skip empty input
        print(f"You entered: {user_input}")


def remove_duplicates(items: list[str]) -> list[str]:
    """
    Remove duplicate items from a list.
    Demonstrates continue for skipping duplicates.
    
    Args:
        items: List with potential duplicates
    
    Returns:
        List with duplicates removed
    """
    result = []
    for item in items:
        if item in result:
            continue  # Skip already added items
        result.append(item)
    return result


if __name__ == "__main__":
    # Tea menu with continue and break
    tea_menu_with_stock()
    
    # Find target number
    numbers = [10, 25, 30, 45, 50]
    find_target_number(numbers, 30)
    find_target_number(numbers, 100)
    
    # Filter even numbers
    print("\n=== Filter Even Numbers ===")
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    evens = filter_even_numbers(nums)
    print(f"Even numbers: {evens}")
    
    # Process orders until closure
    process_orders_until_closure()
    
    # Skip invalid entries
    skip_invalid_entries(["Data1", "", "Data2", "", "Data3"])
    
    # Nested loop with break
    nested_loop_with_break()
    
    # Continue with range
    continue_with_range()
    
    # Remove duplicates
    print("\n=== Remove Duplicates ===")
    items = ["apple", "banana", "apple", "cherry", "banana"]
    unique = remove_duplicates(items)
    print(f"Unique items: {unique}")
    
    # Uncomment to test interactive functions:
    # validate_user_input()
