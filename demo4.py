# Decorators in python:
# /////////////////////////////////////////////////////////////////////////
# simple example:

def decorators(fun):
    def wrapper(n):
        any = fun(n)
        return any * 2
    return wrapper


def upper_list(f):
    
    return f.upper()

print(upper_list("hello"))

# # multiple decorators:

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