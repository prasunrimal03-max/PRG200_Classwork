def calculate_final_amount(total_purchase, is_loyalty_member):
    if total_purchase < 1000:
        discount_percent = 0
    elif total_purchase < 5000:
        discount_percent = 5
    elif total_purchase < 15000:
        discount_percent = 10
    else:
        discount_percent = 20

    amount_after_discount = total_purchase - (total_purchase * discount_percent / 100)

    if is_loyalty_member:
        amount_after_discount = amount_after_discount - (amount_after_discount * 5 / 100)

    print(f"Base discount applied: {discount_percent}%")
    if is_loyalty_member:
        print("Extra loyalty discount applied: 5%")
    print(f"Final payable amount: NPR {amount_after_discount:.2f}")

calculate_final_amount(3000, is_loyalty_member=True)