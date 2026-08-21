"""Constructors, alternate constructors, and class state."""


class ChaiOrder:
    total_orders = 0

    def __init__(self, tea_type: str, sweetness: str, size: str):
        self.tea_type = tea_type
        self.sweetness = sweetness
        self.size = size
        type(self).total_orders += 1

    @classmethod
    def from_string(cls, order_text: str) -> "ChaiOrder":
        tea_type, sweetness, size = order_text.split("-")
        return cls(tea_type, sweetness, size)

    def summary(self) -> str:
        return f"{self.size} {self.tea_type} chai, {self.sweetness} sweetness"


if __name__ == "__main__":
    first = ChaiOrder("Masala", "medium", "Large")
    second = ChaiOrder.from_string("Ginger-low-Small")

    print(first.summary())
    print(second.summary())
    print(f"Orders created: {ChaiOrder.total_orders}")
