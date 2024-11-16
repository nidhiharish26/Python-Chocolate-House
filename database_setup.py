import sqlite3

#creating connection to database

connection = sqlite3.connect('choco_house.db')
cursor = connection.cursor()

#creating tables

command1 = '''CREATE TABLE IF NOT EXISTS 
seasonal_flavours (id INTEGER PRIMARY KEY,
                   flavor_name TEXT NOT NULL,
                   available_until TEXT,
                   description TEXT)'''

command2 = '''CREATE TABLE IF NOT EXISTS 
ingredient_inventory (id INTEGER PRIMARY KEY,
                     ingredient_name TEXT NOT NULL,
                     available_until TEXT,
                     description TEXT)'''

command3 = '''CREATE TABLE IF NOT EXISTS 
customer_suggestions (id INTEGER PRIMARY KEY,
                      name TEXT,
                      email TEXT,
                      suggestion TEXT,
                      allergy_concerns TEXT)'''

cursor.execute(command1)
cursor.execute(command2)
cursor.execute(command3)


connection.commit()
connection.close()  






