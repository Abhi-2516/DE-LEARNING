"""Basic exception handling with try, except, else, and finally."""


def divide_order_total(total: float, cups: int) -> float:
    try:
        return total / cups
    except ZeroDivisionError:
        print("The number of cups must be greater than zero.")
        return 0.0


if __name__ == "__main__":
    print(f"Price per cup: {divide_order_total(120, 3):.2f}")
    print(f"Price per cup: {divide_order_total(120, 0):.2f}")

    try:
        print(int("not a number"))
    except ValueError as error:
        print(f"Conversion failed: {error}")
    else:
        print("Conversion succeeded.")
    finally:
        print("Validation attempt complete.")
