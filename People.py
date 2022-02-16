
class Person:

    def __init__(self, cursor, connection):
        self.cursor = cursor
        self.connection = connection

    def view_people(self):
        people = self.cursor.execute(
            "SELECT person_id, first_name, last_name, active FROM People")
        print(f"{'ID':<3}{'Active':<8}{'Name'}\n{'-'*20}")
        for person in people:
            if person[3] == 1:
                print(f"{person[0]:<3}{'Y':^8}{person[2]}, {person[1]}")
            else:
                print(f"{person[0]:<3}{'N':^8}{person[2]}, {person[1]}")
        action = input(f"\n(1) Add a person\n(2) Deactivate a person\n(3) Activate a person\n"
                       "(4) Assign a person to a cohort\n(0) Return to homepage\n>>>")
        if action == '1':
            self.add_person()
        if action == '2':
            self.deactivate_person()
        if action == '3':
            self.activate_person()
        if action == '4':
            print("coming soon.")
        if action == '0':
            return

    def add_person(self):
        print("\nPlease fill out the form to add a person. Press enter to skip a field.\n"
              "** Fields marked with '*' are required and cannot be skipped! **\n")
        first_name = input(f"{'First Name*':<12}: ")
        last_name = input(f"{'Last Name':<12}: ")
        email = input(f"{'Email*':<12}: ")
        phone = input(f"{'Phone':<12}: ")
        password = input(f"{'Password*':<12}: ")
        address = input(f"{'Address':<12}: ")
        city = input(f"{'City':<12}: ")
        state = input(f"{'State':<12}: ")
        postal_code = input(f"{'Zipcode':<12}: ")
        insert_query = "INSERT INTO People (first_name,last_name,email,phone,password,address,city,state,postal_code) VALUES (?,?,?,?,?,?,?,?,?)"
        values = (first_name, last_name, email, phone,
                  password, address, city, state, postal_code,)
        self.cursor.execute(insert_query, values)
        self.connection.commit()
        new_person = self.cursor.execute(
            f"SELECT first_name FROM People WHERE first_name = ?", (first_name,))
        for name in new_person:
            print(f"\nSUCCESS: {name[0]} succesfully added!\n")
        return

    def deactivate_person(self):
        people = self.cursor.execute(
            "SELECT person_id, first_name, last_name, active FROM People")
        print(f"{'ID':<3}{'Active':<8}{'Name'}\n{'-'*20}")
        for person in people:
            if person[3] == 1:
                print(f"{person[0]:<3}{'Y':^8}{person[2]}, {person[1]}")
            else:
                print(f"{person[0]:<3}{'N':^8}{person[2]}, {person[1]}")
        try:
            person_id = int(input(
                "\n**Please enter a person ID to deactivate.**\n>>>"))
        except:
            print("That isn't a valid ID")
            return
        self.cursor.execute(
            "UPDATE People SET active = 0 WHERE person_id = ?", (person_id,))
        self.connection.commit()
        print(
            f"SUCCESS: ID {person_id} succesfully deactivated!")
        return

    def activate_person(self):
        people = self.cursor.execute(
            "SELECT person_id, first_name, last_name, active FROM People")
        print(f"{'ID':<3}{'Active':<8}{'Name'}\n{'-'*20}")
        for person in people:
            if person[3] == 1:
                print(f"{person[0]:<3}{'Y':^8}{person[2]}, {person[1]}")
            else:
                print(f"{person[0]:<3}{'N':^8}{person[2]}, {person[1]}")
        try:
            person_id = int(input(
                "\n**Please enter a person ID to activate.**\n>>>"))
        except:
            print("That isn't a valid ID")
            return
        self.cursor.execute(
            "UPDATE People SET active = 1 WHERE person_id = ?", (person_id,))
        self.connection.commit()
        print(
            f"SUCCESS: ID {person_id} succesfully activated!")
        return
