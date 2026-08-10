TAX_RATE = 0.13   # global constant (13% VAT)


def apply_discount(price, percent):
    return price - (price * percent / 100)


def apply_tax(price):
    return price + (price * TAX_RATE)


def final_price(price, discount_pct):
    discounted = apply_discount(price, discount_pct)
    return apply_tax(discounted)