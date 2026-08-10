# ? Plot the points on a cartesian plane which has 2 coordinates x and y .Do the following
#1. Define a class point . Its instance should have 2 attributes x and y. x and y default value must be zero
#2. Define an instance method reset().
#     When called it will set x,y values to zero (ie,. it will set the points to origin(0,0)).
#3. Define an method move().
#      This should change the values of x & y
#4. Use this move method to update reset() method
#5. Define 2 methods xmove and ymove .
#       This should move the values of x and y seperately


# class Point:
#     def __init__(self,x=0,y=0):
#         self.x=x
#         self.y=y
#     def reset(self):
#         self.x,self.y=0,0
#         self.move(0,0)

#     def move(self,a,b):
#         self.x=a
#         self.y=b
#     def xmove(self,a):
#         self.x=a    

#     def ymove(self,b):
#         self.y=b

# p1=Point(1,0)      
# print(p1.x, p1.y)
# p1.reset() 
# print(p1.x,p1.y)      
# p1.move(4,5)
# print(p1.x,p1.y)
# p1.reset() 
# print(p1.x,p1.y)  
# p1.xmove(3)
# print(p1.x)
# p1.ymove(5)
# print(p1.y)


#?  write a python class queue the implements a basic queue data structure with the enqueue and dequeue methods
# The enqueue method should add an element to the rear of the queue, and the dequeue
#  method should remove and return the remaining element from the queue.
# Additionally, include a method is_empty to check if the queue is empty.

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0
q1=Queue()    
q1.enqueue("A")
q1.enqueue("B")
q1.enqueue("C")
print(q1.items)
print(q1.dequeue())
print(q1.is_empty())






