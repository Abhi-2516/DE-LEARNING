"""
For Loops with Lists
Project: Order Processing & Task Management
"""

def process_orders():
    """
    Process orders for multiple customers.
    Demonstrates iterating through a list directly.
    """
    print("=== Processing Orders ===")
    orders = ["Abhi", "Sonu", "Hitesh"]
    
    for name in orders:
        print(f"Order is ready for {name}")


def mark_completed_tasks(tasks: list[str]) -> list[str]:
    """
    Mark all tasks in a list as completed.
    
    Args:
        tasks: List of task names
    
    Returns:
        List of completed task messages
        
    Example:
        >>> mark_completed_tasks(['Buy groceries', 'Clean room'])
        ['Completed: Buy groceries', 'Completed: Clean room']
    """
    completed = []
    for task in tasks:
        completed.append(f"Completed: {task}")
    return completed


def print_products():
    """
    Print a product menu.
    Demonstrates accessing each element in a list.
    """
    print("\n=== Product Menu ===")
    products = ["Chai", "Coffee", "Hot Chocolate", "Tea"]
    
    for product in products:
        print(f"- {product} available")


def calculate_total_price(prices: list[float]) -> float:
    """
    Calculate total price of items.
    
    Args:
        prices: List of individual prices
    
    Returns:
        Sum of all prices
    """
    total = 0
    for price in prices:
        total += price
    return total


if __name__ == "__main__":
    # Process orders
    process_orders()
    
    # Mark tasks as completed
    print("\n=== Task Completion ===")
    tasks = ["Write report", "Send email", "Update database"]
    completed_tasks = mark_completed_tasks(tasks)
    for task in completed_tasks:
        print(task)
    
    # Print products
    print_products()
    
    # Calculate total
    print("\n=== Price Calculation ===")
    prices = [100, 150, 200, 75]
    total = calculate_total_price(prices)
    print(f"Total price: ${total}")
