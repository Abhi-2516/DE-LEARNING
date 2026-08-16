"""
While Loops
Project: Temperature Monitoring & ATM Simulator
"""

def temperature_monitor():
    """
    Monitor temperature increase with while loop.
    Demonstrates basic while loop with condition.
    """
    print("=== Temperature Monitoring ===")
    temp = 40
    
    while temp <= 100:
        print(f"Current temperature: {temp}°C")
        temp = temp + 15
    
    print("Tea is ready and boiled!")


def simulate_atm_withdrawals(balance: int, withdrawals: list[int]) -> list[str]:
    """
    Simulate ATM withdrawal process.
    
    Args:
        balance: Initial account balance
        withdrawals: List of withdrawal amounts
    
    Returns:
        List of transaction messages
        
    Example:
        >>> simulate_atm_withdrawals(1000, [200, 300, 600])
        ['Withdrawn: 200', 'Withdrawn: 300', 'Insufficient funds for requested amount: 600', 'Remaining Balance: 500']
    """
    result = []
    index = 0
    
    while index < len(withdrawals):
        amount = withdrawals[index]
        if amount <= balance:
            balance -= amount
            result.append(f"Withdrawn: {amount}")
        else:
            result.append(f"Insufficient funds for requested amount: {amount}")
        index += 1
    
    result.append(f"Remaining Balance: {balance}")
    return result


def countdown_timer(seconds: int):
    """
    Simple countdown timer using while loop.
    
    Args:
        seconds: Number of seconds to count down
    """
    print(f"\n=== Countdown Timer ({seconds} seconds) ===")
    while seconds > 0:
        print(f"Time remaining: {seconds} seconds")
        seconds -= 1
    print("Time's up!")


def user_input_validator():
    """
    Repeatedly ask user for valid input using while loop.
    Demonstrates while loop with user input.
    """
    print("\n=== Input Validator ===")
    attempts = 0
    max_attempts = 3
    
    while attempts < max_attempts:
        try:
            age = int(input(f"Enter your age (Attempt {attempts + 1}/{max_attempts}): "))
            if age < 0 or age > 150:
                print("Please enter a valid age between 0 and 150")
                attempts += 1
            else:
                print(f"Thank you! You are {age} years old.")
                break
        except ValueError:
            print("Invalid input. Please enter a number.")
            attempts += 1
    
    if attempts == max_attempts:
        print("Maximum attempts exceeded!")


def password_checker():
    """
    Prompt user until correct password is entered.
    Demonstrates while True with break.
    """
    print("\n=== Password Checker ===")
    correct_password = "secret123"
    
    while True:
        password = input("Enter password: ")
        if password == correct_password:
            print("Access granted!")
            break
        else:
            print("Incorrect password. Try again.")


def sum_until_negative():
    """
    Sum numbers until user enters negative number.
    Demonstrates while loop with running calculation.
    """
    print("\n=== Sum Calculator ===")
    print("Enter numbers (negative to stop):")
    total = 0
    
    while True:
        try:
            num = int(input("Enter a number: "))
            if num < 0:
                break
            total += num
        except ValueError:
            print("Please enter a valid number")
    
    print(f"Total sum: {total}")


def multiplication_drill(number: int, max_times: int = 10):
    """
    Drill multiplication tables using while loop.
    
    Args:
        number: Number to drill
        max_times: Maximum multiplier (default 10)
    """
    print(f"\n=== Multiplication Drill: {number} ===")
    i = 1
    
    while i <= max_times:
        print(f"{number} x {i} = {number * i}")
        i += 1


if __name__ == "__main__":
    # Temperature monitor
    temperature_monitor()
    
    # ATM simulator
    print("\n=== ATM Withdrawal Simulator ===")
    initial_balance = 1000
    withdrawals = [200, 300, 150, 400]
    transactions = simulate_atm_withdrawals(initial_balance, withdrawals)
    for transaction in transactions:
        print(transaction)
    
    # Countdown timer
    countdown_timer(5)
    
    # Multiplication drill
    multiplication_drill(7)
    
    # Uncomment to test interactive functions:
    # user_input_validator()
    # password_checker()
    # sum_until_negative()
