import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='biodataes',
                                         user='root',
                                         password='')
    mySql_insert_query = """( Name, id, ph,adders,b-group) 
                           VALUES 
                           ('rithvik',' 1709', '2020200021','2699,frwf','a1b') """

    cursor = connection.cursor()
    cursor.execute(mySql_insert_query)
    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into table")
    cursor.close()

except mysql.connector.Error as error:
    print("Failed to insert record into table {}".format(error))

finally:
    if (connection.is_connected()):
        connection.close()
        print("MySQL connection is closed")

