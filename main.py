from ATMController import ATMController
from BankAPI import BankAPI


def setupAPI(cards, pin, accounts):
    ### Add users and accounts to bankAPI
    print("=======API setup started========")
    bankAPI = BankAPI()

    user1 = bankAPI.createUser("Fake Name", 123456, "user1", cards)
    for accountID in accounts:
        account = bankAPI.createAccount(accountID, user1.id)
        user1.addAccount(account)
    print("=======API setup complete========")
    return bankAPI


def successfulTest(bankAPI):
    atmController = ATMController(bankAPI)
    atmController.insertCard(1000)
    atmController.typePinNumber(123456)
    account = atmController.getAccounts()[1]
    atmController.selectAccount(account)
    atmController.checkBalance()
    for i in range(3):
        atmController.deposite(1)
        atmController.checkBalance()
    for i in range(4):
        atmController.withdraw(1)
        atmController.checkBalance()
    atmController.removeCard()
    return


def noCardTest(bankAPI):
    atmController = ATMController(bankAPI)
    atmController.typePinNumber(123456)
    atmController.selectAccount(5516)
    atmController.getAccounts()
    atmController.checkBalance()
    return


def wrongCardTest(bankAPI):
    atmController = ATMController(bankAPI)
    atmController.insertCard(5555)
    atmController.typePinNumber(123456)
    return


def wrongPinTest(bankAPI):
    atmController = ATMController(bankAPI)
    atmController.insertCard(1000)
    atmController.typePinNumber(000000)
    return


def wrongAccountTest(bankAPI):
    atmController = ATMController(bankAPI)
    atmController.insertCard(1000)
    atmController.typePinNumber(123456)
    atmController.selectAccount(0000)
    return


def outOfBalanceTest(bankAPI):
    atmController = ATMController(bankAPI)
    atmController.insertCard(1000)
    atmController.typePinNumber(123456)
    account = atmController.getAccounts()[1]
    atmController.selectAccount(account)
    atmController.checkBalance()
    atmController.deposite(1)
    atmController.checkBalance()
    atmController.withdraw(100)
    atmController.checkBalance()
    atmController.removeCard()
    return


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # different cards owned by the user
    cards = [1000, 1100, 2100, 3100]
    # pin number for authentication
    pin = 123456
    # different accounts owned by the user
    accounts = [5555, 5556, 5557, 5558]
    # initialize bankAPI
    bankAPI = setupAPI(cards, pin, accounts)

    # Uncomment following section to run tests:
    successfulTest(bankAPI)
    # noCardTest(bankAPI)
    # wrongPinTest(bankAPI)
    # wrongAccountTest(bankAPI)
    # outOfBalanceTest(bankAPI)

