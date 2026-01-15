import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '1234',
    database = 'cadd'
)

cursor = mydb.cursor()

query = "INSERT INTO courses (course_id, course_name, duration, price) VALUES (%s,%s,%s,%s)"
values = ((2,"C++",45,15000),
          (3,"Java",40,12000),
          (4,"Ruby",30,12000),
          (5,"Django",35,11000),
          (6,"Data Analytics",80,50000))
cursor.executemany(query,values)

mydb.commit()