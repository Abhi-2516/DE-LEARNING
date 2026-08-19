"""Build a decorator that adds behavior before and after a function."""

from functools import wraps


def announce(func):
    @wraps(func)
    def wrapper():
        print("Before the function runs")
        func()
        print("After the function runs")

    return wrapper


@announce
def greet():
    print("Hello from the decorator lesson")


if __name__ == "__main__":
    greet()
    print(f"Function name: {greet.__name__}")