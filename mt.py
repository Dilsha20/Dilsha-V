import threading
import time

lock=threading.lock()

def work(name):
    if lock:
        for i in range(1,6):
            print(name, i)
            time.sleep(1)
t1 = threading.Thread(target=work, args=("hari",)) #creates a thread

t2= threading.Thread(target=work,args=("mohan",)) #creates a thread
    #print("thread is running")

t1 = threading.Thread(target=work) #creates a thread
t1.start()
t2.start()# starts thread
t1.join()#waits before main program execution
t2.join()