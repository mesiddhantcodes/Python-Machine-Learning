import mysql.connector
# import mysql.connector
#create user 'user'@'%' identified by 'password'
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="2002"
)
print(mydb)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE if not exists test")
mycursor.execute("create table if not exists test.test_table (c1 int, c2 float , c3 varchar(30))")
mydb.close()