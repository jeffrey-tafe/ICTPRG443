# 1. Create a SQLite database called login.db .
# 2. Create a table called TProfiles with the following fields:
#     a. user_name (text)
#     b. Password (text)
# 3. Add a few records to this table
# 4. Use this table to validate the login values entered by the user using the above Login UI
# 5. How would you handle invalid login credentials?

import sqlite3
import re


def create_db_connection(db_name):
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


def create_table(conn, cursor):
    try:
        query = f'''
            CREATE TABLE IF NOT EXISTS TProfiles (
            user_name TEXT,
            password TEXT
            )
        '''

        with conn:
            cursor.execute(query)

        return True

    except sqlite3.Error as e:
        print(f"SQLite Error: {e}")
        return False


def insert_records(conn, cursor):
    try:

        user_records = [
            ("user1", "password1"),
            ("user2", "password2"),
            ("user3", "password3"),
            ("user4", "password4"),
            ("user5", "password5")
        ]

        query = 'INSERT INTO TProfiles (user_name, password) VALUES(?,?);'

        with conn:
            cursor.executemany(query, user_records)

        return True

    except sqlite3.Error as e:
        print(f"SQLite Error: {e}")
        return False


def is_valid_password(conn, cursor, username, password):
    if len(password) < 3:
        return False # Password is too short

    query = "SELECT password FROM TProfiles WHERE user_name = ?"

    try:
        with conn:
            cursor.execute(query, (username,))
            result = cursor.fetchone()
            return result is not None and result[0] == password

    except sqlite3.Error as e:
        print(f"SQLite Error: {e}")
        return False


def is_valid_username(conn, cursor, username):
    if len(username) < 3:
        return False  # Username is too short

    query = "SELECT user_name FROM TProfiles WHERE user_name = ?"

    try:
        with conn:
            cursor.execute(query, (username,))
            result = cursor.fetchone()
            return result is not None
    except sqlite3.Error as e:
        print(f"SQLite Error: {e}")
        return False


def prompt_password(conn, cursor, username):
    for _ in range(3):
        password = input("Password: ")
        if is_valid_password(conn, cursor, username, password):
            return True
        else:
            print("Invalid password. Please try again.")
    return False


def prompt_username(conn, cursor):

    for _ in range(3):
        username = input("Username: ")
        if is_valid_username(conn, cursor, username):
            return username
        else:
            print("Invalid username. Please try again.")
    return None





def main_create_db():
    conn, cursor = create_db_connection('test.db')
    if conn is None:
        print("Error: Failed to create database connection. Terminating operation.")
        return

    table_created = create_table(conn, cursor)
    if table_created is False:
        print("Error: Failed to create table. Terminating operation.")
        return

    records_inserted = insert_records(conn, cursor)
    if records_inserted is False:
        print("Error: Failed to insert records. Terminating operation.")
        return


def main_login():
    conn, cursor = create_db_connection('test.db')
    if conn is None:
        print("Error: Failed to create database connection. Terminating operation.")
        return

    username = prompt_username(conn, cursor)
    if username is None:
        print("Login failed too many times. Terminating operation.")
        return

    authenticated = prompt_password(conn, cursor, username)
    if authenticated is False:
        print("Login failed too many times. Terminating operation.")
        return
    else:
        print("Login successful. Welcome :)")

main_login()