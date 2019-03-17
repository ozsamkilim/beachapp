import sqlite3
from flask import session

DB_FILE_PATH = 'data/data.db'


class Recipes:
	def __init__(self):
		self.conn = sqlite3.connect(DB_FILE_PATH)
		self.conn.row_factory = sqlite3.Row
		self.cursor = self.conn.cursor()
		'''Set up necessary database objects that will be reused by
		other functions of this class.'''
		

	def get_recipes(self, user_id):
		self.cursor.execute('select * from recipes where user_id = ?', (user_id,))
		rows = self.cursor.fetchall()
		return rows


		
		'''Get a list of dictionaries(!) representing recipes that belong
		to the given user.'''

	def get_recipe(self, recipe_id):
		self.cursor.execute('select * from recipes where recipe_id = ? ',(recipe_id,))
		row = self.cursor.fetchone()
		return row
		
		'''Get a dictionary(!) of the data for the recapie whose ID
		matches the given ID.'''
		

	def add_recipe(self, recipe_title, recipe , image , user_id):
		query ="INSERT INTO recipes (recipe_title, recipe ,image, user_id) VALUES (?,?,?,?)"
		self.cursor.execute(query,(recipe_title, recipe, image, user_id))
		self.conn.commit()
		self.conn.close()
		# '''Add a recipe to the database. Use the given dictionary of data
		# as well as the given user ID as data for the new row.'''







	

