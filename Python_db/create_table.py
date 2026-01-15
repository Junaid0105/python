#importing mysql connectors
import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '1234',
    database = 'cadd'
)

cursor = mydb.cursor()
table = "CREATE TABLE  courses (course_id integer(5), course_name varchar(20), duration integer(5), price float(5,2))"
cursor.execute(table)