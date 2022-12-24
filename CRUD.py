from tabulate import tabulate
import mysql.connector

con = mysql.connector.connect(host="localhost", user="root", password="root", database="python_db")


def insert(name, age, city):
    res = con.cursor()
    sql = "insert into users (name,age,city) values (%s,%s,%s)"
    user = (name, age, city)
    res.execute(sql, user)
    con.commit()
    print("Data Insert Success")


def update(name, age, city,id):
    res = con.cursor()
    sql = "update users set name=%s,age=%s,city=%s where id=%s"
    user = (name, age, city,id)
    res.execute(sql, user)
    con.commit()
    print("Data Update Success")



def select():
    res = con.cursor()
    sql = "SELECT ID,NAME,AGE,CITY from users"
    res.execute(sql)
    # result=res.fetchone()
    # result=res.fetchmany(2)
    result = res.fetchall()
    print(tabulate(result, headers=["ID", "NAME", "AGE", "CITY"]))


def delete(id):
    res = con.cursor()
    sql = "delete from users where id=%s"
    user = (id,)
    res.execute(sql, user)
    con.commit()
    print("Data Delete Success")



while True:
    print("1.Insert Data")
    print("2.Update Data")
    print("3.Select Data")
    print("4.Delete Data")
    print("5.Exit")
    choice = int(input("Enter Your Choice : "))
    if choice == 1:
        name = input("Enter Name : ")
        age = input("Enter Age : ")
        city = input("Enter City : ")
        insert(name, age, city)
    elif choice == 2:
        id = input("Enter The Id : ")
        name = input("Enter Name : ")
        age = input("Enter Age : ")
        city = input("Enter City : ")
        update(name, age, city,id)
    elif choice == 3:
        select()
    elif choice == 4:
        id = input("Enter The Id to Delete : ")
        delete(id)
    elif choice == 5:
        quit()
    else:
        print("Invalid Selection . Please Try Again !")
