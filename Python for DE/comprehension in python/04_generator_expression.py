"""Generator expressions: calculate values lazily and save memory."""


def cups_sold_above_threshold(sales: list[int], threshold: int = 3) -> int:
    """Sum sales entries greater than the threshold."""
    return sum(cups for cups in sales if cups > threshold)


def discounted_prices(prices: list[int], discount: float = 0.10) -> list[int]:
    """Create a list from a generator of discounted whole-number prices."""
    price_generator = (int(price * (1 - discount)) for price in prices)
    return list(price_generator)


if __name__ == "__main__":
    daily_sales = [5, 10, 12, 7, 3, 8, 9, 15]
    print("Cups sold above 3:", cups_sold_above_threshold(daily_sales))
    print("Discounted prices:", discounted_prices([250, 100, 1200, 400]))
