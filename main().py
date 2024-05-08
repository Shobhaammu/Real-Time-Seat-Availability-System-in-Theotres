from seat import SeatReservationSystem

if __name__ == "__main__":
    seat_counts = [20, 30, 50]  # Seat counts for each row [Front, Middle, Upper]
    movies = ["family star", "tillu2", "kgf2"]
    reservation_system = SeatReservationSystem(seat_counts, movies)
    print("Welcome to Seat Reservation System")
    
    while True:
        print("\nSelect Show Time:")
        print("1. Morning Show")
        print("2. Afternoon Show")
        print("3. Night Show")
        print("4. Exit")
        show_choice = input("Enter your choice: ")

        if show_choice == "4":
            print("Thank you for using Seat Reservation System. Goodbye!")
            break

        if show_choice == "1":
            show_time = "Morning Show"
        elif show_choice == "2":
            show_time = "Afternoon Show"
        elif show_choice == "3":
            show_time = "Night Show"
        else:
            print("Invalid show time choice. Please try again.")
            continue

        print("Available Movies:")
        for i, movie in enumerate(movies, 1):
            print(f"{i}. {movie}")

        movie_choice = input("Enter movie choice (1-3): ")
        if movie_choice not in ["1", "2", "3"]:
            print("Invalid movie choice. Please try again.")
            continue

        movie_name = movies[int(movie_choice) - 1]
        current_seat_availability = reservation_system.check_seat_availability()
        print(f"Current Seat Availability: {current_seat_availability}")

        row_type = input("Select Row Type (Front, Middle, Upper): ")
        if row_type.lower() not in ["front", "middle", "upper"]:
            print("Invalid row type. Please try again.")
            continue

        customer_name = input("Enter your name: ")
        seats_requested = int(input("Enter number of seats to book: "))

        reservation_data = {
            "show_time": show_time,
            "row_type": row_type,
            "movie_name": movie_name,
            "customer_name": customer_name,
            "seats_requested": seats_requested
        }
        reserved_seats = reservation_system.make_reservation(reservation_data)
        
        cancel_choice = input("Do you want to cancel any seats? (yes/no): ")
        if cancel_choice.lower() == "yes":
            seats_to_cancel = list(map(int, input("Enter seat numbers to cancel (comma-separated): ").split(',')))
            cancel_data = {
                "customer_name": customer_name,
                "seats_to_cancel": seats_to_cancel
            }
            canceled_seats = reservation_system.cancel_reservation(cancel_data)
            print(f"Canceled seats: {canceled_seats}")