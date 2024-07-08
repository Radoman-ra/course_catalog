import catalog
from worker import Worker

catalog = catalog.Catalog()

print("\ngeneration of workers")
catalog.generate_workers(6)
catalog.print_all_workers()

print("\nadding worker")
worker = Worker("человек", "работящий", "01-01-1999", 4773847438437, 1000)
catalog.add_worker(worker)
print(worker.to_string())

print("\ndel worker by id: 3")
catalog.remove_worker_by_id(3)
catalog.print_all_workers()

print("\nsort by salary")
catalog.find_workers(sort_by_salary=True)
catalog.print_all_workers()

print("\nfind workers by name")
print(catalog.find_workers(name="человек"))

print("\nfind worker by id: 3(del) and 4")
for id in [3, 4]:
    worker = catalog.get_worker_by_id(id)
    if worker is None:
        print(f"Worker not found id:{id}")
    else:
        print(worker.to_string())

print("\nworkers date of birth from 01-01-1999")
print(catalog.find_workers(start_date="01-01-1999"))
