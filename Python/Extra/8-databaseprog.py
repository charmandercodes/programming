import sqlite3

# Establishing the connection to the SQLite database. If the file 'mydata.db' doesn't exist, 
# it will be created. The connection object represents the database itself.
connection = sqlite3.connect('mydata.db')

# Creating a cursor object to execute SQL commands. The cursor is used to interact with the database.
cursor = connection.cursor()

# Creating a table 'persons' if it doesn't exist already. This table has four columns:
cursor.execute("""
CREATE TABLE IF NOT EXISTS persons (
    id INTEGER PRIMARY KEY,
    first_name TEXT, 
    last_name TEXT, 
    age INTEGER
)
""")

# Inserting data into the 'persons' table. We use "INSERT OR IGNORE" to avoid inserting duplicates 
# if the same person with the same ID is already present.
cursor.execute("""
INSERT OR IGNORE INTO persons VALUES
(1, 'Paul', 'Smith', 24),
(2, 'Mark', 'Johnson', 42),
(3, 'Anna', 'Smith', 34)
""")

# Selecting all rows where the last name is 'Smith'. This query retrieves persons whose last name is 'Smith'.
cursor.execute("""
SELECT * FROM persons 
WHERE last_name = 'Smith'
""")

# Fetching all the matching rows from the above query and printing the result. 
# Each row is represented as a tuple (id, first_name, last_name, age).
rows = cursor.fetchall()
print(rows)  # Output example: [(1, 'Paul', 'Smith', 24), (3, 'Anna', 'Smith', 34)]

# Defining a Person class to represent a person and to interact with the 'persons' table in the database.
class Person:
    # The constructor (__init__ method) initializes a Person object.
    # It takes a database connection object, and optional id_number, first, last, and age parameters.
    # The constructor also creates a cursor specific to this Person instance, to run SQL queries.
    def __init__(self, connection, id_number=-1, first='', last='', age=-1):
        self.id_number = id_number  # Person's ID number
        self.first = first  # First name
        self.last = last  # Last name
        self.age = age  # Age
        self.connection = connection  # Using the passed-in database connection
        self.cursor = self.connection.cursor()  # Creating a cursor tied to this connection

    # This method is responsible for loading a person's data from the database based on their ID.
    def load_person(self, id_number):
        # Running a SELECT query to fetch the row for the given id_number.
        self.cursor.execute(f"""
        SELECT * FROM persons 
        WHERE id = {id_number}
        """)
        
        # Fetching the first matching row from the query result.
        results = self.cursor.fetchone()

        # If a result is found, update the object's attributes with the corresponding values.
        if results:
            self.id_number = id_number
            self.first = results[1]  # First name is at index 1
            self.last = results[2]  # Last name is at index 2
            self.age = results[3]  # Age is at index 3
        else:
            # If no result is found, print a message indicating the person was not found.
            print(f"Person with ID {id_number} not found.")
    def insert_person(self):
        self.cursor.execute(f"""
                        INSERT INTO persons VALUES
                        ({self.id_number}, '{self.first}', '{self.last}', {self.age})
                        """)
        self.connection.commit()


# Testing the Person class
# Creating a Person object and passing the existing connection to ensure it uses the same connection as above.
p1 = Person(connection)

# Loading the person with ID 1 from the database.
p1.load_person(1)

# Printing out the loaded person's details.
print(p1.first)  # Expected output: 'Paul'
print(p1.last)   # Expected output: 'Smith'
print(p1.age)    # Expected output: 24
print(p1.id_number)  # Expected output: 1

# Committing any changes made to the database and closing the connection. 
# It's a good practice to commit after making changes and always close the connection when done.


# INSERTING OBJECTS

# Correct way to create p2 with connection
p2 = Person(connection, 7, "Alex", "Robbins", 30)  # connection object comes first

# Now insert the person into the database using the insert_person method
p2.insert_person()


cursor.execute('SELECT * FROM persons')
results = cursor.fetchall()
print(results)

connection.commit()
connection.close()
