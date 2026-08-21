"""Static methods, class methods, multiple inheritance, and MRO."""


class ChaiUtils:
    @staticmethod
    def clean_ingredients(raw_text: str) -> list[str]:
        return [item.strip() for item in raw_text.split(",") if item.strip()]


class Order:
    def __init__(self, tea_type: str):
        self.tea_type = tea_type

    @classmethod
    def from_text(cls, text: str) -> "Order":
        return cls(text.strip().title())


class HotDrink:
    label = "hot drink"


class MilkBased(HotDrink):
    label = "milk-based drink"


class Spiced(MilkBased):
    pass


if __name__ == "__main__":
    print(ChaiUtils.clean_ingredients(" water, milk, ginger "))
    print(Order.from_text("masala").tea_type)
    print(Spiced.label)
    print(" -> ".join(cls.__name__ for cls in Spiced.__mro__))
