# Non-OOP
# single account
# author:- Jagdish
# date:-10/8/2023
# function based

accountName = ""
accountBalance = 0
accountPassword = ""


# new account
def newAccount(name, balance, password):
    global accountName, accountBalance, accountPassword
    accountName = name
    accountBalance = balance
    accountPassword = password


# show details
def show():
    global accountName, accountBalance, accountPassword
    print(" Name:", accountName)
    print(" balance: ", accountBalance)
    print(" Password", accountPassword)


# get balance
def getBalance(password):
    global accountName, accountBalance, accountPassword
    if password != accountPassword:
        print("Incorrect password")
        return None
    return accountBalance


# deposit
def deposit(amountToDeposit, password):
    global accountName, accountBalance, accountPassword
    if amountToDeposit < 0:
        print("You cannot deposit a negative amount!")
        return None

    if password != accountPassword:
        print("Incorrect password")
        return None

    accountBalance = accountBalance + amountToDeposit
    return accountBalance


# withdraw
def withdraw(amountToWithdraw, password):
    global accountName, accountBalance, accountPassword
    if amountToWithdraw < 0:
        print("You cannot withdraw a negative amount")
        return None

    if password != accountPassword:
        print("Incorrect password")
        return None

    if amountToWithdraw > accountBalance:
        print("You cannot withdraw more than you have in your account")
        return None

    accountBalance = accountBalance - amountToWithdraw
    return accountBalance


# user Inpuyt
# function calling
newAccount("Ankush", 1000, "ank123")  # new account create

while True:
    print()
    print("Press b to get the balance")
    print("press d to make a deposit")
    print("press w to make a withdraw")
    print("press s to show the account")
    print("press q to quit")
    print()

    action = input("What do you want to do?")
    action = action.lower()
    action = action[0]
    print()

    if action == "b":
        print("get balance:")
        userPassword = input("Please enter the password: ")
        theBalance = getBalance(userPassword)
        if theBalance is not None:
            print("Your balance is:", theBalance)

    elif action == "d":
        print("Deposit")
        userDepositAmount = input("Please enter amount to deposit")
        userDepositAmount = int(userDepositAmount)
        userPassword = input("Please enetr the password: ")

        newBalance = deposit(userDepositAmount, userPassword)
        if newBalance is not None:
            print("Your new balance is: ", newBalance)

    elif action == "s":
        print("Show")
        show()

    elif action == "q":
        break

    elif action == "w":
        print("Withdraw")
        userWithdrawAmount = input("Please enter amount to Withdraw")
        userWithdrawAmount = int(userWithdrawAmount)
        userPassword = input("Please enetr the password: ")

        newBalance = withdraw(userWithdrawAmount, userPassword)
        if newBalance is not None:
            print("your new balance is", newBalance)

print("Done")
