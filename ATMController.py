from User import User
from Account import Account
from BankAPI import BankAPI


class ATMController:
    def __init__(self, database):
        self.user = None
        self.account = None
        self.card = None
        self.bankAPI = database
        print("Please insert card")

    def insertCard(self, card):
        self.card = card
        print("Card %d inserted" % card)
        return

    def typePinNumber(self, pin):
        result = self.bankAPI.getUser(self.card, pin)
        if not result:
            print("Please insert card")
            self.card = None
            return
        elif result==-1:
            print("Pin number incorrect, please type in pin number again")
            return
        self.user = result
        print("Welcome " + self.user.name)
        return

    def selectAccount(self, accountNumber):
        if not self.user:
            print("No user logged in")
            return
        self.account = self.user.getAccount(accountNumber)
        if not self.account:
            return
        print("Account %d selected" % accountNumber)
        return

    def getAccounts(self):
        if not self.user:
            print("No user logged in")
            return
        if not self.user.accounts:
            print("No accounts opened")
            return
        accounts = list(self.user.accounts.keys())
        print("your accounts: ", accounts)
        return accounts

    def removeCard(self):
        card = self.card
        self.user = None
        self.account = None
        self.card = None
        print("Have a good day!")
        return card

    def checkBalance(self):
        if not self.user:
            print("No user logged in")
            return
        if not self.user.accounts:
            print("No accounts opened")
            return
        if not self.account:
            print("No account selected")
            return
        return self.account.checkBalance()

    def deposite(self, amount):
        if not self.user:
            print("No user logged in")
            return
        if not self.user.accounts:
            print("No accounts opened")
            return
        if not self.account:
            print("No account selected")
            return
        return self.account.deposit(amount)

    def withdraw(self, amount):
        if not self.user:
            print("No user logged in")
            return
        if not self.user.accounts:
            print("No accounts opened")
            return
        if not self.account:
            print("No account selected")
            return
        if self.account.balance == 0:
            print("Withdrawal failed: your current balance is 0")
            return
        if amount > self.account.balance:
            print("Withdraw amount exceeds balance, please enter an amount less than %d" % self.account.balance)
            return
        return self.account.withdraw(amount)
