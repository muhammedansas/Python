# /////////////////////////////  Getter  \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ 

#     A getter is a method used to retrieve the value of an attribute. 
#     It allows controlled access to an attribute, which may be private or protected.


class Employee:
    def __init__(self,name):
        self.__name = name

    def get_name(self):
        return self.__name


obj = Employee('ansas')

print(obj.get_name())