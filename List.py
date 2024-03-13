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
