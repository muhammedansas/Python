# encapsulation:
# //////////////////////////////

# private attribute and method:
# ///////////////////////////////

# class encaps:
#     def __init__(self):
#         self.__name = "ansas"

#     def __main(self):
#         print(self.__name)    

# obj = encaps()                        
# print(obj._encaps__name)                # : this is name angling for access a private attribute

# obj._encaps__main()                     # : this is name angling for access a private method
        
# /////////////////////////////////////////////////////////////////////////////////////////////         

# encapsulation getter and setter:
# //////////////////////////////////////

class A:
    def __init__(self,name,age):
        self.__name=name
        self.age=age

    def get_name(self,age):
        self.__name=age
        print(self.__name)

    def set_name(self,name):
        print()   

    def abc(self):
        print(self.__name)    


obj = A("ansas",21)
obj.get_name("vicky")        