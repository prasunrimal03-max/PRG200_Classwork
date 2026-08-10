def atm(account_id, pin, action, amount=0):
    account = accounts.get(account_id)
    if not account:
        return print("Account not found")
    if account["pin"] != pin:
        return print("Incorrect PIN")
 
    name = account["name"]
    if action == "balance":
        print(f"{name} | Balance: NPR {account['balance']}")
    elif action == "deposit":
        account["balance"] += amount
        print(f"{name} | Deposited NPR {amount} | New Balance: NPR {account['balance']}")
    elif action == "withdraw":
        if amount > account["balance"]:
            print("Insufficient funds")
        else:
            account["balance"] -= amount
            print(f"{name} | Withdrew NPR {amount} | New Balance: NPR {account['balance']}")
 
 
accounts = {
    "A001": {"name": "Ramesh Thapa", "balance": 15000, "pin": "1234"},
    "A002": {"name": "Sunita Karki", "balance": 8500,  "pin": "5678"},
    "A003": {"name": "Bikash Rai",   "balance": 22000, "pin": "9012"}
}
 
print()
print("=" * 50)
print("Question 5 - Simple ATM Simulator")
print("=" * 50)
atm("A001", "1234", "balance")
atm("A002", "0000", "withdraw", 2000)   # wrong PIN
atm("A002", "5678", "deposit",  3000)
atm("A003", "9012", "withdraw", 25000)  # insufficient funds
atm("A004", "1111", "balance")          # account not found