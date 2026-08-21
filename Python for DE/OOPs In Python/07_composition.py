"""Composition: building an object from other objects."""


class Engine:
    def __init__(self, horsepower: int):
        self.horsepower = horsepower

    def details(self) -> str:
        return f"{self.horsepower} HP engine"


class Vehicle:
    def __init__(self, brand: str, engine: Engine):
        self.brand = brand
        self.engine = engine

    def details(self) -> str:
        return f"{self.brand} with a {self.engine.details()}"


if __name__ == "__main__":
    vehicle = Vehicle("CityRide", Engine(120))
    print(vehicle.details())
