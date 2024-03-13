#  *args:  this one can access multiple number of values this return a tuple
# //////////////////////////////////////////////////////
# def main(x,*args):
#     print(x)
#     return sum(args,x)

# print(main(1,2,3,4))

# ////////////////////////////////////////

# keyword arguments:
# //////////////////////////////////////

# def main(name,age):
#     print(f"my name is {name} and my age is {age}")

# main(name="ansas",age=21)

# /////////////////////////////////////////

# **kwargs:   it allows pass number of keyword arguments this returns a dictionary key value pairs
# ////////////////////////////////////////////

# def main(**kwargs): #kwargs is optional we can give any name
#     print(kwargs)

# main(name="ansa",age=21,place="olavanna")


# capitalise values using kwargs:

# def main(**kwargs):
#     for key,value in kwargs.items():
#       if  isinstance(value,str):
#         kwargs[key] = value.capitalize()
#     print(kwargs)    

# main(name="aNsAs",age=21,place="oLAVannA",aa="kHaDhAr",bb=40)        

# Decorators in python:
# /////////////////////////////////////////////////////////////////////////
# simple example:

# def decorators(fun):
#     def wrapper(n):
#         any = fun(n)
#         return any * 2
#     return wrapper

# @decorators
# def upper_list(f):
    
#     return f.upper()

# print(upper_list("hello"))

# multiple decorators:

# def decorators1(fun):
#     def wrapper(s):
#         result = fun(s)
#         return result.upper()
#     return wrapper

# def decorators2(fun):
#     def wrapper(s):
#         result = fun(s)
#         return result * 2
#     return wrapper


# @decorators1
# @decorators2              #:  This is called decorators chaining. we can add multiple decorators in one function
# def print_name(f):
#     return f

# print(print_name("my name is ansas"))

# ////////////////////////////////////////////////////////////////////////////////

