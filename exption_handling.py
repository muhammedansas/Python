# normal one:
# ////////////////////////////////////////////
# try:
#     a= int(input("enter 1st number"))
#     b= int(input("enter 2nd number"))
#     c= a/b
#     print(c)
# except:
#     print("enter a valid number")    

# finally:
#     print("functionality completed")    

# ///////////////////////////////////////////////////

# using else case:
# try:
#     a = int(input("enter a value"))
#     b = int(input("enter a value"))
#     c = a/b
# except:
#     print("enter a valid number")

# else:
#     print(c)    

# 

# /////////////////////////////////////////////////////
# using while loop:
# while True:
#     try:
        #  a = int(input("enter a value"))
        #  b = int(input("enter a value"))
        #  c = a/b
#     except:
#          print("enter a valid number")
#     else:
#          print(c)          
#          break

# /////////////////////////////////////////////////////////

# giving error name in exeption :   in this case we can write which can show which message
# ///////////////////////////////////////////////////////////

# try:
#     a=int(input("enter a value"))
#     b=int(input("enter a value"))
#     c=a/b
# except ZeroDivisionError:
#     print("cant division by zero")
# except ValueError:
#     print("enter valid input")
# else:
#     print(c)
# finally:
#     print("functionality completed")                

# ///////////////////////////////////////////////////////////////


# using raise method in exeptional handling: create and trigger owm custom error messages
# //////////////////////////////////////////////

try:
    a=int(input("enter a number"))
    b=int(input("enter a number"))
    c=a/b
    if a < 0 :
        raise ValueError("number value is invalid")
    elif a > 50:
        raise ValueError("number is higher than zero")
    
except ValueError as ex:
    print(ex)
else:
    print(c)  




