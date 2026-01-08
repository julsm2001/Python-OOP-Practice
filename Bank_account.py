class BankAccount():
    """
    A class to represent a simple bank account with withdrawal limits.
    """
    def __init__(self, holder:str, account_number:int, withdrawal_limit:float, balance:float=0.0):
        # Setting up the account details
        self.holder = holder
        self.account_number = account_number
        self.withdrawal_limit = withdrawal_limit
        self.balance = balance

    def __str__(self):    
        # This makes the account info look clean when printing the object
        return f"Account Holder: {self.holder}| Balance: ${self.balance}"

    def deposit(self, amount:float):
        # Simply add the amount to the current balance
        self.balance = self.balance + amount

    def withdraw(self, amount:float):
        # Validation: Check if the user has enough money and stays within the limit
        if amount <= self.balance and amount <= self.withdrawal_limit:
            self.balance = self.balance - amount
            print(f"Successfully withdrawn ${amount}.\nNew balance: ${self.balance}")
        else:
            print("Transaction denied: Insufficient funds or amount exceeds withdrawal limit.")

# Testing the Class

# Creating a new account for Julián with a $500 limit
my_account = BankAccount("Julián Machuca", 987654, 500.0, 100.0)

print(my_account)

# Normal deposit
my_account.deposit(50.0)

# Valid withdrawal
my_account.withdraw(40.0)

# A withdrawal that should fail due to the limit
my_account.withdraw(600.0)
