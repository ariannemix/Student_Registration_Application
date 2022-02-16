import sqlite3
from People import Person
from Courses import Course
from Cohorts import Cohort
from register_person import Register

connection = sqlite3.connect('cohort_data.db')
cursor = connection.cursor()
person = Person(cursor, connection)
course = Course(cursor, connection)
cohort = Cohort(cursor, connection)
register = Register(cursor, connection)

while True:
    print("\n*** Student Registration ***\n")
    try:
        user_action = int(input("(1) People\n"
                                "(2) Courses\n"
                                "(3) Cohorts\n"
                                "(4) Register\n"
                                "(0) Exit\n"
                                ">>>"))
    except:
        print("\nPlease enter a valid input.\n")
        continue
    if user_action == 1:
        person.view_people()
    if user_action == 2:
        course.view_courses()
    if user_action == 3:
        cohort.view_cohorts()
    if user_action == 4:
        register.registration()
    if user_action == 0:
        print("\nThank you, have a nice day!!\n")
        break
