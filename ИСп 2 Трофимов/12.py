import sqlite3

connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()
cursor.execute('SELECT SUM(age) FROM Users')
toral_age = cursor.fetchone()[0]
print('Общая сумма возрастов пользователей:', toral_age)
connection.close()