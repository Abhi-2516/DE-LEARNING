"""
Smart Thermostat System - Nested If Statements
Project: Temperature Monitoring with Device Status Check
"""

def smart_thermostat():
    """
    A smart thermostat that checks device status first,
    then monitors temperature. Demonstrates nested if statements.
    """
    device_status = 'active'
    temp = 38
    
    if device_status == 'active':
        if temp > 35:
            print("ALERT: Temperature is too high!")
        else:
            print("Normal temperature.")
    else:
        print("Device is offline.")


def smart_thermostat_interactive():
    """
    Interactive version that accepts user input.
    """
    device_status = input("Enter device status (active/offline): ").lower()
    temp = int(input("Enter current temperature: "))
    
    if device_status == 'active':
        if temp > 35:
            print("ALERT: Temperature is too high!")
        else:
            print("Normal temperature.")
    else:
        print("Device is offline.")


if __name__ == "__main__":
    print("--- Auto Check ---")
    smart_thermostat()
    
    print("\n--- Interactive Check ---")
    smart_thermostat_interactive()
