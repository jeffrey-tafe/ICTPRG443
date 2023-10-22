import sqlite3

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()
print("\nCreated database in memory")

query = "CREATE TABLE IF NOT EXISTS person (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT);"
cursor.execute(query)
conn.commit()
print("\nCreated person table")

query = "CREATE TABLE IF NOT EXISTS item (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, type TEXT);"
cursor.execute(query)
conn.commit()
print("\nCreated item table")

print("\nRetrieving table names")
query = "SELECT name FROM sqlite_master WHERE type='table';"
cursor.execute(query)
result = cursor.fetchall()

for table in result:
    print(table[0])

cursor.close()
conn.close()
