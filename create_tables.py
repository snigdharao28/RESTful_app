import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

#	to auto-increment 'id', we use INTEGER PRIMARY KEY unlike 'id int' done previously.
create_table_user = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table_user)

create_table_item = "CREATE TABLE IF NOT EXISTS items (name text PRIMARY KEY, price real)"
cursor.execute(create_table_item)


connection.commit()

connection.close()