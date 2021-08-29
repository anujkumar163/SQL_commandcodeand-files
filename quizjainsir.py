import pymysql
mydb = pymysql.connect(host="localhost",port=3306,user="root",passwd="",database="2pmquizapp")
mycursor = mydb.cursor()


def getTechId():
    mycursor.execute("select * from technology")
    tech_all = mycursor.fetchall() #((), ())
    #print(tech_all)
    for i in tech_all:
        print(i[0], i[1])
    tid = int(input("Select Technology:"))
    return tid


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
            
            tid = getTechId()
            
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

def callStudent(user_id):
    while True:
        print("1. Start test")
        print("2. Results")
        print("3. Logout")

        ch = int(input("Enter choice: "))
        if ch == 1:
            tid = getTechId()

            mycursor.execute("select * from question where tech_id={}".format(tid))
            all_ques = mycursor.fetchall()
            j = 1
            count = 0
            for i in all_ques:
                print(j, i[1])
                print("A.", i[2])
                print("B.", i[3])
                print("C.", i[4])
                print("D.", i[5])

                ans = input("Enter Ans: ")
                if ans == i[6]:
                    count = count + 1
                j = j + 1

            print("Result: ", count, "/", len(all_ques))
            per = (count/len(all_ques))*100
            #status, tid, user_id, date
            #Task 1

        elif ch == 2:
            q1 = """
            select * from technology
            """
            def read_query(q1): 
                cursor = connection.cursor()
                result = None
                rows = cursor.fetchall()
                result_list = [row for row in rows]
                print(result_list)
                

                try:
                    cursor.execute(q1)
                    result = cursor.fetchall()
                    return result
                except:
                    print("Error")    
                



        elif ch == 3:
            break

'''import time
t = time.localtime()
current_time = now.strftime("%H:%M:%S", t)
print(current_time)'''           

un = input("Enter UserName: ")
pwd = input("Enter Password: ")

mycursor.execute("select * from user_profile where username='{}' and password='{}'".format(un, pwd))
udata = mycursor.fetchone()

if udata:
    print("=====Welcome {}======".format(udata[3]))
    if udata[5] == 'admin':
        callAdmin()
    elif udata[5] == "student":
        callStudent(udata[0])
else:
    print("Invalid Username or Password!")
