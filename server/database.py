import os.path, logging
import settings
import psycopg2
from psycopg2 import Error

try:
    # Connect to an existing database
    connection = psycopg2.connect(user="postgres",
                                password="postgres",
                                host="localhost",
                                port="5432",
                                    database="postgres")
    # Connecting to the database file
        
    c = connection.cursor()
        
    # Creating a new SQLite table, sqlite does not have DATE types
    logging.info('Creating tables if not exists')
    c.execute('CREATE TABLE IF NOT EXISTS user_test (username TEXT PRIMARY KEY, date_of_birth TEXT NOT NULL)')
    connection.commit()

    print("Table created successfully in PostgreSQL ")

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if connection:
       c.close()
       connection.close()
       print("PostgreSQL connection is closed")  
