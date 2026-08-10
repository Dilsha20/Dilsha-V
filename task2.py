import sqlite3
conn = sqlite3.connect("demo.db")
# connects to a db [creates a dby if db does not exists]
cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS Tasks(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(20),
        des TEXT
        )
    ''')

conn.close()


def addtasks():
    conn=sqlite3.connect("demo.db")
    cursor=conn.cursor()
    name=input('enter taskname: -')
    des=input("enter task description: ")
    cursor.execute('''
    INSERT INTO Tasks (name,des)
      VALUES(?,?)
    ''', (name, des))
    print("TAsk added ")
    conn.commit()
    conn.close()

def viewtask():
    conn = sqlite3.connect("demo.db")
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM Tasks
    ''')
    tasks=cursor.fetchall() #retreives list of data from the last executes querry
    print("TASKS found")
    if i in tasks:
        print(f"task{i[0]}-{i[1]}")


def search_task():
    conn = sqlite3.connect("demo.db")
    cursor = conn.cursor()
    task_id= int(input("enter task id :-"))
    cursor.execute('''
        SELECT * FROM Tasks WHERE id = ?
    ''',(task_id,))
    task = cursor.fetchone()
    if task:
        print("task found")
        print(f"task{task[0]}-{task[1]}")
    else:
        print("no such task")    

def update_tasks():
    conn = sqlite3.connect("demo.db")
    cursor = conn.cursor()
    td = int(input("enter task id : -"))
    tname = input("eneter task name : -")
    tdes = input("enter task des : ")
    cursor.execute('''
         UPDATE Tasks SET name = ?, des = ? WHERE id = ?
         ''',(tname,tdes,td))
    conn.commit()
    print("task updated")

def delete_tasks():
    conn = sqlite3.connect("demo.db")
    cursor = conn.cursor()
    tid = int(input("enter task id : -"))
    ch = input("Are you aure you want to delete this tasks Y/N \n:-").lower()
    if ch == "y":
        cursor.execute('''
            DELETE FROM Tasks WHERE id = ?
        ''',(tid,))
        conn.commit()
    else:
        print("task not deleted !!!!!!!!!!!!!!!")


def main():
    while True:
        print("welcome to task management ")
        ch = int(input("1.add task\n2.view task\n3.search tasks\n4.update tasks\n5.delete tasks\n6.exit"))
        if ch == 1:
            addtasks()
        elif ch == 2:
            viewtask()   
        elif ch == 3:
            search_task() 
        elif ch==4:
            update_tasks() 
        elif ch==5:
            delete_tasks()       
        else:
            print("invalid input")
main()
