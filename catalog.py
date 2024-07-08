from datetime import datetime

from generator import generate_workers
from worker import Worker


class Catalog:
    def __init__(self):
        self.workers = []

    def add_worker(self, name, job, date_of_birth, phone_num, salary):
        worker = Worker(name, job, date_of_birth, phone_num, salary)
        self.workers.append(worker)

    def print_all_workers(self):
        if not self.workers:
            print("No workers available.")
        else:
            for worker in self.workers:
                print(worker.to_string())

    def generate_workers(self, count):
        for _ in range(count):
            name, job, birthday, phone, salary = generate_workers()
            self.add_worker(name, job, birthday, phone, salary)

    def remove_worker_by_id(self, worker_id):
        self.workers = [worker for worker in self.workers if worker.id != worker_id]

    def update_worker_by_id(self, worker_id, name=None, job=None, date_of_birth=None, phone_num=None, salary=None):
        for worker in self.workers:
            if worker.id == worker_id:
                if name is not None:
                    worker.name = name
                if job is not None:
                    worker.job = job
                if date_of_birth is not None:
                    worker.date_of_birth = date_of_birth
                if phone_num is not None:
                    worker.phone_num = phone_num
                if salary is not None:
                    worker.salary = salary
                break

    def find_workers(self, name=None, job=None, date_of_birth=None, start_date=None, end_date=None,
                     sort_by_salary=False):
        filtered_workers = self.workers

        if name is not None:
            temp_list = []
            for worker in filtered_workers:
                if worker.name == name:
                    temp_list.append(worker)
            filtered_workers = temp_list

        if job is not None:
            temp_list = []
            for worker in filtered_workers:
                if worker.job == job:
                    temp_list.append(worker)
            filtered_workers = temp_list
        if date_of_birth is not None:
            date_of_birth = datetime.strptime(date_of_birth, '%d-%m-%Y')
            temp_list = []
            for worker in filtered_workers:
                if datetime.strptime(worker.date_of_birth, '%d-%m-%Y') == date_of_birth:
                    temp_list.append(worker)
            filtered_workers = temp_list

        if start_date is not None:
            start_date = datetime.strptime(start_date, '%d-%m-%Y')
            filtered_workers = [worker for worker in filtered_workers if
                                datetime.strptime(worker.date_of_birth, '%d-%m-%Y') >= start_date]

        if end_date is not None:
            end_date = datetime.strptime(end_date, '%d-%m-%Y')
            filtered_workers = [worker for worker in filtered_workers if
                                datetime.strptime(worker.date_of_birth, '%d-%m-%Y') <= end_date]

        if sort_by_salary:
            filtered_workers.sort(key=lambda worker: worker.salary)

        result = []
        for worker in filtered_workers:
            result.append(worker.to_string())

        return result

    def get_worker_by_id(self, worker_id):
        for worker in self.workers:
            if worker.id == worker_id:
                print(worker.to_string())
                return
        print(f"Worker with ID {worker_id} not found.")
