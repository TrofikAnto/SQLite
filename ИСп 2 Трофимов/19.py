import sqlite3

connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()
cursor.execute('''SELECT * from users''')
users = cursor.fetchall()
users_list = []
for user in users:
    users_dict = {
        'id': user[0],
        'username': user[1],
        'email': user[2],
        'age': user[3]
    }
users_list.append(users_dict)
for user in users_list:
    print(user)
connection.close()