"""Create a reusable decorator that supports arguments and return values."""

from functools import wraps


def log_activity(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Finished: {func.__name__}")
        return result

    return wrapper


@log_activity
def brew_chai(chai_type, milk="no"):
    return f"Brewing {chai_type} chai; milk: {milk}"


if __name__ == "__main__":
    print(brew_chai("masala", milk="yes"))