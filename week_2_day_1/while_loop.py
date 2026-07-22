business = []
units = []

for i in range(10):
    name = input("Enter business name: ")
    u = int(input("Enter units consumed: "))

    business.append(name)
    units.append(u)

for i in range(10):
    if units[i] <= 50:
        cost = units[i] * 5
    elif units[i] <= 100:
        cost = (50 * 5) + ((units[i] - 50) * 7)
    elif units[i] <= 150:
        cost = (50 * 5) + (50 * 7) + ((units[i] - 100) * 9)
    else:
        cost = (50 * 5) + (50 * 7) + (50 * 9) + ((units[i] - 150) * 11)

    print(business[i], "Electricity Bill =", cost)