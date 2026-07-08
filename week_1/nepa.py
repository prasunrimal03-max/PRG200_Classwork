current_units=int(input("Enter the current unit"))
previous_units=int(input("Enter the previous unit"))
FlatPer_unit=0.01
meter_charge=100
unit_consumed =current_units-previous_units
total_bill= unit_consumed*FlatPer_unit+meter_charge
print(total_bill)