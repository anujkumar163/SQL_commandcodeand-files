import pyodbc
conn = pyodbc.connect(connstr)
cursor = conn.cursor()

sql = "SELECT top 100 * FROM [dbo].[8pm_sample]"
cursor.execute(sql)
data = cursor.fetchall()

#Query1
for row in data :
    print (row[1])

#Query2
print (data)

#Query3
data