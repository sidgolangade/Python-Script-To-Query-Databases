# MySQL Database Connection Script
This is a Python script that demonstrates how to connect to a MySQL database using the `mysql.connector` module. The script prompts the user to enter the hostname, username, password, and database name to establish a connection.

## Prerequisites
- Python 3.x
- `mysql.connector` module
- AWS RDS Database Instance

## Setup and Usage
1. Install the required dependencies by running the command `pip install mysql-connector-python`

2. Clone the repository and navigate to the directory containing the script.

3. Open the script in a Python editor or IDE.

4. Run the script.

5. When prompted, enter the hostname, username, password, and database name to establish a connection to your MySQL database.

6. The script will print a message indicating that it is connected to the database.

7. It will then execute a query to select all rows from the 'users' table.

8. The fetched rows will be printed as the results.

9. Finally, the script will close the cursor and the database connection.

## Note
- Make sure you have the correct credentials and access rights to connect to the specified MySQL database.