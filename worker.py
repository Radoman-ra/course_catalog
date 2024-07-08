from validators import int, string
id = 0
class Worker():
    phone_num = int.IntChecker()
    salary = int.IntChecker()
    name = string.StringChecker()
    job = string.StringChecker()
    def __init__(self, name, job, date_of_birth, phone_num, salary):
        global id
        self.id = id
        id += 1
        self.name = name
        self.job = job
        self.date_of_birth = date_of_birth
        self.phone_num = phone_num
        self.salary = salary
    def to_string(self):
        return f"ID: {self.id}, name: {self.name}, job: {self.job}, date of birth: {self.date_of_birth}, salary: {self.salary}"
