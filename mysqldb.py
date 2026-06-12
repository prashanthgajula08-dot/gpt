import mysql.connector

# Database connection
connection=mysql.connector.connect(
    user="root",
    password="*****",
    host='localhost',
    database="gajula"

)
laddu=connection.cursor()

# Create table safely
data=laddu.execute("create  table employee(id int primary key, ename varchar(90),salart int) ")

# Insert data using parameterized query
data=laddu.execute('insert into employee values  (1, "Prashanth", 50000),(2, "Ravi", 45000),(3, "Sneha", 60000),(4, "Anil", 55000),(5, "Meena", 48000)')
connection.commit()
data=laddu.execute('select* from employee')
data=laddu.fetchall()
for i in data:
    print(i[1])
print(data)
laddu.execute('select * from employee where ename="prashanth" and id=1')
a=laddu.fetchone()
print(a)
laddu.execute('select * from employee where ename="prashanth" and id=0 or "1"="1"')
a=laddu.fetchone()
print(a)
ename=input('enter the name: ')
id=int(input('enter the id: '))
laddu.execute('select * from employee where id=%s and  ename=%s',[id,ename])
a=laddu.fetchall()
print(a)
