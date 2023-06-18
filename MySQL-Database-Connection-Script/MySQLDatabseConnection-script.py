import mysql.connector
from getpass import getpass

# Enter the AWS-RDS MySQL database details

hostname = input("Enter the hostname: ")
username = input("Enter the username: ")
password = getpass("Enter the password: ")
database = input("Enter the database name: ")

# Connect to the MySQL database

connection = mysql.connector.connect(
    host = hostname,
    user = username,
    password = password,
    database = database
)
print ("Connected to the database!")

# Create a cursor object
cursor = connection.cursor()

# Select all rows from the 'users' table
query = "SELECT * FROM users"
cursor.execute(query)

# Fetch all rows and print the results
for row in cursor.fetchall():
    print(row)

# Close the cursor and connection
cursor.close()
connection.close()