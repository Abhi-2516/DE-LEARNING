"""Useful dunder methods and a compact dataclass model."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Product:
    name: str
    price: float

    def __post_init__(self) -> None:
        if self.price < 0:
            raise ValueError("Price cannot be negative")

    def __str__(self) -> str:
        return f"{self.name}: {self.price:.2f}"

    def __lt__(self, other: "Product") -> bool:
        return self.price < other.price


if __name__ == "__main__":
    tea = Product("Masala chai", 80)
    coffee = Product("Filter coffee", 95)

    print(tea)
    print(tea < coffee)
    print(tea == Product("Masala chai", 80))
