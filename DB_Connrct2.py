from dbconfig import *

eid = int(input("Enter ID: "))
nm = input("Enter Name: ")
sal = float(input("Enter Salary: "))

mycursor.execute("insert into employee values ({}, '{}', {})".format(eid,nm,sal))
#DML
mydb.commit()
print("Data Saved!")