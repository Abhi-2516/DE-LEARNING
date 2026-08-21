"""Encapsulation with a protected convention and a validated property."""


class BankAccount:
    def __init__(self, owner: str, opening_balance: float = 0):
        self.owner = owner
        self._balance = 0.0
        self.balance = opening_balance

    @property
    def balance(self) -> float:
        return self._balance

    @balance.setter
    def balance(self, amount: float) -> None:
        if amount < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = float(amount)

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.balance = self.balance + amount

    def withdraw(self, amount: float) -> None:
        if not 0 < amount <= self.balance:
            raise ValueError("Withdrawal exceeds the available balance")
        self.balance = self.balance - amount


if __name__ == "__main__":
    account = BankAccount("Asha", 1_000)
    account.deposit(500)
    account.withdraw(200)
    print(f"{account.owner}: {account.balance:.2f}")
