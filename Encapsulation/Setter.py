# ///////////////////////////////  Setter  \\\\\\\\\\\\\\\\\\\\\\\\\\\

    # A setter is a method used to update the value of an attribute. 
    # It can include validation to ensure that only valid values are assigned to an attribute.


class Employee:
    def __init__(self,name):
        self.__name = name

    def set_name(self,name):                                     # this is for setting/changing the private value
        self.__name = name
        print(self.__name)

obj = Employee('ansas')

obj.set_name('mishal')




