class StringChecker:

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, str_value):
        if not isinstance(str_value, str):
            raise ValueError('valur must be a string')
        elif len(str_value) < 2:
            raise ValueError('minimum string length is 2')
        instance.__dict__[self.name] = str_value

    def __set_name__(self, owner, name):
        self.name = name
