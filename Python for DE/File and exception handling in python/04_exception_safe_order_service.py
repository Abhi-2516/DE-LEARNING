"""A small service combining validation, custom errors, and cleanup."""


class OrderError(Exception):
    """Base error for invalid orders."""


class MenuItemNotFoundError(OrderError):
    pass


class QuantityError(OrderError):
    pass


class OrderService:
    menu = {"masala": 20, "ginger": 40}

    def create_bill(self, flavour: str, cups: int) -> int:
        if flavour not in self.menu:
            raise MenuItemNotFoundError(f"{flavour} is not available")
        if type(cups) is not int or cups <= 0:
            raise QuantityError("cups must be a positive integer")
        return self.menu[flavour] * cups

    def process(self, flavour: str, cups: int) -> str:
        try:
            total = self.create_bill(flavour, cups)
            return f"Order confirmed: {total}"
        except OrderError as error:
            return f"Order failed: {error}"
        finally:
            print("Order processing finished.")


if __name__ == "__main__":
    service = OrderService()
    print(service.process("ginger", 3))
    print(service.process("mint", 2))
