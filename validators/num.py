
class NumChecker:
    def __init__(self, non_negative=False):
        self.non_negative = non_negative

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, (int, float)):
            raise ValueError('Value must be a number (int or float)')
        if self.non_negative and value < 0:
            raise ValueError('Value must be non-negative')
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name
