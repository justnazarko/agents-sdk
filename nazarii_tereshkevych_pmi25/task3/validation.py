import re


class Validator:
    @staticmethod
    def validate_number(value, min_value=None, max_value=None):
        try:
            value = float(value)
            if (min_value is not None and value < min_value) or (max_value is not None and value > max_value):
                return False
            return True
        except ValueError:
            return False

    @staticmethod
    def validate_name(name):
        # Перевірка на наявність цифр та спеціальних символів в імені
        if re.search(r'[0-9!@#$%^&*(),.?"{}|<>]', name):
            return False
        return True