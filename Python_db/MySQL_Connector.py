import mysql.connector
mydb = mysql.connector.connect(host = "localhost", user = "root",password='1234')
print(mydb.connection_id)

# create cursor
cursor = mydb.cursor()

cursor.execute("CREATE DATABASE cadd")