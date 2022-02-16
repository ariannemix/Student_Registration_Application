from current_time import get_time


class Cohort:

    def __init__(self, cursor, connection):
        self.cursor = cursor
        self.connection = connection

    def view_cohorts(self):
        cohorts = self.cursor.execute(
            "SELECT cohort_id,start_date,end_date,co.active,c.name FROM Cohorts co JOIN Courses c ON c.course_id = co.course_id").fetchall()
        print(
            f"{'Cohort ID':^10}{'Active':^8}{'Name':^30}{'Start Date':^20}{'End Date':^20}\n{'-'*85}")
        for cohort in cohorts:
            if cohort[3] == 1:
                print(
                    f"{cohort[0]:^10}{'Y':^8}{cohort[4]:^30}{cohort[1]:^20}{str(cohort[2]):^20}")
            else:
                print(
                    f"{cohort[0]:^10}{'N':^8}{cohort[4]:^30}{cohort[1]:^20}{str(cohort[2]):^20}")
        action = input(f"\n(1) Create a cohort\n(2) Deactivate a cohort\n"
                       "(3) Activate a cohort \n(4) Return to Main Menu\n>>>")
        if action == '1':
            self.create_cohort()
        if action == '2':
            self.deactivate_cohort()
            pass
        if action == '3':
            self.activate_cohort()
            pass
        if action == '4':
            return

    def create_cohort(self):
        time = get_time()
        courses = self.cursor.execute("SELECT * FROM Courses").fetchall()
        print(f"\n{'ID':<5}{'Name'}\n{'-'*20}")
        for course in courses:
            if course[3] == 1:
                print(f"{course[0]:<5}{course[1]}")
        course_id = int(
            input(f"\nEnter a course ID to add to the Cohort.\n>>>"))
        people = self.cursor.execute(
            "SELECT person_id, first_name, last_name, active FROM People")
        print(f"{'ID':<3}{'Name'}\n{'-'*20}")
        for person in people:
            if person[3] == 1:
                print(f"{person[0]:<3}{person[2]}, {person[1]}")
        person_id = int(
            input(f"\nEnter a person ID to add to the Cohort.\n>>>"))
        self.cursor.execute(
            f"UPDATE People SET active = 0 WHERE person_id = {person_id}")
        self.connection.commit()
        self.cursor.execute(
            f"UPDATE Courses SET active = 0 WHERE course_id = {course_id}")
        self.connection.commit()
        insert_query = "INSERT INTO Cohorts (instructor_id, course_id, start_date) VALUES (?,?,?)"
        values = (person_id, course_id, time,)
        self.cursor.execute(insert_query, values)
        self.connection.commit()
        print("\nSUCCESS: Cohort successfully created.\n")

    def deactivate_cohort(self):
        cohorts = self.cursor.execute(
            "SELECT cohort_id,start_date,end_date,co.active,c.name FROM Cohorts co JOIN Courses c ON c.course_id = co.course_id").fetchall()
        print(
            f"{'Cohort ID':^10}{'Active':^8}{'Name':^30}{'Start Date':^20}{'End Date':^20}\n{'-'*85}")
        for cohort in cohorts:
            if cohort[3] == 1:
                print(
                    f"{cohort[0]:^10}{'Y':^8}{cohort[4]:^30}{cohort[1]:^20}{str(cohort[2]):^20}")
            else:
                print(
                    f"{cohort[0]:^10}{'N':^8}{cohort[4]:^30}{cohort[1]:^20}{str(cohort[2]):^20}")
        try:
            cohort_id = int(input(
                "\n**Please enter a cohort ID to deactivate.**\n>>>"))
        except:
            print("That isn't a valid ID")
            return
        self.cursor.execute(
            "UPDATE Cohorts SET active = 0 WHERE cohort_id = ?", (cohort_id,))
        self.connection.commit()
        print(
            f"SUCCESS: ID {cohort_id} succesfully deactivated!")
        return

    def activate_cohort(self):
        cohorts = self.cursor.execute(
            "SELECT cohort_id,start_date,end_date,co.active,c.name FROM Cohorts co JOIN Courses c ON c.course_id = co.course_id").fetchall()
        print(
            f"{'Cohort ID':^10}{'Active':^8}{'Name':^30}{'Start Date':^20}{'End Date':^20}\n{'-'*85}")
        for cohort in cohorts:
            if cohort[3] == 1:
                print(
                    f"{cohort[0]:^10}{'Y':^8}{cohort[4]:^30}{cohort[1]:^20}{str(cohort[2]):^20}")
            else:
                print(
                    f"{cohort[0]:^10}{'N':^8}{cohort[4]:^30}{cohort[1]:^20}{str(cohort[2]):^20}")
        try:
            cohort_id = int(input(
                "\n**Please enter a cohort ID to activate.**\n>>>"))
        except:
            print("That isn't a valid ID")
            return
        self.cursor.execute(
            "UPDATE Cohorts SET active = 1 WHERE cohort_id = ?", (cohort_id,))
        self.connection.commit()
        print(
            f"SUCCESS: ID {cohort_id} succesfully activated!")
        return
