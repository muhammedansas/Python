# Converting slice to tupple:
# ///////////////////////////////////////////////////
# a = ["apple","mango","orange"]
# print(tuple(a))



# /////////////////////////////////////////////////

# Converting tuple to slice:
# ////////////////////////////////////////////////
# a = ("apple","mango","orange")
# print(list(a))

# /////////////////////////////////////////////////


# access and add and remove list element :
# /////////////////////////////////////////////////////////

# a = ["tomato","onion","cuccumer","lady finger"]
# print(a[0])

# a.append("cabage")
# print(a)

# del a[0]
# print(a)


# ////////////////////////////////////////////////////




# Slicing
# /////////////////////////////////////////////////////
# a = [1,2,3,4,5,6,7,8,9,10,11,12]

# b = a[::2]

# print(b)

# //////////////////////////////////////////////////////





# Lambda function   :   it is an annonymous function it has a multiple parameters and one return value(expression)
# {if someny expressions so use normal function in the case of single expression so we use lambda}
# ///////////////////////////////////////////////////////

# normal:

# def sample(x):
#     return x ** 2

# print(sample(2))



# Lambda:

# a = lambda x : x ** 2
# print(a(2))


# ////////////////////////////i/////////////////////////////////////////////






# if else Statement  :  it is a conditional statement for checking conditions
# ////////////////////////////////////////////////////////////////////////////

# normal:

# a=10

# if a>0:
#     print("Entered number is positive")
# elif a<0:
#     print("entered number is negative")
# else:
#     print("entered number is zero")


# nested if:

# a=-1

# if a>=0:
#     if a>0:
#         print("entered number is positive")
#     else:
#         print("entered number is zero")
# else:
#     print("entered number is negative")   

# //////////////////////////////////////////////////////////  





# while loop :
# //////////////////////////////////////////////
# a = 1
# while a <= 10:
#     print(a)
#     a += 1

# ///////////////////////////////////////////////




# for loop:
# //////////////////////////////////////////////

# in list:
# a =["hi","hello","how are you"]

# for i in a:
#     print(i)


# using range :
# for i in range(6):
#     print(i)

# in the case of what numbers we want:
# for i in range(1,6):
#     print(i)  

# range has 3 parameters 1=start , 2=end , 3=step()  :
# for i in range(1,6,2):
#     print(i)

#<--- ////////////////////////////////////////////////////////--->




# Recursion  :  a function call itself in its own definition
# <----////////////////////////////////////////////////////--->

# def a(n):
#     if n <= 1:
#         return n
#     else:
#         return n + a(n - 1)
    
# print(a(3))      