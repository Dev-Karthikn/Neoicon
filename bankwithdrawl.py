# Bank_balance=10000
# No_of_Transactions=[]
# max_transactions=5

# while No_of_Transactions>max_transactions:
#     decision=input("Which Transaction Type do u like to Perform ? (w/d): ")
#     if decision=="w":
#         amount=int(input("Enter the amount to withdrawl: "))
#         if amount>Bank_balance:
#             print("Insufficient balance")
#             continue
#     elif(amount<=Bank_balance):
#         Bank_balance=Bank_balance-amount
#         print("Withdrawl successful,Your available Balance Now is : ₹",Bank_balance)
#         No_of_Transactions+=1
        
#     if(decision =="d"):
#         amount=int(input("Enter the amount to deposit:  ₹ "))
#         Bank_balance=Bank_balance+amount
#         print("Deposit successful,Your available Balance Now is:  ₹",Bank_balance)
#         No_of_Transactions+=1
# print("Transaction Limit has been reached !")  
   


# Initial balance
balance = 10000
transaction_count = 0
max_transactions = 5

print("Welcome to SimpleBank!")
print("Initial Balance: ₹10000\n")

while transaction_count < max_transactions:
    print(f"Transaction {transaction_count + 1} of {max_transactions}")
    action = input("Enter 'd' to Deposit or 'w' to Withdraw: ").lower()
    
    if action not in ['d', 'w']:
        print("Invalid option. Please enter 'd' or 'w'.\n")
        continue

    amount = float(input("Enter the amount: ₹"))

    if amount <= 0:
        print("Amount must be greater than 0.\n")
        continue

    if action == 'd':
        balance += amount
        print(f"Deposited ₹{amount:.2f}")
    elif action == 'w':
        if amount > balance:
            print("Insufficient balance!,Your balance is",balance ,"only,Try again!")
            continue
        balance -= amount
        print(f"Withdrew ₹{amount:.2f}")
    
    transaction_count += 1
    print(f"Updated Balance: ₹{balance:.2f}\n")

print("Transaction limit reached. Try again tomorrow.")



