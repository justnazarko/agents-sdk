import re


class ValidatorDecorator:
    @staticmethod
    def validate_number(min_value=None, max_value=None):
        def decorator(func):
            def wrapper(self, value):
                if value is not None:  # Додайте перевірку на None
                    try:
                        value = float(value)
                        if (min_value is not None and value < min_value) or (max_value is not None and value > max_value):
                            raise ValueError(f"Invalid {func.__name__} value")
                        return func(self, value)
                    except ValueError:
                        raise ValueError(f"Invalid {func.__name__} value")
                return value  # Поверніть значення без змін, якщо воно дорівнює None
            return wrapper
        return decorator

    @staticmethod
    def validate_name(func):
        def wrapper(self, name):
            if name is not None:  # Додайте перевірку на None
                if re.search(r'[^a-zA-Z]', name):  # Дозволити лише букви алфавіту
                    raise ValueError(f"Invalid {func.__name__} value")
                return func(self, name)
            return name  # Поверніть значення без змін, якщо воно дорівнює None

        return wrapper

    @staticmethod
    def validate_vaccine(func):
        def wrapper(self, vaccine):
            if vaccine is not None:  # Додайте перевірку на None
                valid_vaccines = ["pfizer", "moderna", "AstraZeneca"]
                if vaccine not in valid_vaccines:
                    raise ValueError(f"Invalid {func.__name__} value")
                return func(self, vaccine)
            return vaccine  # Поверніть значення без змін, якщо воно дорівнює None
        return wrapper

    @staticmethod
    def validate_date(func):
        def wrapper(self, date):
            if date is not None:  # Додайте перевірку на None
                date_pattern = r'^\d{4}-\d{2}-\d{2}$'
                if not re.match(date_pattern, date):
                    raise ValueError(f"Invalid {func.__name__} value")
                return func(self, date)
            return date  # Поверніть значення без змін, якщо воно дорівнює None
        return wrapper

    @staticmethod
    def validate_time(func):
        def wrapper(self, time):
            if time is not None:  # Додайте перевірку на None
                time_pattern = r'^\d{2}:\d{2}$'
                if not re.match(time_pattern, time):
                    raise ValueError(f"Invalid {func.__name__} value")
                return func(self, time)
            return time  # Поверніть значення без змін, якщо воно дорівнює None
        return wrapper
