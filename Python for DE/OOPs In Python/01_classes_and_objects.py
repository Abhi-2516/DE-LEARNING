"""Classes, objects, attributes, and instance methods."""


class Chai:
    """Blueprint used to create individual chai objects."""

    category = "Beverage"

    def __init__(self, tea_type: str, size_ml: int):
        self.tea_type = tea_type
        self.size_ml = size_ml

    def describe(self) -> str:
        return f"{self.size_ml} ml {self.tea_type} chai"


if __name__ == "__main__":
    masala_chai = Chai("Masala", 200)
    ginger_chai = Chai("Ginger", 250)

    print(masala_chai.describe())
    print(ginger_chai.describe())
    print(f"Category: {Chai.category}")
