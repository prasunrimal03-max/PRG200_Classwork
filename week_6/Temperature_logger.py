import math

station_name = "Kathmandu Weather Station"   # global variable

temperatures = [18.4, 22.1, 15.7, 29.3, 11.8, 25.6, 19.2]


def get_average(temps):
    return sum(temps) / len(temps)


def get_deviation(temps):
    mean_temp = get_average(temps)   # local variable, only exists inside this function
    squared_diffs = [(t - mean_temp) ** 2 for t in temps]
    return math.sqrt(sum(squared_diffs) / len(temps))


def get_summary(temps):
    print(f"--- {station_name} ---")
    print(f"Min: {min(temps)}")
    print(f"Max: {max(temps)}")
    print(f"Average: {get_average(temps):.2f}")
    print(f"Deviation: {get_deviation(temps):.2f}")


get_summary(temperatures)

# mean_temp only exists inside get_deviation() - it is a local variable,
# so Python deletes it once the function finishes running.
# Trying to use it here raises a NameError because it was never
# created in this (global) scope.
try:
    print(mean_temp)
except NameError as e:
    print(f"NameError: {e}")