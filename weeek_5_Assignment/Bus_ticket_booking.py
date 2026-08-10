<<<<<<< HEAD
class Bus:
    def __init__(self, route, total_seats):
        self.route = route
        self.total_seats = total_seats
        self.booked = {}   # seat_number -> passenger_name
 
    def book_seat(self, seat_number, passenger_name):
        if seat_number in self.booked:
            print("Seat already booked")
        else:
            self.booked[seat_number] = passenger_name
 
    def available_seats(self):
        return self.total_seats - len(self.booked)
 
    def passenger_list(self):
        print(f"Passenger list for {self.route}:")
        for seat, passenger in self.booked.items():
            print(f"Seat {seat}: {passenger}")
 
 
bus = Bus("Kathmandu - Pokhara", 10)
 
bookings = [
    (3, "Ramila Shrestha"),
    (7, "Deepak Gurung"),
    (3, "Anita Rai"),        # duplicate
    (1, "Prakash Magar"),
    (7, "Suman Tamang"),     # duplicate
]
 
print()
print("=" * 50)
print("Question 4 - Bus Ticket Booking (Sajha Yatayat)")
print("=" * 50)
for seat, passenger in bookings:
    bus.book_seat(seat, passenger)
 
print(f"Available seats: {bus.available_seats()}")
=======
class Bus:
    def __init__(self, route, total_seats):
        self.route = route
        self.total_seats = total_seats
        self.booked = {}   # seat_number -> passenger_name
 
    def book_seat(self, seat_number, passenger_name):
        if seat_number in self.booked:
            print("Seat already booked")
        else:
            self.booked[seat_number] = passenger_name
 
    def available_seats(self):
        return self.total_seats - len(self.booked)
 
    def passenger_list(self):
        print(f"Passenger list for {self.route}:")
        for seat, passenger in self.booked.items():
            print(f"Seat {seat}: {passenger}")
 
 
bus = Bus("Kathmandu - Pokhara", 10)
 
bookings = [
    (3, "Ramila Shrestha"),
    (7, "Deepak Gurung"),
    (3, "Anita Rai"),        # duplicate
    (1, "Prakash Magar"),
    (7, "Suman Tamang"),     # duplicate
]
 
print()
print("=" * 50)
print("Question 4 - Bus Ticket Booking (Sajha Yatayat)")
print("=" * 50)
for seat, passenger in bookings:
    bus.book_seat(seat, passenger)
 
print(f"Available seats: {bus.available_seats()}")
>>>>>>> 48a5c3f (Assignment)
bus.passenger_list()