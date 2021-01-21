class User:
    def __init__(self, name, pin, id):
        self.id = id
        self.cards = []
        self.name = name
        self.pin = pin
        self.accounts = {}

    def addCard(self, card):
        self.cards.append(card)
        print("New card added")
        return

    def addAccount(self, account):
        print("Account added")
        self.accounts[account.accountNumber] = account
        return

    def getAccount(self, accountNumber):
        if accountNumber not in self.accounts:
            print("Account not found")
            return None
        return self.accounts[accountNumber]
