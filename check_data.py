import sqlite3

# Connect to the database
conn = sqlite3.connect('choco_house.db')
cursor = conn.cursor()

# Fetch all data from the seasonal_flavours table
cursor.execute("SELECT * FROM seasonal_flavours")
flavors = cursor.fetchall()

# Print the data to verify if there is any
for flavor in flavors:
    print(flavor)

conn.close()
