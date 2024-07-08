import random

from faker import Faker

fake = Faker("ru_RU")


def generate_worker():
    name = fake.name()
    job = fake.job()
    birthday = fake.date_of_birth()
    birthday = birthday.strftime('%d-%m-%Y')
    phone = fake.random_number(digits=11, fix_len=True)
    salary = round(random.uniform(500, 1000), 2)
    return name, job, birthday, phone, salary
