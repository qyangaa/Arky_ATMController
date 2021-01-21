from User import User
from Account import Account

class BankAPI:
    """
    Simulation of bankAPI, which contains user informations and checks
    """
    def __init__(self):
        self.users = {}
        self.card2uid = {}

    def addUser(self, user):
        self.users[user.id] = user
        for card in user.cards:
            self.card2uid[card] = user.id

    def getUser(self, card, pin):
        if not card:
            print("No card")
            return 0
        if card not in self.card2uid:
            print("Card not found")
            return 0
        uid = self.card2uid[card]
        user = self.users[uid]
        if user.pin != pin:
            print("Wrong pin number")
            return -1
        return user

    def createUser(self, name, pin, id, cards):
        user = User(name, pin, id)
        for card in cards:
            user.addCard(card)
        self.addUser(user)
        return user

    def createAccount(self, accountNumber, uid):
        account = Account(accountNumber, uid)
        return account


