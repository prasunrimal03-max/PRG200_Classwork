trips = [
    {"distance": 1.5, "hour": 14},
    {"distance": 5.0, "hour": 22},
    {"distance": 12.0, "hour": 3},
    {"distance": 8.5, "hour": 10},
    {"distance": 2.0, "hour": 23},
]

total_revenue = 0

for i, trip in enumerate(trips, start=1):
    distance = trip["distance"]
    hour = trip["hour"]

    if distance <= 2:
        fare = 150
    elif distance <= 10:
        fare = 150 + (distance - 2) * 35
    else:
        fare = 150 + 8 * 35 + (distance - 10) * 28

    is_night = hour >= 22 or hour < 5
    if is_night:
        fare += fare * 0.10

    night_note = " (Night surcharge applied)" if is_night else ""
    print(f"Trip {i}: Distance = {distance} km, Hour = {hour}:00 -> Fare = NPR {fare:.2f}{night_note}")
    total_revenue += fare

print()
print(f"Total revenue from all trips: NPR {total_revenue:.2f}")