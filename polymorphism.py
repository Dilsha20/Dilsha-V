# #polymorphism
# #poly=many morphism-forms

# #method overloading
# #method overriding
# #operator overloading


# #operator overloading
# # class Student:
# #     def __init__(self,m1,m2):
# #         self.m1=m1
# #         self.m2=m2
# #     def __add__(self, otr):
# #         return self.m1+self.m2,otr.m1+otr.m2

# # s1=Student(7,8)
# # s2=Student(9,7)           
# # print(s1+s2)

# #__sub__
# class Student:
#     def __init__(self,m1,m2):
#         self.m1=m1
#         self.m2=m2
#     def __sub__(self, otr):
#         return self.m1-self.m2,otr.m1-otr.m2

# s1=Student(7,8)
# s2=Student(9,7)           
# print(s1-s2)

# #__mul__
# class Student:
#     def __init__(self,m1,m2):
#         self.m1=m1
#         self.m2=m2
#     def __mul__(self, otr):
#         return self.m1*self.m2,otr.m1*otr.m2

# s1=Student(7,8)
# s2=Student(9,7)           
# print(s1*s2)

# #__truediv__
# class Student:
#     def __init__(self,m1,m2):
#         self.m1=m1
#         self.m2=m2
#     def __truediv__(self, otr):
#         return self.m1/self.m2,otr.m1/otr.m2

# s1=Student(7,8)
# s2=Student(9,7)           
# print(s1/s2)

# #__gt__
# class Student:
#     def __init__(self,m1,m2):
#         self.m1=m1
#         self.m2=m2
#     def __gt__(self, otr):
#          return self.m1>self.m2,otr.m1>otr.m2
# s1=Student(7,8)
# s2=Student(9,7)           
# print(s1>s2)    



# #method overloading
#not possible in python



# #method overriding
class A:
    def __init__(self):
        pass
    def hello(self):
        print ("a hello")

class B(A):
    def __init__(self):
         pass
    def hello(self):
        print("B hello")
b1=B()
b1.hello()    