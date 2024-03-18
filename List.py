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


