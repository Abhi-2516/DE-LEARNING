"""Project: Smart Inventory Filter using four comprehension styles."""


def filter_inventory(items: list[dict]) -> tuple[list[str], set[str], dict[str, int], list[int]]:
    """Return affordable names, unique categories, prices, and 10%-discounted prices."""
    affordable_products = [product["name"] for product in items if product["price"] < 500]
    unique_categories = {product["category"] for product in items}
    name_to_price = {product["name"]: product["price"] for product in items}
    discounted_prices = list(int(product["price"] * 0.90) for product in items)

    return affordable_products, unique_categories, name_to_price, discounted_prices


if __name__ == "__main__":
    inventory = [
        {"name": "Notebook", "price": 250, "category": "Stationery"},
        {"name": "Pen", "price": 100, "category": "Stationery"},
        {"name": "Bag", "price": 1200, "category": "Accessories"},
        {"name": "Bottle", "price": 400, "category": "Utensils"},
    ]
    results = filter_inventory(inventory)
    print("Affordable products:", results[0])
    print("Unique categories:", results[1])
    print("Name to price:", results[2])
    print("Discounted prices:", results[3])
