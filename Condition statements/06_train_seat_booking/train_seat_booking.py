"""
Train Seat Booking System - Match/Case Statement
Project: Seat Type Selection with Features
Note: Requires Python 3.10 or higher
"""

def train_seat_booking():
    """
    A train seat booking system that assigns seats based on selected type.
    Demonstrates the match-case statement (structural pattern matching).
    Available from Python 3.10 onwards.
    """
    seat_type = input("Enter your seat type (sleeper/ac/general/luxury): ").lower()
    
    match seat_type:
        case "sleeper":
            print("You got a seat to sleep comfortably.")
        case "ac":
            print("You got an AC seat with climate control.")
        case "general":
            print("You got a general seating. Please find your seat.")
        case "luxury":
            print("You got a full compartment along with a personal washroom!")
        case _:
            print("Invalid seat type. Please choose from: sleeper, ac, general, or luxury.")


def train_seat_booking_with_prices():
    """
    Enhanced version with pricing information.
    """
    seat_type = input("Enter your seat type (sleeper/ac/general/luxury): ").lower()
    
    match seat_type:
        case "sleeper":
            price = 500
            features = "Bed, bedding, reading light"
        case "ac":
            price = 750
            features = "Air-conditioned, comfortable seat"
        case "general":
            price = 250
            features = "Basic seating"
        case "luxury":
            price = 1500
            features = "Private compartment, washroom, meal service"
        case _:
            print("Invalid seat type. Please choose from: sleeper, ac, general, or luxury.")
            return
    
    print(f"\nSeat Type: {seat_type.upper()}")
    print(f"Price: Rs. {price}")
    print(f"Features: {features}")


if __name__ == "__main__":
    print("=== Train Seat Booking System ===\n")
    train_seat_booking()
