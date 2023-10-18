import sqlite3


def create_person_table():
    with conn:
        # Create person table
        query = "CREATE TABLE IF NOT EXISTS person (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age INTEGER);"
        cursor.execute(query)

        # Declare list of people in tuples
        people_list = [
            ('Jacinda', 33),
            ('Jeffrey', 37),
            ('Alandra', 2)
        ]

        # Insert people into table
        query = "INSERT INTO person (name, age) VALUES(?,?);"
        cursor.executemany(query, people_list)


def get_person_record_by_id(person_id):
    try:
        with conn:
            query = "SELECT * FROM person WHERE id = ?"
            cursor.execute(query, (person_id,))
            record = cursor.fetchone()
            return record
    except Exception as e:
        print(f"Error: {e}")
        return None


def get_person_table_columns():
    with conn:
        query = f"PRAGMA table_info(person);"
        cursor.execute(query)
        columns = [row[1] for row in cursor.fetchall()]
        return columns


def get_person_record_all():
    with conn:
        query = "SELECT * FROM person;"
        cursor.execute(query)
        records = cursor.fetchall()
        return records


def get_user_input_name():
    while True:
        name_input = input("Name: ").strip()
        if len(name_input) >= 3:
            return name_input
        else:
            print("Invalid name. Please try again.")


def get_user_input_age():
    while True:
        age_input = input("Age: ").strip()
        try:
            age = int(age_input)
            if age < 0:
                print("Age must be a positive number.")
            else:
                return age
        except ValueError:
            print("Invalid age. Please enter a valid number")


def insert_person_record(person_name, person_age):
    with conn:
        query = "INSERT INTO person (name,age) VALUES(?,?)"
        cursor.execute(query, (person_name, person_age))


# Create database in memory
conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

create_person_table()
records = get_person_record_all()
print("People in DB: " + str(len(records)))


cursor.close()
conn.close()
