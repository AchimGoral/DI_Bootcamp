# import psycopg2

# HOSTNAME = 'localhost'
# USERNAME = 'postgres'
# PASSWORD = 'Achim031291!'
# DATABASE = 'Hollywood'

# connection = psycopg2.connect( host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE )

# cursor = connection.cursor()

# # query = "INSERT INTO actors (first_name, last_name, age, number_oscars) VALUES ('Brad', 'Pitt', 60, 4)"

# query = "SELECT * FROM actors"

# cursor.execute(query)

# # connection.commit()

# results = cursor.fetchall()

# connection.close()

# for item in results:
#         print(item)


# import sqlite3 as sl

# def update(data):
# 	cursor = connection.cursor()
# 	query = f"SELECT amount FROM fruits WHERE fruit = '{data}'"
# 	cursor.execute(query)
# 	# fetching the results
# 	results = cursor.fetchall()
# 	quantity = results[0][0] + 1
# 	query = f"UPDATE fruits SET amount = {quantity} WHERE fruit = '{data}'"
# 	cursor.execute(query)
# 	connection.commit()

# def add(data):
# 	try:
# 		cursor = connection.cursor()
# 		query = f"INSERT INTO fruits (fruit, amount) VALUES ('{data}', 1)"
# 		cursor.execute(query)
# 		connection.commit()
# 	except:
# 		update(data)
# 	print("Saved!")

# def connect():
# 	return sl.connect('test.db')

# def disconnect():
# 	connection.close()

# connection = connect()

# while True:
# 	fruit = input("Enter a fruit: ")
# 	if fruit == 'quit':
# 		break	
# 	add(fruit)

# print('bye')
# disconnect()


import sqlite3 as sl
from faker import Faker
from time import time
f = Faker()

connection = sl.connect('test.db')

cursor = connection.cursor()

start = time()
for i in range(10000):
	query = f"INSERT INTO people (name, email) VALUES ('{f.name()}', '{f.email()}')"
	cursor.execute(query)

connection.commit()
connection.close()
end = time()

print(f"Time to execute: {end-start}")