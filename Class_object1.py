# simple example:
# /////////////////////////////////////////////////////////
# class Student:
#     grace_mark = 10      #this one is class attribute
#     def __init__(self,name,id,biolegy,maths,physics):
#         self.name = name
#         self.id = id
#         self.biolegy =biolegy
#         self.maths = maths
#         self.physics = physics

#     def sum(self):
#         self.total = self.biolegy+self.maths+self.physics
#         print("the total score is {}".format(self.total))

#     @classmethod    
#     def change_gracemark(cls,grace_mark):
#         cls.grace_mark = cls.grace_mark + grace_mark
#         print(cls.grace_mark)

# s1 = Student("ansas","Ab234",10,20,30)
# s2 = Student("haidroi","Ba234",30,40,60)
# Student.change_gracemark(40)
# print(s1.maths)
# s1.sum()
# s2.sum()

# //////////////////////////////////////////////////////////////

# class Main:
#     i = 100
#     def __init__(self):
#         self.i="100"
    
#     def meth(name,age):
#         print("name is {} and age is {}".format(name,age))
#     @classmethod
#     def meth2(cls):
#         print(cls.i,'kkk')

#     @staticmethod
#     def m3():
#         print(Main.i)
# Main.i=200
# Main.m3()


# print(Main.i)


 


        