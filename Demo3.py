# Recursion  :  a function call itself in its own definition
# <----////////////////////////////////////////////////////--->

def a(n):
    if n <= 1:
        return n
    else:
        return n + a(n - 1)
    
print(a(4))      