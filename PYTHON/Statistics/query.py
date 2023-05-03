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
mycursor.execute("select * from TEST1.test_table")
for i in mycursor.fetchall():
    print(i)