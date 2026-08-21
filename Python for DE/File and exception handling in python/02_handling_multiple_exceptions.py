"""Handle expected exceptions separately and preserve useful messages."""


MENU = {"masala": 20, "ginger": 40, "lemon": 30}


def calculate_bill(flavour: str, cups: int) -> int:
    try:
        price = MENU[flavour]
        if not isinstance(cups, int):
            raise TypeError("cups must be an integer")
        if cups <= 0:
            raise ValueError("cups must be positive")
        return price * cups
    except KeyError as error:
        raise ValueError(f"Unknown flavour: {flavour}") from error


if __name__ == "__main__":
    for flavour, cups in (("ginger", 3), ("mint", 2), ("masala", "two")):
        try:
            print(f"{flavour}: {calculate_bill(flavour, cups)}")
        except (TypeError, ValueError) as error:
            print(f"Order rejected: {error}")
