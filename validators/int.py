class IntChecker:

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, int_value):
        if not isinstance(int_value, int):
            raise ValueError("value must be an int")
        instance.__dict__[self.name] = int_value

    def __set_name__(self, owner, name):
        self.name = name