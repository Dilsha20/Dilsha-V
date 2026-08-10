#object oriented programming

# 1.object
#object is an instance of a class
#instance-
#real world entity
#attributes-define an object
#behaviours/methods
# 
# 2.class- 
#blueprint of an object
# to create pbjects
# eg:- car-attribute
# nmae,model,color,year
#methoda- functions inside a class eg(start(),stop(),etc....)

# class Car:
#     def start():
#         print("car has started")
#     def stop():
#         print("car stopped")
# c1=Car
# c2=Car
# c3=Car
# c4=Car
# c1.start()
# c1.stop() 

# class Bike:
#     def start():
#         print("Bike has started")
#     def stop():
#         print("Bike has stopped")
# b1=Bike
# b2=Bike
# b3=Bike
# b4=Bike
# b2.start()
# b2.stop()

#constructor
#used to initialize an object
#__init__()
#self using to point the current object reffering
# class Car:
#     def __init__(self,n,c):
#         self.name=n
#         self.color=c
#     def start(self):
#         print(f"{self.name} has started")
#     def stop(self):
#         print("car stopped")
# c1=Car("swift","black")
# c2=Car("city","red")
# c3=Car
# c4=Car
# c1.start()
# c1.stop() 

#create a class student with 6 attributes (name,m1,m2,m3,m4,m5)
# 3 methods   (sum of mark(),average of mark(),disply())

# class Student:
#     def __init__(self,n,m1,m2,m3,m4,m5):
#         self.name=n
#         self.mark1=m1
#         self.mark2=m2
#         self.mark3=m3
#         self.mark4=m4
#         self.mark5=m5
#     def start(self):
#         print(self.name)
#         print(f"sum={self.mark1+self.mark2+self.mark3+self.mark4+self.mark5}") 
#     def stop(self):
#         print(f"avg={(self.mark1+self.mark2+self.mark3+self.mark4+self.mark5)/5}")  

# s1=Student("dilsha",50,50,50,50,50)
# s2=Student("amreena",45,45,45,45,45)
# s3=Student("thanza",48,49,47,46,45)
# s3.start()
# s3.stop()


#or
class Student12:
    def __init__(self,n,m1,m2,m3,m4,m5):
        self.name=n
        self.m1=m1
        self.m2=m2
        self.m3=m3
        self.m4=m4
        self.m5=m5
    def sum_of_marks(self):
        return self.m1+self.m2+self.m3+self.m4+self.m5
    def average_of_marks(self):
        return self.sum_of_marks()/5
    def display(self):
        print(f"student{self.name} has marks of {self.m1} , {self.m2} , {self.m3}, {self.m4} , {self.m5} , the sum of marks is {self.sum_of_marks()} and the average of mark is {self.average_of_marks()}")
s1 = Student12("Dilsha",49,50,47,46,44)
s1.display()        


#quiz game with timer
#import time