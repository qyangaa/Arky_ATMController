class Account:
    def __init__(self, accountNumber, uid):
        self.accountNumber = accountNumber
        self.uid = uid
        self.balance = 0
        print("Account created")

    def deposit(self, amount):
        self.balance+=amount
        print("Successfully deposited %d dollars"%amount)
        return

    def checkBalance(self):
        print("Current balance is %d dollars" % self.balance)
        return self.balance

    def withdraw(self, amount):
        self.balance-=amount
        print("Successfully withdrawn %d dollars"%amount)
        return amount

