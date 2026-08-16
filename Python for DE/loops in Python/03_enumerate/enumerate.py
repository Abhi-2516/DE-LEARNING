"""
Enumerate Function
Project: Tea Menu Board & Task Numbering
"""

def display_tea_menu():
    """
    Display numbered tea menu items.
    Demonstrates enumerate() function.
    """
    print("=== Tea Menu Board ===")
    menu = ["Green", "Lemon", "Spiced", "Mint"]
    
    for idx, item in enumerate(menu, start=1):
        print(f"{idx}. {item} chai")


def generate_numbered_tasks(tasks: list[str]) -> list[str]:
    """
    Generate numbered task list starting from 1.
    
    Args:
        tasks: List of task names
    
    Returns:
        List with formatted numbered tasks
        
    Example:
        >>> generate_numbered_tasks(['Buy milk', 'Write code'])
        ['1. Buy milk', '2. Write code']
    """
    numbered_tasks = []
    for index, task in enumerate(tasks, start=1):
        numbered_tasks.append(f"{index}. {task}")
    return numbered_tasks


def list_students_with_roll_numbers(students: list[str]) -> list[str]:
    """
    Create a roll number list for students starting from 1001.
    
    Args:
        students: List of student names
    
    Returns:
        List with formatted roll numbers
    """
    result = []
    for idx, name in enumerate(students, start=1001):
        result.append(f"Roll #{idx}: {name}")
    return result


def print_user_ranks(usernames: list[str]):
    """
    Print users with their rank (1st, 2nd, 3rd...).
    Demonstrates enumerate with position tracking.
    """
    print("\n=== User Rankings ===")
    for position, username in enumerate(usernames, start=1):
        ordinal = {1: "1st", 2: "2nd", 3: "3rd"}.get(position, f"{position}th")
        print(f"{ordinal} place: {username}")


def inventory_list(items: list[str]) -> list[str]:
    """
    Create an inventory list with item numbers.
    
    Args:
        items: List of inventory items
    
    Returns:
        Formatted inventory list
    """
    result = []
    for num, item in enumerate(items, start=1):
        result.append(f"Item {num}: {item}")
    return result


if __name__ == "__main__":
    # Display menu
    display_tea_menu()
    
    # Generate numbered tasks
    print("\n=== Numbered Tasks ===")
    tasks = ["Complete project", "Review code", "Deploy", "Monitor"]
    numbered = generate_numbered_tasks(tasks)
    for task in numbered:
        print(task)
    
    # Student roll numbers
    print("\n=== Student Roll Numbers ===")
    students = ["Alice", "Bob", "Charlie", "Diana"]
    rolls = list_students_with_roll_numbers(students)
    for roll in rolls:
        print(roll)
    
    # User rankings
    users = ["John", "Sarah", "Mike", "Emma"]
    print_user_ranks(users)
    
    # Inventory
    print("\n=== Inventory ===")
    items = ["Chai", "Coffee", "Tea", "Water"]
    inventory = inventory_list(items)
    for inv in inventory:
        print(inv)
