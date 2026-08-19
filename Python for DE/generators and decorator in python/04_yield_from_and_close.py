"""Delegate to other generators and close a generator cleanly."""


def local_chai():
    yield "masala chai"
    yield "ginger chai"


def imported_chai():
    yield "matcha"
    yield "oolong"


def full_menu():
    yield from local_chai()
    yield from imported_chai()


if __name__ == "__main__":
    for chai in full_menu():
        print(chai)