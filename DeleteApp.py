from dbconfig import *
empid = int(input("Enter ID: "))
mycursor.execute("delete from employee where eid=()".format(empid))
mydb.commit()
print("Record Deleted!")
