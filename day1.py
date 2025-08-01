class dog:
     print("bark")
class lion:
    print("roar")

class wild(dog,lion):
    print("Enga area ulla varadha")
a=wild()
#  Multiple inheritance
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance  # Private variable

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance

# Using the class
account = BankAccount("Alice", 1000)
account.deposit(500)
account.withdraw(200)

print(account.get_balance())  # Output: 1300

# Try accessing private variable directlyacc
acc=BankAccount("Karthikeyan",35000)
acc.withdraw(20000)
acc.deposit(100000)
print(acc.get_balance())  # Output: 150000