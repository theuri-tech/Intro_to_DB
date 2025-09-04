import mysql.connector
# from mysql.connector import Error 

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="theuri",
        password="1Mula",
        database="alx_book_store"
    )
    if mydb.is_connected():
        cursor = mydb.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")
    
except mysql.connector.Error as err:
    print(f"Failed to connect to MySQL server: {err}")

finally:
    try:
        if cursor:
            cursor.close()
        if mydb:
            mydb.close()
    except NameError:
        pass #cursor or mydb wan't created

