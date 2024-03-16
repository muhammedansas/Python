# Method over riding:
# ////////////////////////////////////////
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

# Creating instances of Dog and Cat
dog = Dog()
cat = Cat()

# Calling the speak method on instances
dog.speak()  # Output: Dog barks
cat.speak()  # Output: Cat meows