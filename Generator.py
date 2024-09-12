# normal case of generator :        when a generator creates that creates an iterator 
# ////////////////////////////////////////////////////////////////////
# def main():
#     yield 5            # when the yield works we dont want to make that value an iterator the yield make that

# value = main()

# print(next(value))


# for loop case:
# /////////////////////////////////////////////////////

# def main():
#     yield 3
#     yield 2
#     yield 5

# value = main()

# for i in value:
#     print(i)


# while loop case:
# ///////////////////////////////////////////////////////

# def main():
#     n = 1

#     while n <=10:
#         yield n
#         n += 1

# value = main()
# for i in value:
#     print(i)        

