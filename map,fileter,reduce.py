from functools import reduce

# map :  map function has two arguments 1st one is a function this function was impild or user defined functions
    #    the second argument is a iterator like list
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# using userdefined function:
# def main(x):
#     return x*2

# print(list(map(main,[1,2,3,4,5]))) 



# using predefined function:
# new_list = [1,2,-3,4,-6]

# print(list(map(abs,new_list)))   #abs return a absolute value like there is no negative numbers


# using lambda function:
# new_list = [1,2,4,5,6]

# print(list(map(lambda x:x*2,new_list)))


# //////////////////////////////////////////////////////////////////////////////////////////////



# filter:    based on specified conditions
# //////////////////////////////////////////////////////////////
# def main(x):
#     if x>0:
#         return x
#     else:
#         None

# print(list(filter(main,[1,2,-4,-7])))

# using lambda:
# print(list(filter(lambda x : x.isupper(),"HeLLo")))

# ///////////////////////////////////////////////////////////////


# reduce : reduce has a 3rd parameter is an initializer like which value wants to start
# ////////////////////////////////////////////////////////////////
# def main(x,y):     #x taking sum of values or other conditional base y taking next values
#     return x+y

# print(reduce(main,[1,2,3,4,5]))


# using lambda:
# print(reduce(lambda x,y:x+y,[1,2,3,4,5]))


# using 3rd parameter(initializer):
# def main(x,y):
#     return x+y
# print(reduce(main,[1,2,3,4,5],10))

# //////////////////////////////////////////////////////////////////

a= 10
b=20
print("entered number is {} fghjk{}".format(a,b))