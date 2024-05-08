class Seat_Availability:
    def __init__(self, seat_counts):
        self.seat_counts = seat_counts
        self.available_seats = sum(seat_counts)
        self.reserved_seats = set()

    def update_seat_counts(self, new_seat_counts):
        self.seat_counts = new_seat_counts
        self.available_seats = sum(new_seat_counts)

    def check_seat_availability(self):
        return self.available_seats

    def manage_seat_reservations(self, reservation_data):
        show_time = reservation_data.get("show_time", "Morning Show")
        row_type = reservation_data.get("row_type", "Front")
        movie_name = reservation_data.get("movie_name", "Unknown")
        customer_name = reservation_data["customer_name"]
        seats_requested = reservation_data["seats_requested"]

        if row_type.lower() == "front":
            ticket_price = 50
        elif row_type.lower() == "middle":
            ticket_price = 100
        elif row_type.lower() == "upper":
            ticket_price = 150
        else:
            print("Invalid row type. Please try again.")
            return

        total_cost = ticket_price * seats_requested

        print(f"Booking details for {show_time}, {row_type} Row:")
        print(f"Movie Name: {movie_name}")
        print(f"Customer Name: {customer_name}")
        print(f"Number of Seats: {seats_requested}")
        print(f"Total Cost: {total_cost}")

        reserved_seat_numbers = []
        for i, row_count in enumerate(self.seat_counts, 1):
            if row_type.lower() in ["front", "middle", "upper"]:
                if row_type.lower() == "front" and i != 1:
                    continue
                if row_type.lower() == "middle" and i != 2:
                    continue
                if row_type.lower() == "upper" and i != 3:
                    continue

            seat_numbers = []
            for j in range(row_count):
                seat_number = sum(self.seat_counts[:i - 1]) + j + 1
                if seat_number not in self.reserved_seats:
                    self.reserved_seats.add(seat_number)
                    seat_numbers.append(seat_number)
                    reserved_seat_numbers.append(seat_number)
                    if len(seat_numbers) == seats_requested:
                        print(f"Reserved seats {seat_numbers} for {customer_name}")
                        break
            else:
                print(f"Not enough seats available for {customer_name}")
        return reserved_seat_numbers

    def cancel_reservation(self, reservation_data):
        customer_name = reservation_data["customer_name"]
        seats_to_cancel = reservation_data["seats_to_cancel"]

        canceled_seats = []
        for seat_number in seats_to_cancel:
            if seat_number in self.reserved_seats:
                self.reserved_seats.remove(seat_number)
                canceled_seats.append(seat_number)
        return canceled_seats


class RealTimeSeat_Availability(Seat_Availability):
    def __init__(self, seat_counts):
        super().__init__(seat_counts)

    def check_seat_availability(self):
        self.available_seats = sum(self.seat_counts)
        return self.available_seats


class SeatReservationSystem:
    def __init__(self, seat_counts, movies):
        self.movies = movies
        self.availability_system = RealTimeSeat_Availability(seat_counts)

    def check_seat_availability(self):
        return self.availability_system.check_seat_availability()

    def make_reservation(self, reservation_data):
        return self.availability_system.manage_seat_reservations(reservation_data)

    def cancel_reservation(self, reservation_data):
        return self.availability_system.cancel_reservation(reservation_data)