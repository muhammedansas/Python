class School:
    def make_sound(self):
        print("this is an lp section")

class Student(School):
    def make_sound(self):
       print("hi")
       
        

s1 = Student()
s1.make_sound()