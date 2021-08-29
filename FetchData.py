from dbconfig import *
mycursor.execute("select * from employe ")
row = mycursor.fetchone() 
print(row)
for i in row:
    print(i)
