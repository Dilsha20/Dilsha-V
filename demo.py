import sqlite3

conn = sqlite3.connect('demo.db')

cursor = conn.cursor()

cursor.execute('''
               
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username VARCHAR(20) UNIQUE ,
            password  TEXT
               )''')

cursor.execute('''
     CREATE TABLE IF NOT EXISTS Tasks(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,             
            name VARCHAR(30),
            desc TEXT,
            FOREIGN KEY(user_id) REFERENCES users(id)
                  )
''')


def register():
    print("Register User")
    # "mohan"
    username = input('enter your username : -').strip()
    if len(username) > 20:
        print('username should not exceed more than 20 chars')
        return
    password = input('enter your password : -')
    conn = sqlite3.connect('third.db')
    cursor = conn.cursor()

    # if password:
    #     for i in password:
    #         if i in '#$%*()&':
    #             print(f'password should not contain {i}')
    #             return

    cursor.execute('''
    INSERT INTO users(username,password)
                   VALUES(?,?)
    ''', (username, password))
    conn.commit()

# AND
# OR
# NOT 

def login():
    conn = sqlite3.connect('third.db')
    cursor = conn.cursor()
    print('LOGIN user')

    username = input('enter your username : -').strip()
    password = input('enter your password : -')

    cursor.execute('''
        SELECT id FROM users WHERE username = ? AND password = ?
    ''', (username, password))
    user = cursor.fetchone()
    print(user)
    if user:
        print('LOgin successfull')
        # print(user)
        # print(user[0])
        return user[0]

    else:
        print('login failed . INvalid creds')


# AND
# OR


def addatasks(user_id):
    # conn = sqlite3.connect('second.db')
    conn = sqlite3.connect('third.db')

    cursor = conn.cursor()
    tname = input('enter task name :')
    tdesc = input('enter task description :')

    cursor.execute('''
        INSERT INTO Tasks(user_id,name,desc)
                   VALUES(?,?,?)
    ''', (user_id, tname, tdesc))

    conn.commit()
    conn.close


# def initdatabase():
#     conn = sqlite3.connect('second.db')
#     cursor = conn.cursor()


def alltasks(user_id):
    # conn = sqlite3.connect('second.db')
    conn = sqlite3.connect('third.db')

    cursor = conn.cursor()

    cursor.execute('''
        SELECT * FROM Tasks WHERE user_id = ?
        ''', (user_id,))
# window key + .

    data = cursor.fetchall()
    if not data:
        print('no tasks found 😒')
    else:
        print(f" {len(data)} tasks found ✅")
        for i in data:
            print(f'TASK {i[0]} ---  {i[2]}')

    # print(data)
conn.close()


def onetask(user_id):
    conn = sqlite3.connect('third.db')
    cursor = conn.cursor()
    t_id = int(input('enter your task id : - '))

    data = cursor.execute('''

    SELECT * FROM Tasks WHERE id = ?

    ''', (t_id,))

    task = data.fetchone()
    print('task found')
    print('-----------------------------')
    print(f'task\t{task[1]} \ndesc\t{task[2]} ')


def updatetask(user_id):
    conn = sqlite3.connect('third.db')
    cursor = conn.cursor()
    t_id = int(input('enter your task id : - '))
    task_name = input('enter new task name : - ')
    task_des = input('eneter new task desc : - ')

    cursor.execute('''
            UPDATE Tasks SET name = ?,desc = ? WHERE id = ?
    ''', (task_name, task_des, t_id))

    conn.commit()
    print('task edited')


def delettasks():
    conn = sqlite3.connect('third.db')
    cursor = conn.cursor()
    t_id = int(input('enter your task id : - '))
    choose = input('Are you sure you want to delete task y/n \n : -')

    if choose == 'y':
        cursor.execute('''

            DELETE FROM Tasks WHERE id = ?

        ''', (t_id,))
        conn.commit()
        print('TASk deleted')
    else:
        print('task not deleted')


def main():
    while True:
        print('-------Main Menu---------')
        print('------------------------- Welcome 🤗 to Task Management -------------------------')
        print("1.Register\n2.Login\n3.Exit")
        ch = int(input('enter your choice:------'))
        if ch == 1:
            register()
        elif ch == 2:
            user_id = login()
            main1(user_id)
        elif ch == 3:
            break
        else:
            print('invaid option')


def main1(user_id):
    while True:
        z = int(input(
            'What do you want \n1.Add Task\n2.View Tasks\n3.Search Task\n4.Update Tasks\n5.Delete Task\n6.Exit-'))
        if z == 1:
            addatasks(user_id)
        elif z == 2:
            alltasks(user_id)
        elif z == 3:
            onetask(user_id)
        elif z == 4:
            updatetask(user_id)
        elif z == 5:
            delettasks()
        elif z == 6:
            break
        else:
            print('invalid choice')


main()

# login()