total_cost_per_plate=70
selling_per_plate=140
number_of_plate=int(input("number of plates"))
total_revenue=selling_per_plate*number_of_plate
total_cost=number_of_plate*total_cost_per_plate
total_profit=total_revenue-total_cost
profit_margin=(total_profit/total_revenue)*100

print(f"total revenue = {total_revenue}")
print(f"total cost={total_cost}")
print(f"total profit={total_profit}")
print(f"total margin={profit_margin}")