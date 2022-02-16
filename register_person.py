from numpy import insert
from current_time import get_time


class Register:

    def __init__(self, cursor, connection):
        self.cursor = cursor
        self.connection = connection

    def registration(self):
        action = input("\n**Please select an action.**\n\n(1) Add a person to a cohort\n(2) Remove a person from a cohort\n"
                       "(3) Mark a course as 'complete'\n(4) View all registrations for a cohort\n>>>")
        if action == '1':
            self.register_person()
        if action == '2':
            self.remove_student()
        if action == '3':
            self.complete_course()
        if action == '4':
            self.view_registrations()

    def register_person(self):
        people = self.cursor.execute(
            "SELECT person_id, first_name, last_name, active FROM People").fetchall()
        print(f"\n{'ID':<3}{'Full Name':^20}\n{'-'*25}")
        for person in people:
            if person[3] == 1:
                print(f"{person[0]:<3}{person[1]+' '+person[2]:^20}")
        student = int(input(
            "\nSelect a person to add to a cohort by typing their ID.\n>>>"))
        cohorts = self.cursor.execute(
            "SELECT co.cohort_id, c.name, p.first_name, p.last_name, co.active FROM Cohorts co JOIN Courses c ON c.course_id = co.course_id JOIN People p ON p.person_id = co.instructor_id")
        print(f"\n{'ID':<3}{'Course Name':^25}{'Instructor':^20}\n{'-'*55}")
        for cohort in cohorts:
            if cohort[4] == 1:
                print(
                    f"{cohort[0]:<3}{cohort[1]:^25}{cohort[2]+' '+cohort[3]:^20}")
        student_name = ''
        for person in people:
            if person[0] == student:
                student_name += f"{person[1]} {person[2]}"
        cohort = int(input(
            f"\nSelect the cohort you would like to add {student_name} to by typing it's ID.\n>>>"))
        current_time = get_time()
        insert_query = "INSERT INTO Student_Cohort_Registrations (student_id, cohort_id, registration_date) VALUES (?,?,?)"
        values = (student, cohort, current_time,)
        self.cursor.execute(insert_query, values)
        self.connection.commit()
        insert_query_1 = "UPDATE People SET active = 0 WHERE person_id = ?"
        values_1 = (student,)
        self.cursor.execute(insert_query_1, values_1)
        self.connection.commit()
        print(f"SUCCESS: {student_name} successfully added to the cohort.")
        return

    def remove_student(self):
        query = """SELECT s.student_id, p.first_name, p.last_name, co.name, s.registration_date, s.completion_date, s.drop_date, s.active
        FROM Student_Cohort_Registrations s JOIN People p ON p.person_id = s.student_id
        JOIN Cohorts c ON s.cohort_id = c.cohort_id
        JOIN Courses co ON co.course_id = c.course_id"""
        students = self.cursor.execute(query).fetchall()
        print(
            f"{'ID':<3}{'Active':^8}{'Class':^25}{'Name':^25}{'Registration Date':^25}{'Drop Date':^25}\n{'-'*110}")
        for student in students:
            if student[7] == 1:
                print(
                    f"{student[0]:<3}{'Y':^8}{student[3]:^25}{student[1]+' '+student[2]:^25}{student[4]:^25}")
        student_id = int(
            input("\nPlease type the ID of the active student you would like to remove.\n>>>"))
        current_time = get_time()
        update_query = "UPDATE Student_Cohort_Registrations SET active = 0, drop_date = ? WHERE student_id = ?"
        values = (current_time, student_id,)
        self.cursor.execute(update_query, values)
        self.connection.commit()
        print(f"SUCCESS: Student successfully removed from cohort.")

    def complete_course(self):
        query = """SELECT s.student_id, p.first_name, p.last_name, co.name, s.registration_date, s.completion_date, s.drop_date, s.active
        FROM Student_Cohort_Registrations s JOIN People p ON p.person_id = s.student_id
        JOIN Cohorts c ON s.cohort_id = c.cohort_id
        JOIN Courses co ON co.course_id = c.course_id"""
        students = self.cursor.execute(query).fetchall()
        print(
            f"\n{'ID':<3}{'Active':^8}{'Class':^25}{'Name':^25}{'Registration Date':^25}{'Drop Date':^25}\n{'-'*110}")
        for student in students:
            if student[7] == 1:
                print(
                    f"{student[0]:<3}{'Y':^8}{student[3]:^25}{student[1]+' '+student[2]:^25}{student[4]:^25}")
        student_id = int(
            input("\nPlease type the ID of the student that has completed their course.\n>>>"))
        current_time = get_time()
        update_query = "UPDATE Student_Cohort_Registrations SET completion_date = ?, active = 0 WHERE student_id = ?"
        values = (current_time, student_id,)
        self.cursor.execute(update_query, values)
        self.connection.commit()
        print("\nSUCCESS: Course successfully marked as complete\n")

    def view_registrations(self):
        query = """SELECT s.student_id, p.first_name, p.last_name, co.name, s.registration_date, s.completion_date, s.drop_date, s.active
        FROM Student_Cohort_Registrations s JOIN People p ON p.person_id = s.student_id
        JOIN Cohorts c ON s.cohort_id = c.cohort_id
        JOIN Courses co ON co.course_id = c.course_id"""
        students = self.cursor.execute(query).fetchall()
        print(
            f"{'ID':<3}{'Active':^8}{'Class':^25}{'Name':^25}{'Registration Date':^25}{'Completion Date':^25}{'Drop Date':^25}\n{'-'*130}")
        for student in students:
            if student[7] == 1:
                print(
                    f"{student[0]:<3}{'Y':^8}{student[3]:^25}{student[1]+' '+student[2]:^25}{student[4]:^25}")
            if student[7] == 0 and student[5] == None:
                print(
                    f"{student[0]:<3}{'N':^8}{student[3]:^25}{student[1]+' '+student[2]:^25}{student[4]:^25}{'Uncomplete':^25}{student[6]:^25}")
            if student[5] != None:
                print(
                    f"{student[0]:<3}{'N':^8}{student[3]:^25}{student[1]+' '+student[2]:^25}{student[4]:^25}{student[5]:^25}")
        action = input("\nPress <enter> to return to the homepage.\n>>>")
        if action:
            return
