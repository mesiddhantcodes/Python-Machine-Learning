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
mycursor.execute("insert into TEST1.test_table values(1234,23.34,'Hi..')")
mycursor.execute("insert into TEST1.test_table values(1234,23.34,'Hi..')")
mycursor.execute("insert into TEST1.test_table values(1234,23.34,'Hi..')")
mycursor.execute("insert into TEST1.test_table values(1234,23.34,'Hi..')")
mycursor.execute("insert into TEST1.test_table values(1234,23.34,'Hi..')")
mycursor.execute("insert into TEST1.test_table values(1234,23.34,'Hi..')")
mycursor.execute("insert into TEST1.test_table values(1234,23.34,'Hi..')")
mycursor.execute("insert into TEST1.test_table values(1234,23.34,'Hi..')")
mycursor.execute("insert into TEST1.test_table values(1234,23.34,'Hi..')")
mycursor.execute("insert into TEST1.test_table values(1234,23.34,'Hi..')")
mycursor.execute("insert into TEST1.test_table values(1234,23.34,'Hi..')")
mycursor.execute("insert into TEST1.test_table values(1234,23.34,'Hi..')")
mycursor.execute("insert into TEST1.test_table values(1234,23.34,'Hi..')")

mydb.commit()

mydb.close()