"""Polymorphism and abstract interfaces."""

from abc import ABC, abstractmethod


class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount: float) -> str:
        """Process a payment and return a receipt message."""


class CardPayment(PaymentMethod):
    def pay(self, amount: float) -> str:
        return f"Card payment accepted: {amount:.2f}"


class UpiPayment(PaymentMethod):
    def pay(self, amount: float) -> str:
        return f"UPI payment accepted: {amount:.2f}"


def checkout(payment_method: PaymentMethod, amount: float) -> None:
    print(payment_method.pay(amount))


if __name__ == "__main__":
    checkout(CardPayment(), 450)
    checkout(UpiPayment(), 275)
