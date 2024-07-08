import validators
id = 0


class Worker():
    phone_num = validators.NumChecker()
    salary = validators.NumChecker()
    name = validators.StringChecker()
    job = validators.StringChecker()
    date_of_birth = validators.DateOfBirthChecker()
    id = 0

    def __init__(self, name, job, date_of_birth, phone_num, salary):
        self.id = Worker.id
        Worker.id += 1
        self.name = name
        self.job = job
        self.date_of_birth = date_of_birth
        self.phone_num = phone_num
        self.salary = salary

    def to_string(self):
        return f"ID: {self.id}, name: {self.name}, job: {self.job}, date of birth: {self.date_of_birth}, phone number:{self.phone_num}, salary: {self.salary}"
