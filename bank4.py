# Noon-OOP
# version Number -4
# any number of accounts -with List
# b->get balance  complete
# d-> deposit complete
# w->withdraw complte
# s-> show        comple
# q-> quit

accountNameList = []
accountBalanceList = []
accountpasswordList = []


# function to create a new account
def newAccont(name, balance, password):
    global accountNameList, accountBalanceList, accountpasswordList
    accountNameList.append(name)
    accountBalanceList.append(balance)
    accountpasswordList.append(password)


# show details
def show(accountNumber):
    global accountNameList, accountBalanceList, accountpasswordList
    print(" Account: ", accountNumber)
    print(" Name: ", accountNameList[accountNumber])
    print(" Balance:", accountBalanceList[accountNumber])
    print(" password:", accountpasswordList[accountNumber])
    print()


# get balance
def getBalance(accountNumber, password):
    global accountNameList, accountBalanceList, accountpasswordList
    if password != accountpasswordList[accountNumber]:
        print("Incorrect password")
        return None
    return accountBalanceList[accountNumber]


# deposit
def Deposit(accountNumber, amountTodeposit, password):
    global accountNameList, accountBalanceList, accountpasswordList
    if password != accountpasswordList[accountNumber]:
        print("Incorrect password")

    if amountTodeposit < 0:
        print("You cannot deposit a negative amount")
        return None

    accountBalanceList[accountNumber] = (
        accountBalanceList[accountNumber] + amountTodeposit
    )
    return accountBalanceList[accountNumber]


# withdraw
def Withdraw(accountNumber, amountToWithdraw, password):
    global accountNameList, accountBalanceList, accountpasswordList
    if password != accountpasswordList[accountNumber]:
        print("Incorrect password")
        return None

    if amountToWithdraw > accountBalanceList[accountNumber]:
        print("You cannot withdraw more than you have in account")
        return None

    accountBalanceList[accountNumber] = (
        accountBalanceList[accountNumber] - amountToWithdraw
    )
    return accountBalanceList[accountNumber]


# quit the app
