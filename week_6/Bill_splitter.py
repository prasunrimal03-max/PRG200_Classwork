import random

random.seed(42)

friends = ["Ramesh", "Sunita", "Bikash", "Anjali", "Dipak"]
total_bill = 3750


def split_bill(friends, total):
    return total / len(friends)


def pick_lucky(friends):
    return random.choice(friends)


def final_summary(friends, total):
    share = split_bill(friends, total)
    lucky_person = pick_lucky(friends)

    print(f"Each person pays: NPR {share:.2f}")
    print(f"Lucky person (pays extra NPR 50): {lucky_person}")

    lucky_total = share + 50   
    print(f"{lucky_person}'s total: NPR {lucky_total:.2f}")


final_summary(friends, total_bill)