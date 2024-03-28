from abc import ABC ,abstractclassmethod

class A(ABC):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    @abstractclassmethod
    def abc(self):
        print(self.name)

    def acb(self):
        print(self.age)


obj = A("ansas",21)
obj.abc()        
