import catalog

catalog = catalog.Catalog()

catalog.generate_workers(6)
catalog.add_worker("человек", "работящий", "01-01-1999", 4773847438437, 1000)
catalog.remove_worker_by_id(3)
catalog.find_workers(sort_by_salary=True)
catalog.print_all_workers()
print(catalog.find_workers(name="человек"))
print(f"\n" * 2)

print(catalog.find_workers(start_date="01-01-1999"))
print(f"\n")

print(catalog.get_worker_by_id(3))
print(catalog.get_worker_by_id(4))
