import psycopg2
import csv 

# Establish a connection to the PostgreSQL database
conn = psycopg2.connect(
    dbname="h1b_data",
    user = "pixel pulp",
    password = "45678",
    host="localhost"
)

# Create a cursor
cursor = conn.cursor()

# Open and read the CSV file and insert data into the database
with open('h1b_data_2016.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    for row in reader:
        cursor.execute(
            "INSERT INTO h1b_data_2016 (column1, column2, ...) VALUES (%s, %s, ...)",
            (row[0], row[1], ...)  # Specify values for each column
        )

# Commit the changes and close the connection
conn.commit()
conn.close()