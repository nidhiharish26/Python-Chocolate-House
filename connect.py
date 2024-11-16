import sqlite3

# Connect to SQLite database
connection = sqlite3.connect('choco_house.db')
cursor = connection.cursor()

# Insert some test data into the table
cursor.execute('''INSERT INTO seasonal_flavours (flavor_name, available_until, description)
                  VALUES ('Chocolate Mint', '2024-12-31', 'A refreshing blend of chocolate and mint'),
                         ('Vanilla Bean', '2024-11-30', 'Smooth and creamy vanilla with a natural bean flavor')''')

# Commit changes to the database
connection.commit()

# Query to get all records from the seasonal_flavours table
cursor.execute("SELECT * FROM seasonal_flavours")
flavors = cursor.fetchall()

# Print out the results
for flavor in flavors:
    print(flavor)

connection.close()

