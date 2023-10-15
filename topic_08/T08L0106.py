import sqlite3

# Create database in memory
conn = sqlite3.connect(":memory:")
cursor = conn.cursor()
print("\nCreated database in memory")

# Create person table
query = "CREATE TABLE IF NOT EXISTS person (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age INTEGER);"
cursor.execute(query)
conn.commit()
print("\nCreated person table")

# Declare list of people in tuples
people_list = [
    ('Jacinda', 33),
    ('Jeffrey', 37),
    ('Alandra', 2)
]

# Insert people into table
print("\nInserting records to person table")
query = "INSERT INTO person (name, age) VALUES(?,?);"
cursor.executemany(query, people_list)
conn.commit()

print("\nRetrieving column names")
query = f"PRAGMA table_info(person);"
cursor.execute(query)
columns = [row[1] for row in cursor.fetchall()]

print("\nRetrieving records from person table")
query = "SELECT * FROM person;"
cursor.execute(query)
records = cursor.fetchall()

# Print column headers
header = "\t".join(columns)
print(header)

# Print records with tabs separating values
for record in records:
    record_line = "\t".join(str(value) for value in record)
    print(record_line)

cursor.close()
conn.close()
