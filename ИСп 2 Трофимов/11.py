import sqlite3

connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()
cursor.execute('SELECT COUNT(*) FROM Users')
toral_users = cursor.fetchone()[0]
print('Общее количество пользователей:', toral_users)
connection.close()