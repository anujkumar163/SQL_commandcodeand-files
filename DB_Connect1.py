import mysql.connector
mydb = mysql.connector.connect(host="localhost",port=3306,user="root",passwd="",database="8pm_sample")
#print(mydb)
mycursor = mydb.cursor()
mycursor.execute("select * from employe")
for i in mycursor:
    print(i)