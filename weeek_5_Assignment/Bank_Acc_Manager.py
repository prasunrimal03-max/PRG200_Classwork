<<<<<<< HEAD
class BankAccount:
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance
 
    def deposit(self, amount):
        self.balance += amount
 
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
 
    def get_balance(self):
        print(f"{self.name} | Balance: NPR {self.balance}")
 
 
accounts_data = [
    ("Ramesh Thapa", "A001", 5000),
    ("Sunita Karki", "A002", 0),
    ("Bikash Rai",   "A003", 12000),
]
 
accounts = [BankAccount(name, acc_no, bal) for name, acc_no, bal in accounts_data]
 
print("=" * 50)
print("Question 1 - Bank Account Manager")
print("=" * 50)
 
accounts[1].deposit(3000)          # A002
accounts[2].withdraw(15000)        # A003, should fail
accounts[0].withdraw(2000)         # A001
 
for acc in accounts:
=======
class BankAccount:
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance
 
    def deposit(self, amount):
        self.balance += amount
 
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
 
    def get_balance(self):
        print(f"{self.name} | Balance: NPR {self.balance}")
 
 
accounts_data = [
    ("Ramesh Thapa", "A001", 5000),
    ("Sunita Karki", "A002", 0),
    ("Bikash Rai",   "A003", 12000),
]
 
accounts = [BankAccount(name, acc_no, bal) for name, acc_no, bal in accounts_data]
 
print("=" * 50)
print("Question 1 - Bank Account Manager")
print("=" * 50)
 
accounts[1].deposit(3000)          # A002
accounts[2].withdraw(15000)        # A003, should fail
accounts[0].withdraw(2000)         # A001
 
for acc in accounts:
>>>>>>> 48a5c3f (Assignment)
    acc.get_balance()