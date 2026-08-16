"""
Basic For Loops
Project: Tea Token Dispenser & Batch Processing
"""

def tea_token_dispenser():
    """
    Simple tea token dispenser system.
    Demonstrates basic for loop with range().
    """
    print("=== Tea Token Dispenser ===")
    for token in range(1, 11):
        print(f"Serving chai with token #{token}")


def tea_batch_processor():
    """
    Batch processing system for tea stall.
    Demonstrates iterating through numeric sequence.
    """
    print("\n=== Tea Batch Processor ===")
    for batch in range(1, 5):
        print(f"Batch {batch} is being prepared...")


def multiplication_table(number: int) -> list[str]:
    """
    Generate multiplication table for a given number.
    
    Args:
        number: The number to generate table for
    
    Returns:
        List of strings showing multiplication results
        
    Example:
        >>> multiplication_table(3)
        ['3 x 1 = 3', '3 x 2 = 6', ..., '3 x 10 = 30']
    """
    result = []
    for i in range(1, 11):
        result.append(f"{number} x {i} = {number * i}")
    return result


if __name__ == "__main__":
    # Run basic loops
    tea_token_dispenser()
    tea_batch_processor()
    
    # Test multiplication table
    print("\n=== Multiplication Table ===")
    table = multiplication_table(5)
    for item in table:
        print(item)
