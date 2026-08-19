"""Use an infinite generator safely by requesting only needed values."""


def refill_chai():
    count = 1
    while True:
        yield f"Refill #{count}"
        count += 1


if __name__ == "__main__":
    refill = refill_chai()
    for _ in range(5):
        print(next(refill))