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
# class Main:
#     def first(self):
#         print("its first method")

# class Second:
#     def second(self):
#         print("its second method")

# class Child(Main,Second):
#     def third(self):
#         print("its third method")
    

# obj1 = Child() 
# obj1.first()
# obj1.second
# obj1.third() 

# /////////////////////////////////////////
# multilevel inheritence:
# ////////////////////////////////////////
# class Main:
#     def first(self):
#         print("its first method")

# class Child1(Main):
#     def second(self):
#         print("its second method")

# class Chaild2(Child1):
#     def third(self):
#         print("its third method")

# obj1 = Chaild2()
# obj1.first()    
# obj1.second()
# obj1.third()    

# /////////////////////////////////////////////////

# Hierarchical inheritence:-
#       multiple subclasses inherit from the same 
# /////////////////////////////////////////////////////

# class Animal():
#     def speak(self):
#         print("speaking")

# class Dog(Animal):
#     def bark(self):
#         print("barking")       

# class Cat(Animal):
#     def meow(self):
#         print("mewign")

# obj = Cat()
# obj.speak()

