import pymysql
mydb = pymysql.connect(host="localhost",port=3306,user="root",passwd="",database="8pm_sample")
mycursor = mydb.cursor()
mycursor.execute("select * from employe ")
row = mycursor.fetchone() 
print(row)
for i in row:
    print(i)
