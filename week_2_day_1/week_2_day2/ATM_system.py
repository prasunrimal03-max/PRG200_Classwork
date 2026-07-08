balance = 5000
pin = 2345

attempts = 3
logged_in = False

while attempts > 0:
    entered_pin = int(input("Enter PIN: "))
    if entered_pin == pin:
        print("Login success!")
        logged_in = True
        break
    else:
        attempts -= 1
        print(f"Wrong PIN. {attempts} attempt(s) left.")

if not logged_in:
    print("Too many failed attempts. Access denied.")
else:
    while True:
        print("1. Check Balance")
        print("2. Withdraw")
        print("3. Exit")

        choice = input("select: ")

        if choice == "1":
            print("Balance:", balance)
        elif choice == "2":
            amount = int(input("amount: "))
            if amount <= balance:
                balance -= amount
                print("new balance:", balance)
            else:
                print("not enough money!!!!!!!!")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")