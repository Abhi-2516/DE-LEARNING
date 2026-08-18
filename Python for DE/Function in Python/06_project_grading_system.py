"""
PROJECT 1: Student Grading System
==================================
Problem: Build an academic grading system using functions

Requirements:
- Calculate grade based on score using logical conditions
- Generate detailed student report
- Use clean, reusable code with functions
- Handle multiple students
"""

def calculate_grade(score: int) -> str:
    """
    Determine letter grade based on score.
    
    Grading Scale:
        A: >= 90
        B: >= 75
        C: >= 60
        D: >= 40
        F: < 40
    
    Parameters:
        score (int): Student's score (0-100)
    
    Returns:
        str: Letter grade (A, B, C, D, or F)
    """
    if score >= 90:
        return "A"
    elif score >= 75:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 40:
        return "D"
    else:
        return "F"


def get_grade_description(grade: str) -> str:
    \"\"\"Get detailed description for a grade.\"\"\"
    descriptions = {
        "A": "Excellent - Outstanding performance",
        "B": "Good - Above average performance",
        "C": "Satisfactory - Average performance",
        "D": "Poor - Below average performance",
        "F": "Fail - Needs improvement"
    }
    return descriptions.get(grade, "Unknown")


def generate_student_report(name: str, score: int) -> str:
    \"\"\"
    Generate detailed report for a student.
    
    Parameters:
        name (str): Student's name
        score (int): Student's score
    
    Returns:
        str: Formatted report
    \"\"\"
    grade = calculate_grade(score)
    description = get_grade_description(grade)
    
    report = f"{name} has scored {score} and received grade {grade}"
    return report


def process_students(students: dict) -> None:
    \"\"\"
    Process multiple students and display results.
    
    Parameters:
        students (dict): Dictionary with name as key and score as value
    \"\"\"
    print("=" * 60)
    print("STUDENT GRADING SYSTEM - RESULTS")
    print("=" * 60)
    print()
    
    # Track statistics
    total_score = 0
    grade_counts = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    
    for name, score in students.items():
        grade = calculate_grade(score)
        description = get_grade_description(grade)
        
        # Display individual report
        print(f"Student: {name}")
        print(f"  Score: {score}/100")
        print(f"  Grade: {grade} - {description}")
        print()
        
        # Update statistics
        total_score += score
        grade_counts[grade] += 1
    
    # Display summary statistics
    print("=" * 60)
    print("SUMMARY STATISTICS")
    print("=" * 60)
    avg_score = total_score / len(students) if students else 0
    print(f"Total Students: {len(students)}")
    print(f"Average Score: {avg_score:.2f}")
    print()
    
    print("Grade Distribution:")
    for grade in ["A", "B", "C", "D", "F"]:
        count = grade_counts[grade]
        percentage = (count / len(students) * 100) if students else 0
        print(f"  {grade}: {count} student(s) ({percentage:.1f}%)")


# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    # Sample student data
    students = {
        "Aman": 85,
        "Priya": 92,
        "Raj": 78,
        "Neha": 45,
        "Arjun": 88,
        "Deepika": 65,
        "Vikram": 35,
        "Shreya": 95
    }
    
    # Process and display results
    process_students(students)
    
    print()
    print("=" * 60)
    print("INDIVIDUAL QUERY EXAMPLES")
    print("=" * 60)
    print()
    
    # Query individual students
    test_names = ["Aman", "Neha"]
    for name in test_names:
        score = students.get(name)
        if score:
            report = generate_student_report(name, score)
            grade = calculate_grade(score)
            print(f"Report: {report}")
            print(f"Description: {get_grade_description(grade)}")
            print()
