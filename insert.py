import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('users.db')

# Create a cursor object using the cursor() method
cursor = conn.cursor()

# Insert data
try:
    # Example data
    qr_data_list = [
        ('QRCodeData1',),
        ('QRCodeData2',),
        # add as many QR data entries as you need
    ]

    # Insert multiple records using the more secure "?" placeholder
    cursor.executemany('INSERT INTO authorized_users (qr_data) VALUES (?)', qr_data_list)

    # Commit your changes in the database
    conn.commit()
    print("Data inserted successfully.")
except sqlite3.IntegrityError:
    print("Data already exists in the database.")
except sqlite3.Error as e:
    print("An error occurred:", e)

# Close the connection
conn.close()
