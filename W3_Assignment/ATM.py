def atm_withdrawal(balance, daily_withdrawn, amount):
    if amount % 500 != 0:
        print("Invalid amount. Must be a multiple of NPR 500.")
        return

    if amount > balance:
        print("Insufficient balance.")
        return

    if daily_withdrawn + amount > 50000:
        print("Daily withdrawal limit reached.")
        return

    new_balance = balance - amount
    print("Withdrawal successful.")
    print(f"Your current balance after withdrawal: NPR {new_balance}")

atm_withdrawal(balance=20000, daily_withdrawn=10000, amount=5000)