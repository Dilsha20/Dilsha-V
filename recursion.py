#recursion
# higher order functions

# when a function get a function as its argument
# when a function return a function


# recursion 
# def hello():
#     print("mohan")
#     return hello()
# hello()

#10 number
# def countzero(n):
#     print(n)
#     if n==0:
#         return #stop
#     return countzero(n-1) #condition
# countzero(10)

#sum
# def sumzero(n):
#     if n==0:
#         return 0
#     return n + sumzero(n-1)
# print(sumzero(10))



#factorial
# def factorial(n):
#     if  n==0:
#         return 0
#     return n*factorial(n-1)
# print(factorial(10))


#scope of a variable
#scope - area in which it is recognised


# name="risal" #global scope
# def myname():
#     name="sreeja" # local scope
# print(name)



# name="risal" #global scope
# def myname():
#     name="sreeja"
#     print(name)
# myname()



# name="risal" #global scope
# def myname():
#     name="sreeja"
#     def nickname(): # local scope
#         name="yazil"
#         print(name)
#     nickname()
# myname()        


# L E G B
# local enclosing global built in
