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
