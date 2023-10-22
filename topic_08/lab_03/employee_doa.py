# Create Python module with the following functions:
# a. createDatabase(db_name) # creates a SQLite database to store Employee records
# b. createEmployeeTable(table_name) # Creates a Table to store Employee records (columns must
# match the attributes defined in above Employee class
# c. addEmployeeToDB(employee_object) # adds an Employee object to database
# d. getEmployees () # returns a List of Employee objects in the Employee Table
# e. getEmployee(emp_id) # returns the relevant Employee object from Employee table
# f. UpdateEmployee(employee_object) # updates an employee record in Employee tableg. DeleteEmployee(emp_id) # deleted relevant Employee record from Employee table

import sqlite3
from employee import Employee


def add_employee(conn, cursor, employee):
    try:

        employee_id = employee.get_employee_id()
        full_name = employee.get_full_name()
        email = employee.get_email()
        tel_num = employee.get_tel_num()

        query = '''INSERT INTO employee (
        employee_id, 
        full_name,
        email,
        tel_num
        ) VALUES(?,?,?,?);'''

        with conn:
            cursor.execute(query, (employee_id, full_name, email, tel_num))

        return True

    except sqlite3.Error as e:
        print(f"SQLite Error: {e}")
        return False


def add_multi_employees(conn, cursor, employees):
    # Skip first as already created
    for num in range(0, 5):
        result = add_employee(conn, cursor, employees[num])
        if result is False:
            return False
    return True


def create_db(db_name):
    try:
        # Create connection or new db to input db_name
        conn = sqlite3.connect(db_name)

        # Create cursor object
        cursor = conn.cursor()

        # return the conn and cursor objects as a tuple
        return conn, cursor

    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
        return None, None


def create_employee_objects():
    employees = []
    employee = Employee('1','Zsazsa Revie','zrevie0@nifty.com','503-623-8314')
    employees.append(employee)
    employee = Employee('2','Leicester Klagge','lklagge1@reddit.com','273-777-6728')
    employees.append(employee)
    employee = Employee('3','Nana Grigorini','ngrigorini2@chron.com','728-244-1473')
    employees.append(employee)
    employee = Employee('4','Homere Talbot','htalbot3@zimbio.com','590-548-7780')
    employees.append(employee)
    employee = Employee('5','Dorris Amps','damps4@nifty.com','727-424-5199')
    employees.append(employee)
    return employees


def create_employee_table(conn, cursor):
    try:
        query = f'''
            CREATE TABLE IF NOT EXISTS employee (
            employee_id TEXT,
            full_name TEXT,
            email TEXT,
            tel_num TEXT
            )
        '''

        with conn:
            cursor.execute(query)

        return True

    except sqlite3.Error as e:
        print(f"SQLite Error: {e}")
        return False


def get_employee(conn, cursor, employee_id, print_employee = False):
    try:
        with conn:
            query = "SELECT * FROM employee WHERE employee_id = ?"
            cursor.execute(query, (employee_id,))
            record = cursor.fetchone()

            if print_employee is True:
                print(record)

            return record

    except sqlite3.Error as e:
        print(f"SQLite Error: {e}")

def get_employees(conn, cursor, print_employees = False):
    try:
        with conn:
            query = "SELECT * FROM employee"
            cursor.execute(query)
            records = cursor.fetchall()

            if print_employees is True:
                for record in records:
                    print(record)

            return records

    except sqlite3.Error as e:
        print(f"SQLite Error: {e}")



def main():
    conn, cursor = create_db('employee.db')
    if conn is None:
        print("Error: Failed to create database connection. Terminating operation.")
        return

    table_created = create_employee_table(conn, cursor)
    if table_created is False:
        print("Error: Failed to create table. Terminating operation.")
        return

    employees = create_employee_objects()

    records_inserted = add_multi_employees(conn, cursor, employees)
    if records_inserted is False:
        print("Error: Failed to insert records. Terminating operation.")
        return

    get_employees(conn, cursor, True)

    get_employee(conn, cursor, 5, True)

main()