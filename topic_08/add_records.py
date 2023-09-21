import sqlite3

conn = sqlite3.connect('acme.db')

cursor = conn.cursor()

first_name = "Joe"
last_name = "Bloggs"
email = "joe.bloggs@tafesa.edu.au"

# Insert record to table
query = "INSERT INTO student (first_name, last_name, email) VALUES(?,?,?)"
cursor.execute(query, (first_name, last_name, email))
conn.commit()

# Get records from table and print
query = "SELECT * FROM student"
result = cursor.execute(query)
for row in result:
    print("ID: ", row[0])
    print("First Name: ", row[1])
    print("Last Name: ", row[2])
    print("Email: ", row[3])

# Drop all records from table
query = "DELETE FROM student"
cursor.execute(query)
conn.commit()

# Insert a record using a dictionary
record = {'first_name': 'Peta', 'last_name': 'Venturas', 'email': 'peta.venturas@tafesa.edu.au'}
query = "INSERT INTO student (first_name, last_name, email) VALUES(:first_name,:last_name,:email)"
cursor.execute(query, record)
conn.commit()

# Alternate way to get data when just one row expected
query = "SELECT * FROM student"
result = cursor.execute(query)
id, first_name, last_name, email = result.fetchone()
print(f"\n{id}, {first_name}, {last_name}, {email}")

# Drop all records from table
query = "DELETE FROM student"
cursor.execute(query)
conn.commit()

# Insert data with a list
data = [("Joey", "Bloggsy", "joey.blogsey@tafesa.edu.au"),
        ("Jeffrey", "Smith", "jeffrey.smith@tafesa.edu.au"),
        ("Alex", "Great", "alex.great@tafesa.edu.au")
        ]

query = "INSERT INTO student (first_name, last_name, email) VALUES(?,?,?)"
cursor.executemany(query, data)
conn.commit()

# Get new data
query = "SELECT * FROM student"
result = cursor.execute(query)
result2 = result.fetchmany(2)
for row in result2:
    print("\nID: ", row[0])
    print("First Name: ", row[1])
    print("Last Name: ", row[2])
    print("Email: ", row[3])

cursor.close()
conn.close()
