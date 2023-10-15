import psycopg2
import csv

# PostgreSQL database configuration
conn = psycopg2.connect(host='localhost', dbname='postgres',user='post', password='asd123qwe', port=5432)


# Define a function to insert data from a CSV file into the database
def insert_data_from_csv(file_path, table_name):
    try:
        # Connect to the PostgreSQL database
        cursor = conn.cursor()

        # Open the CSV file and read its contents
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row if present

            for row in reader:
                # Assuming the CSV columns match the table columns
                # Adjust the INSERT statement as needed
                insert_query = f"INSERT INTO {table_name} VALUES (%s, %s, %s)"  # Modify to match your table schema
                cursor.execute(insert_query, tuple(row))

        # Commit the changes and close the connection
        conn.commit()
        conn.close()
        print(f"Data from {file_path} inserted into {table_name} successfully.")

    except (Exception, psycopg2.Error) as error:
        print(f"Error inserting data: {error}")

if __name__ == "__main__":
    # Replace these with your file and table information
    csv_file_path = "/Users/survagyabali/Desktop/H-1B_Disclosure_Data_FY16.csv"
    table_name = "Y1"

    insert_data_from_csv(csv_file_path, table_name)