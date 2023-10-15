import sqlite3

conn = sqlite3.connect(":memory:")

print("\nCreated database in memory")

cursor = conn.cursor()

query = "CREATE TABLE IF NOT EXISTS person (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)"

cursor.execute(query)

conn.commit()

print("\nCreated person table")

query = "PRAGMA table_info(person)"

cursor.execute(query)

result = cursor.fetchone()

print(result)

cursor.close()
conn.close()