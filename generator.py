from faker import Faker
from datetime import timedelta

fake = Faker("ru_RU")

def generate_cours():
    name = fake.name()
    job = fake.job()
    birthday = fake.date_between()
    phone = fake.phone_number()
    salary = fake.random_int(min=1, max=100)
    return name, job, birthday, phone, salary