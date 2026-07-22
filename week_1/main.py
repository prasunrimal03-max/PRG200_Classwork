name = input("Enter the name of money sender: ")
send_money = int(input("Enter the money in USD: "))

conversion_rate = 152
bank_charge = 0.05

convert_money = send_money*conversion_rate + send_money*bank_charge

print(f"Converted money: NPR {convert_money}")

# print(convert_money)