"""Nested comprehensions: flatten or transform nested collections."""


def flatten_order_items(orders: list[list[str]]) -> list[str]:
    """Flatten a list of orders into one list of items."""
    return [item for order in orders for item in order]


def multiplication_table(size: int) -> list[list[int]]:
    """Build a square multiplication table from 1 to size."""
    return [[row * column for column in range(1, size + 1)] for row in range(1, size + 1)]


if __name__ == "__main__":
    orders = [["tea", "snack"], ["coffee"], ["juice", "water"]]
    print("All order items:", flatten_order_items(orders))
    for row in multiplication_table(3):
        print(row)
