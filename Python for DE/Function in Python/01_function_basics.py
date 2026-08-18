"""
Functions in Python - Basics
=============================
Learn: How functions help remove code duplication and create reusable code.
Key Concept: Parameters (defined in function) vs Arguments (passed during call)
"""

# Example 1: Simple function with parameters and arguments
def print_order(name, types):
    """
    Print a chai order.
    
    Parameters:
        name (str): Customer name
        types (str): Type of chai
    """
    print(f"{name} ordered chai: {types}")

# Function calls with arguments
print_order("aman", "masala")
print_order("hitesh", "mint")
print_order("priya", "ginger")


# Example 2: Splitting complex tasks into functions
# Task: Create a monthly report for a cafe
def fetch_sales():
    """Fetch sales data from database."""
    print("Fetching the sale data...")
    return [1000, 1500, 2000, 1800]

def filter_valid_sales(sales):
    """Filter valid sales data."""
    print("Filtering valid sales data...")
    return [s for s in sales if s > 0]

def summarize_data(sales):
    """Summarize the data."""
    print("Summarizing the data...")
    return sum(sales)

def generate_report():
    """Generate monthly report by orchestrating all functions."""
    sales = fetch_sales()
    valid_sales = filter_valid_sales(sales)
    total = summarize_data(valid_sales)
    print(f"Total sales: ₹{total}\n")

generate_report()


# Example 3: Function to hide implementation details (Abstraction)
def get_input():
    """Get user input."""
    print("Getting user input...")

def validate_input():
    """Validate user input."""
    print("Validating data...")

def save_to_db():
    """Save data to database."""
    print("Saving to database...")

def user_registration():
    """User registration workflow."""
    get_input()
    validate_input()
    save_to_db()
    print("User registration is complete!\n")

user_registration()

# Key Takeaways:
print("=" * 50)
print("KEY CONCEPTS - Function Basics:")
print("=" * 50)
print("1. Parameters: Variables defined in function definition")
print("2. Arguments: Values passed when calling a function")
print("3. Functions help avoid code duplication")
print("4. Functions split complex tasks into manageable pieces")
print("5. Functions hide implementation details (Abstraction)")
