from validators import num, string, date_of_birth

id = 0


class Worker():
    phone_num = num.NumChecker()
    salary = num.NumChecker()
    name = string.StringChecker()
    job = string.StringChecker()
    date_of_birth = date_of_birth.DateOfBirthChecker()
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
