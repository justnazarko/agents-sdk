class Validator:
    @staticmethod
    def is_positive_integer(value):
        try:
            value = int(value)
            return value > 0
        except ValueError:
            return False

    @staticmethod
    def is_non_negative_integer(value):
        try:
            value = int(value)
            return value >= 0
        except ValueError:
            return False

    @staticmethod
    def is_integer(value):
        try:
            int(value)
            return True
        except ValueError:
            return False
