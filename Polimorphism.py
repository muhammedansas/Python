# Method over riding:
# ////////////////////////////////////////
# class Animal:
#     def speak(self):
#         print("Animal speaks")

# class Dog(Animal):
#     def speak(self):
#         print("Dog barks")
        
# class Cat(Animal):
#     def speak(self):
#         print("Cat meows")

# # Creating instances of Dog and Cat
# dog = Dog()
# cat = Cat()

# # Calling the speak method on instances
# dog.speak()  # Output: Dog barks
# cat.speak()  # Output: Cat meows


# /////////////////////////////////////////////////////////////////

# Constructor Overloading:-

# class A():
#     def __init__(self,name,age,place):
#         print("1st constructor")


# class B(A):
#     def __init__(self,name,age,place=None):
#         super().__init__(name,age,place)
#         print("2nd constructor")


# B("ansa",2,'hj')

# /////////////////////////////////////////////////

# class A():
#     def __init__(self):
#         print("1st constructor")


# class B(A):
#     def __init__(self):
#         print("2nd constructor")
        
        
# class C(B):
#     def __init__(self):
#         super(B,self).__init__()
#         print("3nd constructor")


# C()