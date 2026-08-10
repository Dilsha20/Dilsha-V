import sqlite3
conn=sqlite3.connect("first.db") #establishind connection
cursor=conn.cursor() #to interact with the database

#operstions
cursor.execute(
    '''

    CREATE TABLE IF NOT EXISTS Student(
        name VARCHAR(20),
        age INTEGER,
        address TEXT
        )
    '''


)

def addstudent():
    conn=sqlite3.connect("first.db")
    cursor=conn.cursor()
    student_name=input("enter student name:--")
    student_age=input("enter student age:--")
    student_address=input("enter student address:--")
    cursor.execute('''
        INSERT INTO Student(name,age,address)
                   VALUES(?,?,?)
        ''',(student_name,student_age,student_address))
    conn.commit()
    print("student added")
conn.close()

def main():
    while True:
        print("welcom to student management")
        ch=int(input("1.ADD STUDENT\n2.VIEW STUDENT"))
        if ch==1:
           addstudent() 
        else:
           print("invalid choice")
main()             


