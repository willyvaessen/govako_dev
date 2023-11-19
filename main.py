import os

import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv

load_dotenv()

mydb_govako = mysql.connector.connect(
    host="pi4B1",
    database=os.getenv('DB_NAME'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_USER_PWD')
)


def test_connection():
    try:
        conn = mydb_govako

        if conn.is_connected():
            db_info = conn.get_server_info()
            print("Connected to MySQL Sever version ", db_info)
            cursor = conn.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)

    except Error as e:
        print("Error while connecting to MySQL", e)

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("MySQL connection is closed")


test_connection()


#
# # cursor = mydb_root.cursor()
#
# databases = 'SHOW DATABASES'
# cursor.execute(databases)
# for (databases) in cursor:
#     print(f"Database found: {databases[0]}")
#
#
# # print("Root DB" + str(mydb_root))
# print("GoVaKo DB" + str(mydb_govako))
