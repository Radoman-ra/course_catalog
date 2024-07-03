import generator, creator

courses = []

def show_all_courses():
    for i in range(courses.__len__()):
        print(str(i), courses[i])

print("Welcome to Course Catalog!"
      "\n1.Do you want to add a course?"
      "\n2.Do you want to generate courses?")
match input():
    case "1":
        course = creator.add_course()
        courses.append(course)
    case "2":
        print("How many courses do you want to generate?")
        for i in range(int(input())):
            name, description, start_date, end_date, price = generator.generate_cours()
            course = creator.Course(name, description, start_date, end_date, price)
            courses.append(course)
print("Do you want to delite course?"
      "\n1.yes"
      "\n2.no")
match input():
    case "1":
        show_all_courses()
        id = input("Enter id: ")
        del courses[int(id)]
show_all_courses()








