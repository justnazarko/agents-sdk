from validation import Validator
import re


class VACCINATION_REQUEST:
    def __init__(self, ID, patient_name, patient_phone, vaccine, date, start_time, end_time):
        if not Validator.validate_number(ID):
            raise ValueError("Invalid ID")
        if not Validator.validate_name(patient_name):
            raise ValueError("Invalid patient name")
        if not Validator.validate_number(patient_phone):
            raise ValueError("Invalid patient phone")

        # Валідація для інших полів
        if not self.validate_vaccine(vaccine):
            raise ValueError("Invalid vaccine")
        if not self.validate_date(date):
            raise ValueError("Invalid date")
        if not self.validate_time(start_time):
            raise ValueError("Invalid start time")
        if not self.validate_time(end_time):
            raise ValueError("Invalid end time")

        self.ID = ID
        self.patient_name = patient_name
        self.patient_phone = patient_phone
        self.vaccine = vaccine
        self.date = date
        self.start_time = start_time
        self.end_time = end_time

    def validate_vaccine(self, vaccine):
        # Перевірка валідності вакцини (наприклад, чи вона є в списку допустимих значень)
        valid_vaccines = ["pfizer", "moderna", "AstraZeneca"]
        return vaccine in valid_vaccines

    def validate_date(self, date):
        # Перевірка валідності дати (формат YYYY-MM-DD)
        date_pattern = r'^\d{4}-\d{2}-\d{2}$'
        return bool(re.match(date_pattern, date))

    def validate_time(self, time):
        # Перевірка валідності часу (формат HH:MM)
        time_pattern = r'^\d{2}:\d{2}$'
        return bool(re.match(time_pattern, time))

    def __str__(self):
        return f"ID: {self.ID}, Name: {self.patient_name}, Phone: {self.patient_phone}, Vaccine: {self.vaccine}, Date: {self.date}, Start Time: {self.start_time}, End Time: {self.end_time}"