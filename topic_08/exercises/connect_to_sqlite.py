import sqlite3

conn = sqlite3.connect('acme.db')

cursor = conn.cursor()

query = 'CREATE TABLE IF NOT EXISTS student (id INTEGER PRIMARY KEY AUTOINCREMENT, first_name TEXT, last_name TEXT, email TEXT)'

cursor.execute(query)

conn.commit()

cursor.execute('SELECT name FROM sqlite_master WHERE type = "table"')
rows = cursor.fetchall()
for row in rows:
    print(row[0])

cursor.execute('PRAGMA table_info(student)')  # Can't use DESC student in sqlite
result = cursor.fetchall()
print(result)
for row in result:
    print(row)

cursor.close()
conn.close()