import mysql.connector
conn=mysql.connector.connect(
    user="root",
    password='root@1234',
    host='localhost',
    database='gajula'
)
cur=conn.cursor()
# cur.execute("select * from employee")
# a=cur.fetchmany(2)
# for i in range(5):
#     print(cur.fetchone())
# cur.execute("select * from employee where id=3")
# print(cur.fetchall())
# cur.execute("select * from employee where id=%s",(2,))
# print(cur.fetchall())

# cur.execute("select * from employee where ename=%s",["Anil"])
# print(cur.fetchall())
# name=input('enter the name: ')
# cur=conn.cursor(dictionary=True)
# cur.execute('select * from employee where ename=%s',(name,))
# print(cur.fetchall())

import mysql.connector

conn = mysql.connector.connect(
    user="root",
    password="root@1234",
    host="localhost",
    database="gajula"
)

cur = conn.cursor(dictionary=True)

# cur.execute("""
# CREATE TABLE employee (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     ename VARCHAR(50) NOT NULL,
#     age INT,
#     salary DECIMAL(10,2),
#     dept VARCHAR(30)
# )
# """)

# conn.commit()
# print("Table created successfully")
# data = [
#     ("nandini", 38, 92000.00, "CFO"),
#     ("Anjali", 32, 55001.00, "DA")

# ]
# cur.executemany("insert into employee  (ename, age, salary, dept) values(%s, %s, %s, %s)", data)
# conn.commit()

# cur.execute("select* from employee")
# print(cur.fetchall())
# print(conn.is_connected())
conn.close()
print(conn.is_connected())

