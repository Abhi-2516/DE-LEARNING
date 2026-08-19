"""Learn how generator functions produce one value at a time."""


def serve_chai():
    """Yield tea orders one at a time instead of building a full list."""
    yield "cup 1: masala chai"
    yield "cup 2: ginger chai"
    yield "cup 3: lemon tea"


if __name__ == "__main__":
    stall = serve_chai()
    print(next(stall))
    print("The next cup is ready when requested.")

    for cup in stall:
        print(cup)