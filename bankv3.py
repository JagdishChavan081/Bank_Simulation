# non -oop
# version :- 3
# two account

# first user
account0Name = ""
account0balance = 0
account0password = ""

# second user
account1Name = ""
account1balance = 0
account1password = ""


# new account
def newAccount(accountNumber, name, balance, password):
    global account0Name, account0balance, account0password
    global account1Name, account1balance, account1password

    if accountNumber == 0:
        account0Name = name
        account0balance = balance
        account0password = password

    if accountNumber == 1:
        account1Name = name
        account1balance = balance
        account1password = password


# show
# get balance
# deposit
# withdraw
