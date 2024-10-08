# Add to list to another list:
# /////////////////////////////
# x = [1,2,3,4]
# y = [5,6,7,8]
# z = x+y
# print(z)


# Add list_1 into list_2 using extend:
# //////////////////////////////////////
# list_1 = [1,2,3,4]
# list_2 = [5,6,7,8]
# list_1.extend(list_2)
# print(list_1)

# //////////////////////////////////////////    

# merge two list using loop:
# /////////////////////////////
# list_1 = [1,2,3,4]
# list_2 = [5,6,7,8]

# for x in list_2:
#     list_1.append(x)

# print(list_1)    

# Find prime number in an list:
# ///////////////////////////////
# normal:

# list_1 = list(range(1,50))
# new_list = []

# for i in list_1:
#     list_2 = []
#     for j in range(1,i//2+1):
#         if i%j == 0:
#             list_2.append(j)
#     if len(list_2) <= 1 :
#         new_list.append(i)

# print(new_list)               


# using list comprehension:

# list_1 = list(range(1,50))
# new_list = [i for i in list_1 if len([x for x in range(1,i//2+1) if i%x == 0])<=1]
# print(new_list)

# //////////////////////////////////////////////////////////////

# list value give another list:
# ////////////////////////////////
# new_list = [1,2,3,4,5]
# square_list = []
# for i in new_list:
#     square_list.append(i**2)

# print(square_list)   

# same one using listcomprehension:
# ////////////////////////////////

# new_list = [1,2,3,4,5]

# square_list = [i**2 for i in new_list if i>2]

# print(square_list)

# ////////////////////////////////////

# change values of a list:
# ////////////////////////////////////

# new_list = [1,"hi guys",[3,4,5],(4,5,6)]
# new_list[1] = "hello guys"
# print(new_list)
# new_list[2] = "this is changed value"
# print(new_list)

# remove elements in list different ways:
# //////////////////////////////////////////////
# using remove method:.

# new_list = [1,2,3,4,5,6] 
# new_list.remove(3)                    # :   what element wants to be delete using remove method
# print(new_list)

# using pop method:

# new_list = [1,2,3,4,5]
# new_list.pop(2)                       # : remove which intex number value
# print(new_list)                        

# using del method:

# new_list = [1,2,3,4,5]
# del new_list[2]                         # : this method also delete index value                     
# print(new_list) 

# del new_list
# print(new_list)                         # : this method can delete an entire list

# using list comprehension method:

# new_list = [1,2,3,4,5,6]
# new_list = [x for x in new_list if x != 3]        # : this means first iterate list values and give an if condition for delete 3
# print(new_list)


# creating new list using list():
# x = list(('apple','mango',1,2,4))
# print(x)


# a = (1,2,3,4,"aaa")

# # x = a[:4] + (5,) + a[4:]
# # print(x)

# try:
#     a =10 
#     if a <9:
#         print("this is true")
# except:
#     print("this is false")    

# def dec(fun):
#     def wrapper(name):
#         result = fun(name)
#         return result.upper() 
#     return wrapper 
    

# def main(name):
#     return name+ " helloo world"   
    
# f = dec(main)
# print(f("helloo"))



class Main():
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        val = self.num
        if val < 9:
            self.num += 1
            return val
        else:
            raise StopIteration

obj1 = Main()

print(next(obj1))

for i in obj1:
    print(i)
