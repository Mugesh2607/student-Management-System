from tabulate import tabulate
import mysql.connector
conn=mysql.connector.connect(host="localhost",password="Mugesh735",user="root",database="school")

def insert(name,age,city):
    s=conn.cursor()
    sql="insert into students(name,age,city) values(%s,%s,%s)"
    details=(name,age,city)
    s.execute(sql,details)
    conn.commit()
    print("Data insert success")

def update(name,age,ciy,id):
    s=conn.cursor()
    sql="update students set name=%s,age=%s,city=%s where id=%s"
    details=(name,age,city,id)
    s.execute(sql,details)
    conn.commit()
    print("Data update success")

    

def delete(id):
    s=conn.cursor()
    sql="delete from students where id=%s"
    details=(id,)
    s.execute(sql,details)
    conn.commit()
    print("Data Delete success")
    

def select():
    s=conn.cursor()
    sql="select * from students"
    s.execute(sql)
    result=s.fetchall()
    print(tabulate(result,headers=["ID","NAME","AGE","CITY"]))

    

while True:
    print("1.Insert Data")
    print("2.Update Data")
    print("3.Delete Data")
    print("4.Select Data")
    print("5.Exit")
    choice=int(input("Enter Your Choice : "))
    if choice==1:
        name =input("Enter Name : ")
        age=int(input("Enter Age : "))
        city =input("Enter City : ")
        insert(name,age,city)
    
    elif choice==2:
        id=input("Enter ID : ")
        name =input("Enter Name : ")
        age=int(input("Enter Age : "))
        city =input("Enter City : ")
        update(name,age,city,id)
    
    elif choice==3:
        id=input("Enter ID : ")
        delete(id)


    elif choice==4:
        select()

    elif choice==5:
        quit()
    else:
        print("Invalid Selection")



