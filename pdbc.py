import mysql.connector
connection=mysql.connector.connect(
    user="root",
    password="root@1234",
    host="localhost",
    database="prashanthdb"

)
# # print('connection is done:)')

# cur=connection.cursor()
# # data=cur.execute('create table store(p_id int, pname varchar(90), price int)')
# data=cur.execute("insert into  store values(1,'rice',980)")
# # connection.commit()
# # cur.execute("SHOW TABLES")
# # for table in cur:
# #     print(table)
# print(data)