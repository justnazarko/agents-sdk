from blablacar import BlablacarBooking, Time

def main():
    file_path = "booking.txt"
    bookings = BlablacarBooking.read_booking_from_file(file_path)

    for booking in bookings:
        print(f"Driver Name: {booking.driver_name}")
        print(f"No. of People: {booking.no_of_people}")
        print(f"Start Time: {booking.start_time.hour}:{booking.start_time.minute}")
        print(f"End Time: {booking.end_time.hour}:{booking.end_time.minute}")
        print(f"Start Place: {booking.start_place}")
        print(f"End Place: {booking.end_place}")
        print()

    # Тут ми додамо нові бронювання
    try:
        BlablacarBooking.add_booking("Nazarii", 2, Time(9, 30), Time(11, 00), "Lviv", "Kyiv")
        BlablacarBooking.add_booking("Alice", 2, Time(10, 00), Time(11, 00), "NewYork", "LasVegas")
        BlablacarBooking.add_booking("Bob", 2, Time(10, 30), Time(11, 30), "LosAngeles", "SanFrancisco")
        BlablacarBooking.add_booking("Charlie", 4, Time(14, 15), Time(17, 30), "Chicago", "Kyiv")
    except ValueError as e:
        print(f"Error: {str(e)}")

    # Тут ми перевіримо, чи нові бронювання були додані
    new_bookings = BlablacarBooking.bookings
    print("\nNew Bookings:")
    for booking in new_bookings:
        print(f"Driver Name: {booking.driver_name}")
        print(f"No. of People: {booking.no_of_people}")
        print(f"Start Time: {booking.start_time.hour}:{booking.start_time.minute}")
        print(f"End Time: {booking.end_time.hour}:{booking.end_time.minute}")
        print(f"Start Place: {booking.start_place}")
        print(f"End Place: {booking.end_place}")
        print()

    most_booked_hours = BlablacarBooking.most_booked_hours()
    print("\nMost Booked Hours:")
    for hour in most_booked_hours:
        print(f"Hour: {hour}")

    most_trips_driver = BlablacarBooking.driver_with_most_trips()
    print("\nDriver with Most Trips:")
    if most_trips_driver:
        print(f"Driver Name: {most_trips_driver}")

if __name__ == "__main__":
    main()
