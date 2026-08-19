"""Capstone: lazily clean and format a stream of tea orders."""

from functools import wraps


def log_activity(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Running {func.__name__}")
        return func(*args, **kwargs)

    return wrapper


def clean_orders(orders):
    for order in orders:
        cleaned = order.strip().lower()
        if cleaned:
            yield cleaned


def format_orders(orders):
    for order in orders:
        yield f"Preparing: {order.title()}"


@log_activity
def prepare_orders(raw_orders):
    return format_orders(clean_orders(raw_orders))


if __name__ == "__main__":
    raw_orders = [" Masala chai ", "", " ginger tea", "LEMON TEA "]
    for message in prepare_orders(raw_orders):
        print(message)