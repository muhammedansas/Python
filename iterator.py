# class Main:

#     def __init__(self):
#         self.num = 1
#         pass

#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.num <=10:
#             val = self.num
#             self.num += 1
#             return val
#         else:
#             raise StopIteration

# obj = Main()

# for i in obj:
#     print(i)



# iterator
# list1=[1,2,3,4,5,6]

# l=iter(list1)

# print(next(l))


# generator

# def m(n):
#     c=0
#     while c<n:
#         yield c
#         c+=1
       
        
# k=m(5)

# print(next(k))
# print(next(k))
# print(next(k))


# encapsulation

class A:
   def __init__(self):
      self.__name="vicky"

  



obj=A()
print(obj._A__name)



