import sqlite3

connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()
cursor.execute('''SELECT * from users''')
users = cursor.fetchall()
for user in users:
    print(user)
connection.close()