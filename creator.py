class Course:
    def __init__(self, course_name, course_description, start_date, end_date, course_price):

        if not isinstance(course_name, str) or not course_name:
            raise ValueError("Course name must be a non-empty string")
        if not isinstance(course_description, str) or not course_description:
            raise ValueError("Course description must be a non-empty string")
        if not isinstance(course_price, (int, float)) or course_price <= 0:
            raise ValueError("Course price must be a positive number")
        if start_date >= end_date:
            raise ValueError("Start date must be before end date")

        self.name = course_name
        self.description = course_description
        self.start_date = start_date
        self.end_date = end_date
        self.price = course_price

    def __str__(self):
        return (f"{self.name:^99}"
                f"\n\n{self.description}\n"
                f"\nStart: \t\t\t\t{self.start_date}"
                f"\nFinish: \t\t\t{self.end_date}"
                f"\nPrice is only:\t\t\t{self.price}$")