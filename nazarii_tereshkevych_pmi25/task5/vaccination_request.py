from validation import ValidatorDecorator


class VACCINATION_REQUEST:
    def __init__(self, ID=None, patient_name=None, patient_phone=None, vaccine=None, date=None, start_time=None,
                 end_time=None):
        self.ID = ID
        self.patient_name = patient_name
        self.patient_phone = patient_phone
        self.vaccine = vaccine
        self.date = date
        self.start_time = start_time
        self.end_time = end_time

    @property
    def ID(self):
        return self._ID

    @ID.setter
    @ValidatorDecorator.validate_number()
    def ID(self, value):
        self._ID = value

    @property
    def patient_name(self):
        return self._patient_name

    @patient_name.setter
    @ValidatorDecorator.validate_name
    def patient_name(self, value):
        self._patient_name = value

    @property
    def patient_phone(self):
        return self._patient_phone

    @patient_phone.setter
    @ValidatorDecorator.validate_number(0)
    def patient_phone(self, value):
        self._patient_phone = value

    @property
    def vaccine(self):
        return self._vaccine

    @vaccine.setter
    @ValidatorDecorator.validate_vaccine
    def vaccine(self, value):
        self._vaccine = value

    @property
    def date(self):
        return self._date

    @date.setter
    @ValidatorDecorator.validate_date
    def date(self, value):
        self._date = value

    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    @ValidatorDecorator.validate_time
    def start_time(self, value):
        self._start_time = value

    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    @ValidatorDecorator.validate_time
    def end_time(self, value):
        self._end_time = value

    def __str__(self):
        return f"ID: {self.ID}, Name: {self.patient_name}, Phone: {self.patient_phone}, " \
               f"Vaccine: {self.vaccine}, Date: {self.date}, Start Time: {self.start_time}, End Time: {self.end_time}"
