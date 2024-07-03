from faker import Faker
from datetime import timedelta

fake = Faker()

def generate_cours():
    name = fake.job()
    description = fake.text(max_nb_chars=300)
    start_date = fake.date_this_year(before_today=False, after_today=True)
    end_date = start_date + timedelta(days=fake.random_int(min=30, max=180))
    price = (fake.random_int(min=1, max=10) * 100)- 1
    return name, description, start_date, end_date, price