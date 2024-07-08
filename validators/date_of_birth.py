from datetime import datetime

class DateOfBirthChecker:

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, date_of_birth_value):
        if not isinstance(date_of_birth_value, str):
            raise ValueError('Date of birth must be a string')
        try:
            datetime.strptime(date_of_birth_value, '%d-%m-%Y')
        except ValueError:
            raise ValueError('Date of birth must be in the format dd-mm-yyyy')
        instance.__dict__[self.name] = date_of_birth_value

    def __set_name__(self, owner, name):
        self.name = name
