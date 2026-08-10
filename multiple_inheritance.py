# #multiple inheritence
class Person1:
    def __init__(self):
        pass
    def walk(self):
        print("person can walk")
    def smile(self):
        print("person can smile hahahahahahahaha")
    def speak(self):
        print("person 1 can speak")

class Person2:
    def __init__(self):
        pass
    def read(self):
        print("person can read")
    def write(self):
        print("peson can write")
    def speak(self):
        print("person 2 can speak")    


class Person3:
    def __init__(self):
        pass
    def fly(self):
        print("person can fly")
    def swim(self):
        print("peson can swim")
    def speak(self):
        print("person 3 can speak")

class Person4(Person3,Person2,Person1):
    def __init__(self):
        pass
    def sleep(self):
        print("person can sleep")
    def eat(self):
        print("peson can eat")
    def speak(self):
        print("person 4 can speak")
        super().speak()


p4=Person4()
p4.speak()
#MRO :-- method resolution order
