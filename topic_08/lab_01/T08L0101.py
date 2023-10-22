import sqlite3

conn = sqlite3.connect('t08l0101.db')

cursor = conn.cursor()

query = 'select sqlite_version()'

cursor.execute(query)

record = cursor.fetchone()

print('SQL Version: ', record[0])

conn.close()

