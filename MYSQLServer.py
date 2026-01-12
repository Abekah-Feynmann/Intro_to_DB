import mysql.connector
from mysql.connector import Error
try:
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "filifeynmann5966B$%^",
    )

    if mydb.is_connected:
        print("Connected to MYSQL server")

    mycursor = mydb.cursor()

    #Create a table called alx_book_store if doesn't exist
    mycursor.execute("""
    CREATE DATABASE IF NOT EXISTS alx_book_store;
    """)

    print("Database 'alx_book_store' created successfully!")

except Error as e:
    print("Failing to connect to MYSQL:", e)

else:
    mycursor.close()
    mydb.close()
    print("Database connection closed.")
