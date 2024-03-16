# single inheritnce:
# //////////////////////////////////////////
# class School:
#     def make_sound(self):
#         print("this is an lp section")

# class Student(School):
#     def make_sound(self):
#        print("hi")
       
        

# s1 = Student()
# s1.make_sound()

# //////////////////////////////////////////
# multiple inheritence:
# ///////////////////////////////////////////
class Main:
    def first(self):
        print("its first method")

class Second:
    def second(self):
        print("its second method")

class Child(Main,Second):
    def third(self):
        print("its third method")
    

obj1 = Child() 
obj1.first()
obj1.second()
obj1.third()     