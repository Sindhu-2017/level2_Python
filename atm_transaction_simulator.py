# 3. ATM Transaction Simulator
#
# Create an ATM program that allows the user to:
#
# 1. Check Balance
#
# 2. Deposit
#
# 3. Withdraw
#
# 4. Change PIN
#
# 5. Exit
#
# Requirements:
#
# Maximum 3 PIN attempts.
#
# Withdrawal cannot exceed balance.
#
# Deposit must be positive.
#
# Use match-case.
#
# Use a loop to keep the ATM running.
#
# Use break for Exit.
account_holder_name = input("Enter the name of the account holder :")
balance = float(input("Enter the initial balance :"))

PIN = input("Enter the PIN :")

def checkBalance():
    print("Balance : ",balance)

def deposit(amount):
    if amount > 0 :
        global balance
        balance += amount
        print("Amount deposited successfully , Your current balance: ",balance)

def withdraw(amount):
    global balance
    if amount < balance :
        balance -= amount
        print("Amount withdrawn successfully , Your current balance: ",balance)
    else:
        print("Enter a valid amount to withdraw :")

def changePin(new_pin):
    global PIN
    PIN =new_pin

attempts = 0
max_attempts = 3
while attempts < max_attempts:
    attempts += 1
    key = input("Enter the PIN to access account:")
    if key == PIN :
        while True :
            print("Enter your choice :")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Change PIN")
            print("5. Exit")

            choice = int(input("Enter your choice :"))
            match choice:
                case 1:
                    print("Check Balance :")
                    checkBalance()

                case 2:
                    print("Deposit :")
                    amount = float(input("Enter the amount to deposit :"))
                    deposit(amount)

                case 3:
                    print("Withdraw :")
                    amount = float(input("Enter the amount to withdraw :"))
                    withdraw(amount)

                case 4:
                    print("Change PIN :")
                    new_pin = input("Enter the new PIN :")
                    changePin(new_pin)

                case 5:
                    print("Exit")
                    break

                case _:
                    print("Enter a valid choice :")

    else:
       print("Invalid pin ,Try again")

if attempts == max_attempts:
    print("Your attempts limit has been reached")