"""
Zip Function
Project: Order Summary & Student Scores Report
"""

def order_summary():
    """
    Create order summary combining names and amounts.
    Demonstrates zip() function pairing two lists.
    """
    print("=== Order Summary ===")
    names = ["Abhi", "Sam", "Ram", "Hitesh"]
    bills = [100, 2000, 500, 1400]
    
    for name, amount in zip(names, bills):
        print(f"{name} paid: Rs {amount}")


def generate_score_report(names: list[str], scores: list[int]) -> list[str]:
    """
    Generate student score report by pairing names with scores.
    
    Args:
        names: List of student names
        scores: List of student scores
    
    Returns:
        List of formatted score reports
        
    Example:
        >>> generate_score_report(['Alice', 'Bob'], [95, 87])
        ['Alice scored 95 marks', 'Bob scored 87 marks']
    """
    report = []
    for name, score in zip(names, scores):
        report.append(f"{name} scored {score} marks")
    return report


def employee_salary_slip(employees: list[str], salaries: list[int]) -> list[str]:
    """
    Generate salary slips for employees.
    
    Args:
        employees: List of employee names
        salaries: List of corresponding salaries
    
    Returns:
        List of salary slip messages
    """
    slips = []
    for emp, salary in zip(employees, salaries):
        slips.append(f"{emp}: Rs {salary} salary credited")
    return slips


def match_questions_with_answers(questions: list[str], answers: list[str]) -> list[str]:
    """
    Match questions with their correct answers.
    
    Args:
        questions: List of questions
        answers: List of corresponding answers
    
    Returns:
        List of formatted question-answer pairs
    """
    pairs = []
    for q_num, (question, answer) in enumerate(zip(questions, answers), start=1):
        pairs.append(f"Q{q_num}: {question}\nA{q_num}: {answer}\n")
    return pairs


def product_inventory(products: list[str], quantities: list[int]) -> dict:
    """
    Create inventory dictionary from products and quantities.
    
    Args:
        products: List of product names
        quantities: List of available quantities
    
    Returns:
        Dictionary mapping products to quantities
    """
    inventory = {}
    for product, qty in zip(products, quantities):
        inventory[product] = qty
    return inventory


def display_weather_forecast(cities: list[str], temperatures: list[int]):
    """
    Display weather forecast for multiple cities.
    
    Args:
        cities: List of city names
        temperatures: List of temperatures
    """
    print("=== Weather Forecast ===")
    for city, temp in zip(cities, temperatures):
        status = "Hot" if temp > 30 else "Moderate" if temp > 20 else "Cold"
        print(f"{city}: {temp}°C ({status})")


if __name__ == "__main__":
    # Order summary
    order_summary()
    
    # Score report
    print("\n=== Score Report ===")
    names = ["Alice", "Bob", "Charlie", "Diana"]
    scores = [95, 87, 92, 78]
    report = generate_score_report(names, scores)
    for line in report:
        print(line)
    
    # Salary slips
    print("\n=== Salary Slips ===")
    employees = ["John", "Jane", "Jack"]
    salaries = [50000, 55000, 60000]
    slips = employee_salary_slip(employees, salaries)
    for slip in slips:
        print(slip)
    
    # Q&A matching
    print("\n=== Question-Answer Pairs ===")
    questions = ["What is Python?", "Define loop?"]
    answers = ["A programming language", "Repeated execution of code"]
    qa_pairs = match_questions_with_answers(questions, answers)
    for pair in qa_pairs:
        print(pair)
    
    # Inventory
    print("\n=== Product Inventory ===")
    products = ["Chai", "Coffee", "Tea"]
    quantities = [50, 35, 45]
    inventory = product_inventory(products, quantities)
    for product, qty in inventory.items():
        print(f"{product}: {qty} units")
    
    # Weather
    cities = ["Mumbai", "Delhi", "Bangalore"]
    temps = [35, 28, 22]
    display_weather_forecast(cities, temps)
