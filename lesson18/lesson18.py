import mysql.connector


# 1
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password")
curs = db.cursor()
curs.execute("CREATE  DATABASE IF NOT EXISTS My_first_db")
db.commit()
db.close()
# 2
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database='My_first_db')
curs = db.cursor()
curs.execute("CREATE TABLE Student (id INT, name VARCHAR(255))")
# 3
curs.execute("CREATE TABLE Employee (id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(255), salary INT(6))")
# 4
curs.execute("ALTER TABLE Student MODIFY COLUMN id INT PRIMARY KEY")
db.commit()
# 5
val = ("01", "John")
sql = "INSERT INTO student (id, name) VALUES (%s, %s)"
curs.execute(sql, val)
val = ("01", "John", "10000")
sql = "INSERT INTO employee (id, name, salary) VALUES (%s, %s, %s)"
curs.execute(sql, val)
db.commit()
db.close()
