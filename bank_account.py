from datetime import datetime

class InsufficientFundsError(Exception):
    """Raised when withdrawal amount exceeds available balance."""
    def __init__(self, amount, balance):
        self.amount = amount
        self.balance = balance
        super().__init__(
            f"Cannot withdraw ₹{amount:.2f}. Available balance: ₹{balance:.2f}"
        )

class InvalidAmountError(Exception):
    """Raised when a negative or zero amount is entered."""
    def __init__(self, amount):
        super().__init__(f"Amount must be positive. Got: ₹{amount}")

class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        if balance < 0:
            raise InvalidAmountError(balance)
        self.owner = owner
        self.__balance = balance
        self.__transactions = []
        self.__log(f"Account created with opening balance ₹{balance:.2f}")

    def __log(self, message: str):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.__transactions.append(f"[{timestamp}]  {message}")

    @property
    def balance(self) -> float:
        return self.__balance

    def deposit(self, amount: float):
        """Deposit money into the account."""
        if not isinstance(amount, (int, float)):
            raise TypeError(f"Amount must be a number, got {type(amount).__name__}")
        if amount <= 0:
            raise InvalidAmountError(amount)

        self.__balance += amount
        self.__log(f"DEPOSIT   +₹{amount:.2f}   →  Balance: ₹{self.__balance:.2f}")
        print(f"✅ ₹{amount:.2f} deposited. New balance: ₹{self.__balance:.2f}")

    def withdraw(self, amount: float):
        """Withdraw money from the account."""
        if not isinstance(amount, (int, float)):
            raise TypeError(f"Amount must be a number, got {type(amount).__name__}")
        if amount <= 0:
            raise InvalidAmountError(amount)
        if amount > self.__balance:
            raise InsufficientFundsError(amount, self.__balance)

        self.__balance -= amount
        self.__log(f"WITHDRAW  -₹{amount:.2f}   →  Balance: ₹{self.__balance:.2f}")
        print(f"✅ ₹{amount:.2f} withdrawn. New balance: ₹{self.__balance:.2f}")

    def transfer(self, amount: float, target_account: "BankAccount"):
        """Transfer money to another BankAccount."""
        if not isinstance(target_account, BankAccount):
            raise TypeError("Target must be a BankAccount instance.")

        self.withdraw(amount)
        target_account.deposit(amount)
        self.__log(f"TRANSFER  -₹{amount:.2f}  →  To: {target_account.owner}")
        target_account.__log(f"TRANSFER  +₹{amount:.2f}  ←  From: {self.owner}")
        print(f"🔄 ₹{amount:.2f} transferred to {target_account.owner}'s account.")

    def get_history(self):
        """Print full transaction history."""
        print(f"\n{'═'*55}")
        print(f"  📋 Transaction History — {self.owner}")
        print(f"{'═'*55}")
        if not self.__transactions:
            print("  No transactions yet.")
        else:
            for entry in self.__transactions:
                print(f"  {entry}")
        print(f"{'═'*55}\n")

    def __str__(self):
        return (
            f"\n{'─'*40}\n"
            f"  👤 Account Owner : {self.owner}\n"
            f"  💰 Balance       : ₹{self.__balance:.2f}\n"
            f"{'─'*40}"
        )

if __name__ == "__main__":
    print("\n🏦 Welcome to PyBank!\n")
    alice = BankAccount("Alice", balance=5000)
    bob   = BankAccount("Bob",   balance=1000)

    print(alice)
    print(bob)

    alice.deposit(2000)
    alice.withdraw(500)
    alice.transfer(1500, bob)

    print(alice)
    print(bob)
    print("\n⚠️  Testing Error Handling:\n")

    try:
        bob.withdraw(99999)
    except InsufficientFundsError as e:
        print(f"❌ InsufficientFundsError: {e}")

    try:
        alice.deposit(-200)
    except InvalidAmountError as e:
        print(f"❌ InvalidAmountError: {e}")

    try:
        alice.deposit("five hundred")
    except TypeError as e:
        print(f"❌ TypeError: {e}")

    alice.get_history()
    bob.get_history()
