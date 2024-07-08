import re

class PhoneNumberChecker:

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, phone_num_value):
        if not isinstance(phone_num_value, str):
            raise ValueError('Phone number must be a string')
        # Обновлено регулярное выражение для проверки формата +7 (XXX) YYY-ZZZZ
        pattern = r'^\+7 \(\d{3}\) \d{3}-\d{4}$'
        if not re.match(pattern, phone_num_value):
            raise ValueError('Phone number must be in the format +7 (XXX) YYY-ZZZZ where X, Y, Z are digits')
        instance.__dict__[self.name] = phone_num_value

    def __set_name__(self, owner, name):
        self.name = name
