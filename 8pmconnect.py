import pymysql
pymysql.connect(host="localhost", port=3306, user="root", passwd="", database="8pm_sample")
mycursor = mydb.cursor()
mycursor.execute("insert into employe value(115, 'rahul', 25000)")
mudb.commit()
print("Data inserted")