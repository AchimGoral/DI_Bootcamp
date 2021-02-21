# import sqlite3 as sl
import psycopg2

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'Achim031291!'
DATABASE = 'restaurant_items'

class MenuItem:

	def __init__(self, item, price):
		self.item = item
		self.price = price
		

	def run_query(self, query):
		# connection = sl.connect("menu_database.db")
		connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
		cursor = connection.cursor()
		cursor.execute(query)
		connection.commit()
		connection.close()

	def save(self):
		try:
			query = f"INSERT INTO restaurant_items (item, price) VALUES ('{self.item}', {self.price})"
			self.run_query(query)
		except:
			return False

	def delete(self):
		query = f"DELETE FROM restaurant_items WHERE item = '{self.item}'"
		self.run_query(query)

	def update(self, old_item):
		query = f"UPDATE restaurant_items SET item = '{self.item}' WHERE item = '{old_item}'"
		self.run_query(query)
		query = f"UPDATE restaurant_items SET price = {self.price} WHERE item = '{self.item}'" 
		self.run_query(query)

	@classmethod
	def all(cls):
		query = f"SELECT item, price FROM restaurant_items"
		# connection = sl.connect("menu_database.db")
		connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
		cursor = connection.cursor()
		cursor.execute(query)
		results = cursor.fetchall()
		connection.close()
		if results:
			return results
		return "Database is empty"

	@classmethod
	def get_by_name(cls, get_item):
		query = f"SELECT item, price FROM restaurant_items WHERE item = '{get_item}'"
		# connection = sl.connect("menu_database.db")
		connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
		cursor = connection.cursor()
		cursor.execute(query)
		results = cursor.fetchall()
		connection.close()
		if results:
			return results
		return "Item not in Database"