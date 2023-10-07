# Analysis of Required Operations and Data
# create account
# Deposit
# withdraw
# check balance

# data
# customer name
# password
# balance

# author : jagdish
# 7/10/2023
# task: initialize the bank account write basic functionality
# approcah : Non-OOP
# version: 1
# testing : single account

# data
accountName = "Ankush"
accountBalance = 1000
accountpassword = "ank123"

# functionality
while True:
    print()
    print("Press B to get the balance")
    print("Press d for deposit")
    print("press w to make withdrawal")
    print("press s to show the account")
    print("press q to quit")
    print()

    action = input("what do you want to do?")
    action = action.lower()
    action = action[0]
    print()

    # check balance
    if action == "b":
        print("Get Balance")
        userPassword = input("Enter the password: ")
        if userPassword != accountpassword:
            print("Incorrect password")
        else:
            print("Your balance is: ", accountBalance)

    # deposit
    elif action == "d":
        print("Deposit")
        userDepositAmount = input("Please enter amount to deposit: ")
        userDepositAmount = int(userDepositAmount)
        userPassword = input("Enter your the password")

        if userDepositAmount < 0:
            print("You cannot deposit a negative amount")

        elif userPassword != accountpassword:
            print("Incorrect Password")

        else:
            accountBalance = accountBalance + userDepositAmount
            print("Your new balance is: ", accountBalance)

    # show
    elif action == "s":
        print("show")
        print(" Name: ", accountName)
        print(" Balance: ", accountBalance)
        print("password: ", accountpassword)

    # quit
    elif action == "q":
        break

    # withdraw
    elif action == "w":
        print("Withdraw:")

        userWithdrawAmount = input("Please enter the amount to withdraw: ")
        userWithdrawAmount = int(userWithdrawAmount)
        userPassword = input("Please enter the password: ")

        if userWithdrawAmount < 0:
            print("You cannot withdraw a negative amount")

        elif userPassword != accountpassword:
            print("incorrect password for this account")

        elif userWithdrawAmount > accountBalance:
            print("You cannot withdraw more than you have in your acount")

        else:
            accountBalance = accountBalance - userWithdrawAmount
            print("Your new balance is:", accountBalance)
            print("done")
