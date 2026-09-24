# 11. Mini Banking Application ⭐⭐⭐
# Implement:
# 1. Create Account
# 2. Deposit
# 3. Withdraw
# 4. Check Balance
# 5. Transaction History
# 6. Exit
# Apply:
# loops 
# conditions 
# match-case 
# lists 
# dictionaries 
# validation 
# break

accounts = {}
while True :
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Transaction History")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            account_no = input("Enter account number: ")
            if account_no in accounts:
                print("Account already exists.")
            else:
                name = input("Enter account holder name: ")
                accounts[account_no] = {
                    "name": name,
                    "balance": 0.0,
                    "transactions": []
                }
                print("Account created successfully.")

        case 2:
            account_no = input("Enter account number: ")

            if account_no not in accounts:
                print("Account not found.")
                continue
            else:
                amount = float(input("Enter deposit amount: "))
                if amount <= 0:
                    print("Amount must be greater than 0.")
                else:
                    accounts[account_no]["balance"] += amount
                    accounts[account_no]["transactions"].append(f"Deposited: {amount:.2f}")
                    print("Deposit successful.")

        case 3:
            account_no = input("Enter account number: ")

            if account_no not in accounts:
                print("Account not found.")
                continue
            else:
                amount = float(input("Enter withdrawal amount: "))

                if amount <= 0:
                    print("Amount must be greater than 0.")
                elif amount > accounts[account_no]["balance"]:
                    print("Insufficient balance.")
                else:
                    accounts[account_no]["balance"] -= amount
                    accounts[account_no]["transactions"].append(f"Withdrawn: {amount:.2f}")
                    print("Withdrawal successful.")

        case 4:
            account_no = input("Enter account number: ")

            if account_no in accounts:
                print(f"Account Holder: {accounts[account_no]['name']}")
                print(f"Balance: {accounts[account_no]['balance']:.2f}")
            else:
                print("Account not found.")

        case 5:
            account_no = input("Enter account number: ")
            if account_no in accounts:
                transactions = accounts[account_no]["transactions"]
                if transactions:
                    print("Transaction History:")
                    for transaction in transactions:
                        print(transaction)
                else:
                    print("No transactions yet.")
            else:
                print("Account not found.")

        case 6:
            print("Thank you for using the banking application.")
            break

        case _:
            print("Invalid choice")







            



