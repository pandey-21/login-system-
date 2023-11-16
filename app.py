import shutil
import mysql.connector as m
con=m.connect(
    host='localhost',
    user='root',
    password='1234',
    database='loginfo'
)

cr=con.cursor()
a= "create table IF NOT EXISTS user_info(user_id int(6) primary key, password varchar(50) NOT NULL);"
cr.execute(a)    

def signin(userid, passwd):
    cr.execute('insert into user_info values(%s,%s)',(userid,passwd))
    print("user registered")
    con.commit()   

def verify(userid,passwd):
    cr.execute("SELECT * FROM user_info WHERE user_id=%s AND password=%s",(userid,passwd))
    return cr.fetchone() is not None

def login(userid,passwd):
    for i in range(3):
        
        if verify(userid, passwd):
            print("Jai Shri Ram 🕉️")
            break
        else:
            print("incorrect username or password. Please try again")
    else:
        print('all attempts exhausted.try after 24 hrs')   


choose=input('login OR signin----')
userid=int(input('enter your user id---'))
passwd=input('enter your password---')
if choose=='login':
    login(userid,passwd)
elif choose=='signin':
    signin(userid,passwd)

    
    

