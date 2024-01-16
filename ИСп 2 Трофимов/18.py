import sqlite3

connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()
cursor.execute('''SELECT * FROM users''')
first_users = cursor.fetchall()
print(first_users)
cursor.execute('''SELECT * FROM users''')
first_five_users = cursor.fetchall(5)
print(first_five_users)
cursor.execute('''SELECT * FROM users''')
all_users = cursor.fetchall()
print(all_users)
connection.close()