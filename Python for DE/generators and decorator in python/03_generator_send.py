"""Send values into a running generator with ``send``."""


def chai_customer():
    print("Welcome to the chai stall.")
    order = yield
    while True:
        print(f"Preparing: {order}")
        order = yield


if __name__ == "__main__":
    stall = chai_customer()
    next(stall)  # Start the generator before sending the first value.
    stall.send("masala chai")
    stall.send("cardamom tea")
    stall.close()