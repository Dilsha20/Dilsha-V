#abstraction
#data hiding
#possible in through inheritence

from abc import ABC,abstractmethod
class Animal(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def make_sound(self):
        print("animal make sound")
class Dog(Animal):
    def __init__(self):
        pass
    def make_sound(self):
        print("woff woff woff")
d=Dog()
d.make_sound()                