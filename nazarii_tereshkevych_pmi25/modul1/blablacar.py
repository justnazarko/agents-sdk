class Time:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

class BlablacarBooking:
    bookings = []

    def __init__(self, driver_name, no_of_people, start_time, end_time, start_place, end_place):
        self.set_driver_name(driver_name)
        self.set_no_of_people(no_of_people)
        self.set_start_time(start_time)
        self.set_end_time(end_time)
        self.set_start_place(start_place)
        self.set_end_place(end_place)

    def set_driver_name(self, driver_name):
        if driver_name.isalpha():
            self.driver_name = driver_name
        else:
            raise ValueError("DriverName should only contain letters.")

    def set_no_of_people(self, no_of_people):
        if 1 <= no_of_people <= 4:
            self.no_of_people = no_of_people
        else:
            raise ValueError("NoOfPeople should be between 1 and 4.")

    def set_start_time(self, start_time):
        if isinstance(start_time, Time):
            self.start_time = start_time
        else:
            raise ValueError("StartTime should be an instance of the Time class.")

    def set_end_time(self, end_time):
        if isinstance(end_time, Time) and end_time.hour >= self.start_time.hour and (end_time.hour > self.start_time.hour or end_time.minute >= self.start_time.minute):
            self.end_time = end_time
        else:
            raise ValueError("EndTime should be an instance of the Time class and should be greater than or equal to StartTime.")

    def set_start_place(self, start_place):
        if start_place.isalpha():
            self.start_place = start_place
        else:
            raise ValueError("StartPlace should only contain letters.")

    def set_end_place(self, end_place):
        if end_place.isalpha():
            self.end_place = end_place
        else:
            raise ValueError("EndPlace should only contain letters.")

    @classmethod
    def most_booked_hours(cls):
        hours_count = {}
        most_booked_hours = []

        for booking in cls.bookings:
            start_hour = booking.start_time.hour
            if start_hour in hours_count:
                hours_count[start_hour] += 1
            else:
                hours_count[start_hour] = 1

        max_count = max(hours_count.values())
        most_booked_hours = [hour for hour, count in hours_count.items() if count == max_count]

        return most_booked_hours

    @classmethod
    def driver_with_most_trips(cls):
        driver_trip_count = {}
        most_trips_driver = None

        for booking in cls.bookings:
            driver_name = booking.driver_name
            if driver_name in driver_trip_count:
                driver_trip_count[driver_name] += 1
            else:
                driver_trip_count[driver_name] = 1

        if driver_trip_count:
            most_trips_driver = max(driver_trip_count, key=driver_trip_count.get)

        return most_trips_driver
    @classmethod
    def add_booking(cls, driver_name, no_of_people, start_time, end_time, start_place, end_place):

        for booking in cls.bookings:
            if booking.driver_name == driver_name and booking.start_time == start_time:
                if booking.no_of_people + no_of_people > 4:
                    raise ValueError("Cannot book more than 4 people for the same driver and time.")
                if booking.end_place != start_place:
                    raise ValueError("Driver cannot be in two different places at the same time.")


        new_booking = BlablacarBooking(driver_name, no_of_people, start_time, end_time, start_place, end_place)
        cls.bookings.append(new_booking)
        return new_booking

    @staticmethod
    def read_booking_from_file(file_path):
        booking_list = []

        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()

            for line in lines:
                data = line.strip().split(',')
                if len(data) == 6:
                    driver_name, no_of_people, start_time, end_time, start_place, end_place = data

                    start_hour, start_minute = map(int, start_time.split(':'))
                    end_hour, end_minute = map(int, end_time.split(':'))
                    start_time_obj = Time(start_hour, start_minute)
                    end_time_obj = Time(end_hour, end_minute)

                    booking = BlablacarBooking(driver_name, int(no_of_people), start_time_obj, end_time_obj,
                                               start_place, end_place)
                    booking_list.append(booking)

        except FileNotFoundError:
            print(f"File not found: {file_path}")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

        return booking_list