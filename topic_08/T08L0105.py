import sqlite3

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()
print("\nCreated database in memory")

query = "CREATE TABLE IF NOT EXISTS person (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT);"
cursor.execute(query)
conn.commit()
print("\nCreated person table")

print("\nInserting records to person table")
query = "INSERT INTO person (name) VALUES('Jacinda'),('Alandra'),('Jeffrey');"
cursor.execute(query)
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
