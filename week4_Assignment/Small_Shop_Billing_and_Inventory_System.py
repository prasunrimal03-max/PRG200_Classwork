def process_order(inventory, cart):
    bill = {}
    total = 0
 
    for item, qty in cart.items():
        if item not in inventory:
            print(f"Sorry, '{item}' is not sold here")
            continue
 
        available = inventory[item]["stock"]
        price = inventory[item]["price"]
 
        if qty <= available:
            item_total = price * qty
            bill[item] = (qty, item_total)
            total += item_total
            inventory[item]["stock"] -= qty
        else:
            print(f"Sorry, not enough stock for {item}")
 
    print("---- Bill ----")
    for item, (qty, item_total) in bill.items():
        print(f"{item} x{qty} = NPR {item_total}")
    print(f"Grand Total: NPR {total}")
    print("--------------")
 
    stock_parts = [f"{item}={data['stock']}" for item, data in inventory.items() if item in bill]
    print("Updated stock:", ", ".join(stock_parts))
 
 
inventory = {
    "rice":  {"price": 120, "stock": 20},
    "milk":  {"price": 90,  "stock": 10},
    "bread": {"price": 60,  "stock": 15},
    "eggs":  {"price": 15,  "stock": 30}
}
 
cart = {
    "rice": 2,
    "milk": 3,
    "eggs": 12
}
 
print("=" * 50)
print("Question 1 - Small Shop Billing and Inventory System")
print("=" * 50)
process_order(inventory, cart)