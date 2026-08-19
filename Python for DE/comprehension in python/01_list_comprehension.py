"""List comprehensions: transform and filter items into a new list."""


def affordable_teas(menu: list[str]) -> list[str]:
    """Return tea names containing the word 'iced'."""
    return [tea for tea in menu if "iced" in tea.lower()]


def square_even_numbers(numbers: list[int]) -> list[int]:
    """Return squares for even numbers only."""
    return [number**2 for number in numbers if number % 2 == 0]


if __name__ == "__main__":
    menu = ["masala", "iced tea", "green tea", "iced peach", "ginger tea"]
    print("Iced teas:", affordable_teas(menu))
    print("Even squares:", square_even_numbers(list(range(1, 11))))
