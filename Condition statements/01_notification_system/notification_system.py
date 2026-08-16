"""
Notification System - Basic If/Else Statement
Project: Kettle Boiling Notification
"""

def check_kettle_status():
    """
    Simple notification system to check if kettle is boiled.
    This demonstrates the basic if-else conditional statement.
    """
    kt_boiled = True
    
    if kt_boiled:
        print("Kettle is boiled, you can make tea now.")
    else:
        print("Kettle is not boiled yet, please wait.")


if __name__ == "__main__":
    check_kettle_status()
