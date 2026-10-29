import random
class BankAccount:

    def __init__(self, name_customer):
        self.account_balance = 0
        self.name = name_customer
        self.account_number = random.randint(0,999999999)

    def deposit(self,amount):
        if amount <= 0:
            raise Exception("Value needs to be greater than zero")
        else:
            self.account_balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise Exception("Value needs to be greater than zero")
        if amount > self.account_balance:
            raise Exception("Insufficient funds")
        else:
            self.account_balance -= amount

    def view_info(self):
        print(f"Name: {self.name}")
        print(f"Account number: {self.account_number}")
        print(f"Balance: ${self.account_balance:,.2f}")
        
        
        

        
