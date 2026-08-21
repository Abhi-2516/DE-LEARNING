"""Instance attributes, class attributes, and attribute shadowing."""


class SmartDevice:
    brand = "HomeTech"

    def __init__(self, name: str, is_on: bool = False):
        self.name = name
        self.is_on = is_on

    def turn_on(self) -> None:
        self.is_on = True

    def status(self) -> str:
        state = "on" if self.is_on else "off"
        return f"{self.name} is {state} ({self.brand})"


if __name__ == "__main__":
    device = SmartDevice("Kitchen kettle")
    print(device.status())

    device.brand = "CustomBrand"
    device.turn_on()
    print(device.status())
    print(f"Class brand remains: {SmartDevice.brand}")
