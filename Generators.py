#generators
# lazy iterables--- values on demand
# list,tuple,set,etc are iterables

# def mydata():
#     return "one"

# print(mydata())

#generator creation

# def mydata():
#     yield "one"
#     yield "two"
#     yield "three"
#     yield "four"
# a=mydata()
# print(next(a))
# print(next(a))
# print(next(a))
 
# b=[]
# i=0
# while True:
#     b.append(i)
#     i=i+1


# def inifinz():
#    i=1
#    while True:
#        yield i
#        i=i+1
# inifine_numbers=inifinz()
# print(inifine_numbers)
# for i in inifine_numbers:
#     print(i) 

import sys
a=[]
for i in range(1,10000001):
    a.append(i)
def crore():
    for i in  range(1,10000001):
        yield i
b=crore()
print(sys.getsizeof(a))   
print(sys.getsizeof(b))                  
