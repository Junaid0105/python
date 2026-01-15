import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '1234',
    database = 'cadd'
)

cursor = mydb.cursor()

cursor.execute("SELECT * FROM COURSES")

result = cursor.fetchall()
for i in result:
    print(i)