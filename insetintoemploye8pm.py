import pymysql
mydb = pymysql.connect(host="localhost",port=3306,user="root",passwd="",database="2pmquizapp")
mycursor = mydb.cursor()
def callAdmin():
    while True:
        print("1. Add Student")
        print("2. Add Technology")   
        print("3. Add Questions")
        print("4. Logout")

        ch = int(input("Enter choice: "))

        if ch == 1:
            un = input("Enter UserName: ")
            pwd = input("Enter Password: ")
            nm = input("Enter Name: ")
            em = input("Enter Email: ")

            mycursor.execute("insert into user_profile(username,password,name,email,role) values ('{}', '{}', '{}', '{}','student')".format(un,pwd,nm,em))
            mydb.commit()
            print("Student Added!")
            
        elif ch == 2:
            try:
                tn = input("Enter Technology Name: ")
                mycursor.execute("insert into technology(tname) values('{}')".format(tn))
                mydb.commit()
                print("Technology Added!")
            except:
                print("Technology Already Exist!")
            
        elif ch == 3:
            mycursor.execute("select * from technology")
            tech_all = mycursor.fetchall() #((), ())
            #print(tech_all)
            for i in tech_all:
                print(i[0], i[1])
            tid = int(input("Select Technology:"))

            q = input("Enter Question: (0-100)")
            a = input("Enter Option A: ")
            b = input("Enter Option B: ")
            c = input("Enter Option C: ")
            d = input("Enter Option D: ")
            correct = input("Enter Correct (A/B/C/D): ")

            mycursor.execute("insert into question(question,opta,optb,optc,optd,correct,tech_id)values('{}','{}','{}','{}','{}','{}',{})".format(q,a,b,c,d,correct,tid))
            mydb.commit()
            print("Question Added!")

            
        elif ch == 4:
            break

def callStudent():
    print("Me hu Student!")

un = input("Enter UserName: ")
pwd = input("Enter Password: ")

mycursor.execute("select * from user_profile where username='{}' and password='{}'".format(un, pwd))
udata = mycursor.fetchone()

if udata:
    print("=====Welcome {}======".format(udata[3]))
    if udata[5] == 'admin':
        callAdmin()
    elif udata[5] == "student":
        callStudent()
else:
    print("Invalid Username or Password!")