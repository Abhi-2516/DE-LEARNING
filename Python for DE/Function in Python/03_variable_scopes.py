"""
Functions in Python - Variable Scopes
======================================
Learn: Understanding Local, Enclosing, Global, and Built-in scopes (LEGB Rule)
"""

print("=" * 60)
print("LEGB Rule: Local → Enclosing → Global → Built-in")
print("=" * 60)
print()

# SCOPE 1: Local Scope
print("\n1. LOCAL SCOPE - Variables inside a function")
print("-" * 50)

def serve_chai():
    """Variables defined here are local to this function."""
    chai_type = "Masala"  # Local variable
    print(f"Inside function (Local): {chai_type}")

chai_type = "Lemon"  # Global variable
serve_chai()
print(f"Outside function (Global): {chai_type}\n")


# SCOPE 2: Enclosing Scope (Closure)
print("2. ENCLOSING SCOPE - Variables in outer function")
print("-" * 50)

def chai_counter():
    """Outer function defines a variable."""
    chai_order = "lemon"  # Enclosing scope
    
    def print_order():
        """Inner function - accesses outer variable."""
        chai_order = "Ginger"  # Creates new local variable (shadows enclosing)
        print(f"Inner function: {chai_order}")
    
    print_order()
    print(f"Outer function: {chai_order}")

chai_counter()
print()


# SCOPE 3: Global Scope
print("3. GLOBAL SCOPE - Variables at module level")
print("-" * 50)

global_chai = "Tulsi"  # Global variable

def check_global():
    """Access global variable without modification."""
    print(f"Reading global: {global_chai}")

check_global()
print(f"Direct access: {global_chai}\n")


# SCOPE 4: Using 'global' keyword to modify global variable
print("4. MODIFYING GLOBAL VARIABLES - Using 'global' keyword")
print("-" * 50)

counter = 0  # Global variable

def increment_counter():
    """Modify global variable using 'global' keyword."""
    global counter
    counter += 1
    print(f"Counter inside function: {counter}")

print(f"Initial counter: {counter}")
increment_counter()
increment_counter()
print(f"Final counter: {counter}\n")


# SCOPE 5: Using 'nonlocal' keyword
print("5. NONLOCAL SCOPE - Modify enclosing function variable")
print("-" * 50)

def update_order():
    """Outer function with variable."""
    chai_type = "elachi"  # Enclosing scope
    
    def kitchen():
        """Modify enclosing variable using 'nonlocal'."""
        nonlocal chai_type
        chai_type = "kesar"
        print(f"Kitchen modified: {chai_type}")
    
    kitchen()
    print(f"Back in order: {chai_type}")

update_order()
print()


# SCOPE 6: Complex example - Global vs Nonlocal
print("6. REAL WORLD EXAMPLE - Transaction Processing")
print("-" * 50)

loyalty_points = 0  # Global variable

def process_transactions(transactions: list) -> int:
    """
    Process transactions and update loyalty points.
    
    Parameters:
        transactions (list): List of transaction amounts
    
    Returns:
        int: Total processed amount
    """
    
    def apply_bonus():
        """Inner function using nonlocal."""
        nonlocal total
        if total > 1000:
            total += 50  # Bonus for high spenders
            print("🎁 Bonus of ₹50 applied!")
    
    total = 0
    
    # Sum all transactions
    for amount in transactions:
        total += amount
    
    # Apply bonus if applicable
    apply_bonus()
    
    # Update global loyalty points
    global loyalty_points
    loyalty_points += total // 100  # Earn 1 point per ₹100
    
    return total

# Test transactions
transactions = [400, 600, 200]
total_amount = process_transactions(transactions)
print(f"Total Amount: ₹{total_amount}")
print(f"Loyalty Points Earned: {loyalty_points}\n")


# SCOPE 7: Built-in Scope
print("7. BUILT-IN SCOPE - Python built-in functions and constants")
print("-" * 50)

def demonstrate_builtins():
    """Access built-in functions and constants."""
    # Built-in functions: print, len, range, etc.
    items = ['chai', 'coffee', 'juice']
    print(f"Built-in function len(): {len(items)}")
    
    # Built-in constants
    print(f"Built-in constant True: {True}")
    print(f"Built-in constant None: {None}")

demonstrate_builtins()
print()


# KEY SUMMARY TABLE
print("=" * 60)
print("SCOPE SUMMARY TABLE")
print("=" * 60)
print(f"{'Scope':<15} {'Access':<12} {'Modify':<20}")
print("-" * 60)
print(f"{'Local':<15} {'Yes':<12} {'Yes (direct)':<20}")
print(f"{'Enclosing':<15} {'Yes':<12} {'Yes (nonlocal)':<20}")
print(f"{'Global':<15} {'Yes':<12} {'Yes (global)':<20}")
print(f"{'Built-in':<15} {'Yes':<12} {'No':<20}")
print()

# Key Takeaways:
print("=" * 60)
print("KEY CONCEPTS - Variable Scopes:")
print("=" * 60)
print("✓ LEGB Rule: Python searches scopes in order")
print("✓ Local: Variables inside a function")
print("✓ Enclosing: Variables in outer function (closures)")
print("✓ Global: Variables at module level")
print("✓ Built-in: Python's built-in functions and constants")
print("✓ 'global' keyword: Modify global variables")
print("✓ 'nonlocal' keyword: Modify enclosing variables")
