"""Inheritance, super(), and method overriding."""


class Beverage:
    def __init__(self, name: str):
        self.name = name

    def prepare(self) -> str:
        return f"Preparing {self.name}"


class Chai(Beverage):
    def __init__(self, name: str, spice_level: int):
        super().__init__(name)
        self.spice_level = spice_level

    def prepare(self) -> str:
        return f"{super().prepare()} with spice level {self.spice_level}"


if __name__ == "__main__":
    chai = Chai("Masala chai", 3)
    print(chai.prepare())
    print(f"Is Beverage subclass: {issubclass(Chai, Beverage)}")
