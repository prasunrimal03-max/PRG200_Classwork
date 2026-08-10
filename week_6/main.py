from discount import final_price, TAX_RATE

products = [
    ("Laptop",     85000, 10),
    ("Headphones", 4500,  15),
    ("Phone Case",  800,   5),
    ("USB Cable",   600,   0),
]

print(f"TAX_RATE imported: {TAX_RATE}")

for name, price, discount_pct in products:
    final = final_price(price, discount_pct)
    print(f"{name} | Original: NPR {price} | Final: NPR {final:.2f}")