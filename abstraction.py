# /////////////////////////////////////  Abstraction  \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# Abstraction in Python refers to the concept of hiding the implementation details of a function or a class and only exposing the essential functionalities. 
# It allows you to focus on what an object does rather than how it does it. In Python, abstraction is achieved using abstract classes and interfaces, typically implemented using the abc module.



from abc import ABC ,abstractclassmethod

class A(ABC):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    @abstractclassmethod                             # must want to use this abstractmethod otherwise this not a abstract class and also inherit the ABC module
    def abc(self):
        pass                                         # the abstract class method must want the implimentation and rest will do the inherited class

    def acb(self):
        print(self.age)

class B(A):
    def abc(self):                                   # abstract class only define the method and the rest will do the ingerited class
        print(self.age)    


obj1 = B("ansas",21)
obj1.acb()



class Solution(object):
    def searchInsert(self, nums, target):
        if target in nums:
            return nums.index(target)
        else:
            nums.append(target)
            nums.sort()
            a = nums.index(target)
            nums.remove(target)
            return a