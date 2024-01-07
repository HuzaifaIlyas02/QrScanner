import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('users.db')

# Create a cursor object using the cursor() method
cursor = conn.cursor()

# Select data
cursor.execute("SELECT * FROM authorized_users")

# Fetch all rows as a list of tuples
results = cursor.fetchall()

# Output the rows
for row in results:
    print(row)

# Close the connection
conn.close()
