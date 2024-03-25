# magic method:
# ////////////////////////////////////////////////////////////////
# they are called magic methods because they are automatically invoked by python in responce




# Add magic method: like this method have two parameter like num. num know as the second object argument
# /////////////////////////////////////
class Auther:
    def __init__(self,name):
        self.name = name
    
    def __add__(self,num):
        return self.name + num.name

obj = Auther(20)
obj1 = Auther(30)
print(obj+obj1)



# str magic method:  str method have one parameter is self it return a string
# //////////////////////////////////////////////////////
class Main:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return "the name is {} the age is {}".format(self.name,self.age)    

obj = Main("ansas",21)
print(obj)




        