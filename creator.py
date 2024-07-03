from datetime import datetime


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
        return (f"{self.name}"
                f"|{self.description}"
                f"|Start: {self.start_date.strftime('%d-%m-%Y')}"
                f"|Finish: {self.end_date.strftime('%d-%m-%Y')}"
                f"|Price:{self.price}$")
def add_course():
    print("Write the name of the course:")
    course_name = input()
    print("Write the description of the course:")
    course_description = input()
    print("Write the start date of the course (DD-MM-YYYY):")
    start_date = datetime.strptime(input(), "%d-%m-%Y").date()
    print("Write the end date of the course (DD-MM-YYYY):")
    end_date = datetime.strptime(input(), "%d-%m-%Y").date()
    print("Write the price of the course:")
    course_price = int(input())
    return Course(course_name, course_description, start_date, end_date, course_price)
