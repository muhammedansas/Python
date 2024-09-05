# ////////////////////////  Name Mangling  \\\\\\\\\\\\\\\\\\\\\\\\\\

# Name mangling is a technique Python uses to ensure that private attributes (defined with a double underscore __) are not easily accessible from outside the class. 
# It modifies the attribute's name to make it more difficult to access directly, adding a prefix based on the class name.

class Employee:
    def __init__(self,name):
        self.__name = name

obj = Employee('ansas')

print(obj._Employee__name)