import mysql.connector

mydb = mysql.connector.connect(
    host  = 'localhost',
    user = 'root',
    password = '1234',
    database = 'cadd'
)

cursor = mydb.cursor()
# write query for inserting data into tables
query = "INSERT INTO courses(course_id, course_name, duration, price) VALUES (%s,%s,%s,%s)"
# insert the values in tuple
values = (1, "Python", 40, 1000)
# execute the query and take values
cursor.execute(query,values)

# permanent changes in database
mydb.commit()
