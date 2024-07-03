import generator, creator

courses = []
id = 0

def add_course(course):
    global id
    courses.append(course)
    id += 1
for i in range(5):
    name, description, start_date, end_date, price = generator.generate_cours()
    cours = creator.Course(name, description, start_date, end_date, price)
    add_course(cours)

for i in range(courses.__len__()):
    print(str(i), courses[i])
    print("-" * 100)

