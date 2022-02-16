class Course:

    def __init__(self, cursor, connection):
        self.cursor = cursor
        self.connection = connection

    def view_courses(self):
        courses = self.cursor.execute("SELECT * FROM Courses").fetchall()
        print(f"\n{'ID':<5}{'Active':<8}{'Name'}\n{'-'*20}")
        for course in courses:
            if course[3] == 1:
                print(f"{course[0]:<5}{'Y':^8}{course[1]}")
            else:
                print(f"{course[0]:<5}{'N':^8}{course[1]}")
        action = input(f"\n(1) Add a course \n(2) Deactivate a course \n"
                       "(3) Activate a course \n(0) Return to homepage\n>>>")
        if action == '1':
            self.add_course()
        if action == '2':
            self.deactivate_course()
        if action == '3':
            self.activate_course()
        if action == '0':
            return

    def add_course(self):
        print("\nPlease fill out the form to add a course. Press enter to skip a field.\n"
              "** Fields marked with '*' are required and cannot be skipped! **\n")
        name = input(f"{'Course Name*':<12}: ")
        description = input(f"{'Description':<12}: ")
        insert_query = "INSERT INTO Courses (name,description) VALUES (?,?)"
        values = (name, description,)
        self.cursor.execute(insert_query, values)
        self.connection.commit()
        new_course = self.cursor.execute(
            "SELECT name FROM Courses WHERE name = ?", (name,))
        for course in new_course:
            print(f"\nSUCCESS: {course[0]} succesfully added!\n")
        return

    def deactivate_course(self):
        courses = self.cursor.execute(
            "SELECT * FROM Courses").fetchall()
        print(f"\n{'ID':<5}{'Active':<8}{'Name'}\n{'-'*20}")
        for course in courses:
            if course[3] == 1:
                print(f"{course[0]:<5}{'Y':^8}{course[1]}")
            else:
                print(f"{course[0]:<5}{'N':^8}{course[1]}")
        try:
            course_id = int(input(
                "\n**Please enter a person ID to deactivate.**\n>>>"))
        except:
            print("That isn't a valid ID")
            return
        self.cursor.execute(
            "UPDATE Courses SET active = 0 WHERE course_id = ?", (course_id,))
        self.connection.commit()
        print(
            f"SUCCESS: ID {course_id} succesfully deactivated!")
        return

    def activate_course(self):
        courses = self.cursor.execute(
            "SELECT * FROM Courses").fetchall()
        print(f"\n{'ID':<5}{'Active':<8}{'Name'}\n{'-'*20}")
        for course in courses:
            if course[3] == 1:
                print(f"{course[0]:<5}{'Y':^8}{course[1]}")
            else:
                print(f"{course[0]:<5}{'N':^8}{course[1]}")
        try:
            course_id = int(input(
                "\n**Please enter a person ID to activate.**\n>>>"))
        except:
            print("That isn't a valid ID")
            return
        self.cursor.execute(
            "UPDATE Courses SET active = 1 WHERE course_id = ?", (course_id,))
        self.connection.commit()
        print(
            f"SUCCESS: ID {course_id} succesfully activated!")
        return
