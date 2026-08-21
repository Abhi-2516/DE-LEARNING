"""Raise domain-specific exceptions when business rules are violated."""


class ChaiShopError(Exception):
    """Base exception for chai-shop business errors."""


class UnsupportedFlavourError(ChaiShopError):
    """Raised when a flavour is not on the menu."""


class InvalidQuantityError(ChaiShopError):
    """Raised when the requested quantity is invalid."""


AVAILABLE_FLAVOURS = {"masala", "ginger", "lemon"}


def brew_chai(flavour: str, cups: int) -> str:
    if flavour not in AVAILABLE_FLAVOURS:
        raise UnsupportedFlavourError(f"Unsupported flavour: {flavour}")
    if not isinstance(cups, int) or cups <= 0:
        raise InvalidQuantityError("cups must be a positive integer")
    return f"Brewing {cups} cup(s) of {flavour} chai"


if __name__ == "__main__":
    for flavour, cups in (("masala", 2), ("mint", 1), ("ginger", 0)):
        try:
            print(brew_chai(flavour, cups))
        except ChaiShopError as error:
            print(f"Could not process order: {error}")
