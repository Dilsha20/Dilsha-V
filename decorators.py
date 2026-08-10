 #decorators
# #functions that enhances other function
# #*args --multiple poositional arguments
# #**kwargs --multiple keyword arguments
# #higher order function---- a function as its argument or returns a function
# #@saymyname ---decorater call --saymyname is a function name
 
# def saymyname(fun):
#     def wrapper():
#         print("say my name")
#         fun()
#         print("you are right")
#     return wrapper

# @saymyname
# def add():
#     print("add 2 numbers")    
# add() 

# #*args 
# #positional arguments
# def add(*args):
#     return args
# print(add(2,5,8,65,55,4,454,87,8,87,787,8,878,4455,545))
# #**kwargs
# #keyword arguments
# def fullname(**kwargs):
#     print(kwargs)
# fullname(fname="dil",mname="sha", lname="mus", tname="thafa")   

# #time module
# import time
# # print(time.time()) #current local time in seconds
# # print(time.ctime()) #current local time
# # print(time.ctime(1784183545.3531551))
# # start=time.time()
# # for i in range(1,11):
# #     print(i)
# #     time.sleep(1) #delay 
# # stop=time.time()
# # print("total time:",stop-start)  

# # def totaltime(fun):
# #     def wrapper(*args,**kwargs):
# #         start = time.time()
# #         fun(*args,**kwargs)
# #         stop=time.time()
# #         print(f"total time: {stop-start}")
# #     return wrapper 
# # @totaltime
# # def myname(n):
# #     for i in range(n):
# #         print(i)
# #         time.sleep(1)
# # myname(5)        


# def totaltime(n):
#     def innner(fun):
#         def wrapper(*args,**kwargs):
#             print("executed",n,"times")
#             start = time.time()
#             fun(*args,**kwargs)
#             stop=time.time()
#             print(f"total time: {stop-start}")
#         return wrapper 
#     return innner

# @totaltime(10)
# def myname(n):
#     for i in range(n):
#         print(i)
#         time.sleep(1)
# myname(2)
