import sqlite3
conn = sqlite3.connect('my_new_db.db')
cursor = conn.cursor()
cursor.execute('SELECT * FROM test')
result = cursor.fetchall()
print(result)