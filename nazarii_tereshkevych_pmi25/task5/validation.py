import re


class ValidatorDecorator:
    @staticmethod
    def validate_number(min_value=None, max_value=None, error_message="Invalid number"):
        def decorator(func):
            def wrapper(self, value):
                if value is not None:
                    try:
                        value = float(value)
                        if (min_value is not None and value < min_value) or (max_value is not None and value > max_value):
                            raise ValueError(error_message)
                        return func(self, value)
                    except ValueError:
                        raise ValueError(error_message)
                return value
            return wrapper
        return decorator

    @staticmethod
    def validate_name(func):
        error_message = "Invalid name. Please enter only letters."
        def wrapper(self, name):
            if name is not None:
                if re.search(r'[^a-zA-Z]', name):
                    raise ValueError(error_message)
                return func(self, name)
            return name

        return wrapper

    @staticmethod
    def validate_vaccine(func):
        error_message = "Invalid vaccine. Please choose from pfizer, moderna, AstraZeneca."
        def wrapper(self, vaccine):
            if vaccine is not None:
                valid_vaccines = ["pfizer", "moderna", "AstraZeneca"]
                if vaccine not in valid_vaccines:
                    raise ValueError(error_message)
                return func(self, vaccine)
            return vaccine
        return wrapper

    @staticmethod
    def validate_date(func):
        error_message = "Invalid date format. Please use YYYY-MM-DD."
        def wrapper(self, date):
            if date is not None:
                date_pattern = r'^\d{4}-\d{2}-\d{2}$'
                if not re.match(date_pattern, date):
                    raise ValueError(error_message)
                return func(self, date)
            return date
        return wrapper

    @staticmethod
    def validate_time(func):
        error_message = "Invalid time format. Please use HH:MM."
        def wrapper(self, time):
            if time is not None:
                time_pattern = r'^\d{2}:\d{2}$'
                if not re.match(time_pattern, time):
                    raise ValueError(error_message)
                return func(self, time)
            return time
        return wrapper
